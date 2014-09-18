# Copyright (c) 2010 Infrae / Technical University Delft. All rights reserved.
# See also LICENSE.txt
import StringIO, socket, httplib, urlparse, logging
from time import sleep
from copy import copy

class APIException(Exception):
    """ An exception in the general usage of the API """
    pass

    
class FedoraConnectionException(Exception):
    """ An exception thrown by Fedora connections """
    def __init__(self, httpcode, reason=None, body=None):
        self.httpcode = httpcode
        self.reason = reason
        self.body = body

    def __repr__(self):
        return 'HTTP code=%s, Reason=%s, body=%s' % (
                    self.httpcode, self.reason, self.body.splitlines()[0])

    def __str__(self):
        return repr(self)


class Connection(object):
    """
    Represents a connection to a Fedora-Commons Repository using the REST API
    http://fedora-commons.org/confluence/display/FCR30/REST+API    
    """
    def __init__(self, url, debug=False,
                 username=None, password=None, 
                 persistent=False):
        """
         url -- URI pointing to the Fedora server. eg.
         
            http://localhost:8080/fedora/
            
         persistent -- Keep a persistent HTTP connection open.
                Defaults to true
        """        
        self.scheme, self.host, self.path = urlparse.urlparse(url, 'http')[:3]
        self.url = url
        self.username = username
        self.password = password
        self.debug = debug
        
        self.persistent = persistent
        self.reconnects = 0
        self.conn = httplib.HTTPConnection(self.host)

        self.form_headers = {}
        
        if not self.persistent:
            self.form_headers['Connection'] = 'close'
        
        if self.username and self.password:
            token = ('%s:%s' % (self.username,
                                self.password)).encode('base64').strip()
            self.form_headers['Authorization'] = 'Basic %s' % token
        
    def close(self):
        self.conn.close()

    def open(self, url, body='', headers=None, method='GET'):
        if headers is None:
            http_headers = {}
        else:
            # Copy because in an edge case later we may alter the headers.
            http_headers = copy(headers)
        if url.startswith('/'):
            url = url[1:]
        url = '%s/%s' % (self.path, url)
        
        # Fedora doesn't like a zero length message body when ingesting a datastream.
        if body == '' and (method == 'PUT' or method == 'POST') and 'datastreams/' in url:
            logging.debug('Body empty for HTTP request using'
                          ' fake form for datastream ingest.')
            
            # Establish the mime type and boundary.
            parsed = urlparse.urlparse(url)

            try:
                mime_type = urlparse.parse_qs(parsed.query)['mimeType']

                if not mime_type:
                    mime_type = 'application/octet-stream'
                boundary = '----------ThIs_Is_tHe_bouNdaRY_$'

                # Build message body.
                body = (('--{0}{1}Content-Disposition: form-data;'
                        ' name="file"; filename="IGNORE THE HACK."{1}'
                        'Content-Type: {2}{1}{1}{1}--{0}--{1}').format(boundary, '\r\n', mime_type))

                # Change headers for new content type.
                http_headers.update({
                    'User-Agent': 'INSERT USERAGENTNAME',
                    'Content-Type': 'multipart/form-data; boundary=%s' % boundary
                })
            except KeyError:
                pass

        # Send out the request.
        attempts = 3
        while attempts:
            try:
                logging.debug('Trying %s on %s' % (method, url))
                # We can't have unicode characters floating around in the body.
                self.conn.request(method, url, body, http_headers)
                return check_response_status(self.conn.getresponse())
            except (socket.error,
                    httplib.ImproperConnectionState,
                    httplib.BadStatusLine):
                    # We include BadStatusLine as they are spurious
                    # and may randomly happen on an otherwise fine
                    # connection (though not often)
                logging.exception('Got an Exception in open')
                self._reconnect()
                attempts -= 1
                if not attempts:
                    raise
            except FedoraConnectionException as e:
                attempts -= 1
                if not attempts or e.httpcode not in [409]:
                    logging.exception('Got HTTP code %s in open...  Failure.' % e.httpcode)
                    raise e
                else:
                    logging.exception('Got HTTP code %s in open... Retrying...' % e.httpcode)
                    self._reconnect()
                    sleep(5)
        if not self.persistent:
           self.close()
        
    def _reconnect(self):
        self.reconnects += 1
        self.close()
        self.conn.connect()
        
def check_response_status(response):
    if response.status not in (200, 201, 204):
        ex = FedoraConnectionException(response.status, response.reason)
        try:
            ex.body = response.read()
        except:
            pass
        raise ex
    return response
