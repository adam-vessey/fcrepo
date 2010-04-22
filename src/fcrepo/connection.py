import socket
import httplib
import urlparse
import logging

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
                    self.httpcode, self.reason, self.body)

    def __str__(self):
        return 'HTTP code=%s, reason=%s, body=%s' % (
                    self.httpcode, self.reason, self.body)


class Connection(object):
    """
    Represents a connection to a Fedora-Commons Repository using the REST API
    http://fedora-commons.org/confluence/display/FCR30/REST+API    
    """
    def __init__(self, url, debug=False,
                 username=None, password=None, 
                 persistent=True):
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
        
        self.xmlheaders = {'Content-Type': 'text/xml; charset=utf-8'}
        if not self.persistent:
            self.xmlheaders['Connection'] = 'close'

        self.form_headers = {
                'Content-Type':
                'application/x-www-form-urlencoded; charset=utf-8'}

        if not self.persistent:
            self.form_headers['Connection'] = 'close'
        
        if self.username and self.password:                
            authz = ('%s:%s' % (self.username, self.password)).strip().encode('base64')
            self.form_headers['Authorization'] = 'Basic %s' % authz
        
    def close(self):
        self.conn.close()

    def open(self, url, body='', headers=None, method='GET',):
        if headers is None:
            headers = {}
        if url.startswith('/'):
            url = url[1:]
        url = '%s/%s' % (self.path, url)
        attempts = 3
        while attempts:
            try:
                logging.debug('Trying %s on %s' % (method, url))
                self.conn.request(method, url, body, headers)
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
