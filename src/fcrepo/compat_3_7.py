fake_wadl = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<application xmlns="http://research.sun.com/wadl/2006/10">
    <doc xmlns:jersey="http://jersey.dev.java.net/" jersey:generatedBy="Jersey: 1.0.3.1 08/14/2009 04:21 PM"/>
    <resources base="http://atmintis.mb.vu.lt:8080/fedora/objects/">
        <resource path="/{pid}">
            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
            <method name="POST" id="createObject">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="label"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="logMessage"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="info:fedora/fedora-system:FOXML-1.1" type="xs:string" style="query" name="format"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="UTF-8" type="xs:string" style="query" name="encoding"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="namespace"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="ownerId"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="A" type="xs:string" style="query" name="state"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="false" type="xs:boolean" style="query" name="ignoreMime"/>
                </request>
                <response>
                    <representation mediaType="*/*"/>
                </response>
            </method>
            <method name="GET" id="getObjectProfile">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                </request>
                <response>
                    <representation mediaType="text/html"/>
                    <representation mediaType="text/xml"/>
                </response>
            </method>
            <method name="DELETE" id="deleteObject">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="logMessage"/>
                </request>
                <response>
                    <representation mediaType="*/*"/>
                </response>
            </method>
            <method name="PUT" id="updateObject">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="label"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="logMessage"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="ownerId"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="state"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="lastModifiedDate"/>
                </request>
                <response>
                    <representation mediaType="text/plain"/>
                </response>
            </method>
            <resource path="/versions">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="GET" id="getObjectHistory">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
            <resource path="/objectXML">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="GET" id="getObjectXML">
                    <response>
                        <representation mediaType="text/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/validate">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="GET" id="doObjectValidation">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                    </request>
                    <response>
                        <representation mediaType="text/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/export">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="GET" id="getObjectExport">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="info:fedora/fedora-system:FOXML-1.1" type="xs:string" style="query" name="format"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="context"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="UTF-8" type="xs:string" style="query" name="encoding"/>
                    </request>
                    <response>
                        <representation mediaType="text/xml"/>
                        <representation mediaType="application/zip"/>
                    </response>
                </method>
            </resource>
        </resource>
        <resource path="/{pid}/methods">
            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
            <method name="GET" id="getAllObjectMethods">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                </request>
                <response>
                    <representation mediaType="text/html"/>
                    <representation mediaType="text/xml"/>
                </response>
            </method>
            <resource path="/{sDef}">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="sDef"/>
                <method name="GET" id="getObjectMethodsForSDef">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                    </request>
                    <response>
                        <representation mediaType="text/html"/>
                        <representation mediaType="text/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{sDef}/{method}">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="method"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="sDef"/>
                <method name="GET" id="invokeSDefMethodUsingGET">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
        </resource>
        <resource path="/{pid}/relationships">
            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
            <method name="GET" id="getRelationships">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="subject"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="predicate"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="rdf/xml" type="xs:string" style="query" name="format"/>
                </request>
                <response>
                    <representation mediaType="application/rdf+xml"/>
                    <representation mediaType="text/plain"/>
                    <representation mediaType="application/x-turtle"/>
                    <representation mediaType="application/sparql-results+xml"/>
                </response>
            </method>
            <method name="DELETE" id="purgeRelationship">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="subject"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="predicate"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="object"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:boolean" style="query" name="isLiteral"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="datatype"/>
                </request>
                <response>
                    <representation mediaType="*/*"/>
                </response>
            </method>
            <resource path="/new">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="POST" id="addRelationship">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="subject"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="predicate"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="object"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:boolean" style="query" name="isLiteral"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="datatype"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
        </resource>
        <resource path="/{pid}/datastreams">
            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
            <method name="GET" id="listDatastreams">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                </request>
                <response>
                    <representation mediaType="*/*"/>
                </response>
            </method>
            <resource path="/{dsID}/content">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="dsID"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="GET" id="getDatastream">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="download"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
            <resource path="/{dsID}">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="dsID"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="POST" id="addDatastream">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="X" type="xs:string" style="query" name="controlGroup"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="dsLocation"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="altIDs"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="dsLabel"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="true" type="xs:boolean" style="query" name="versionable"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="A" type="xs:string" style="query" name="dsState"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="formatURI"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="checksumType"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="checksum"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="mimeType"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="logMessage"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
                <method name="PUT" id="modifyDatastream">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="dsLocation"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="altIDs"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="dsLabel"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:boolean" style="query" name="versionable"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="dsState"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="formatURI"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="checksumType"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="checksum"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="mimeType"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="logMessage"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="false" type="xs:boolean" style="query" name="ignoreContent"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="lastModifiedDate"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
                <method name="GET" id="getDatastreamProfile">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="asOfDateTime"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="false" type="xs:boolean" style="query" name="validateChecksum"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
                <method name="DELETE" id="deleteDatastream">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="startDT"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="endDT"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="logMessage"/>
                    </request>
                    <response>
                        <representation mediaType="application/json"/>
                    </response>
                </method>
            </resource>
            <resource path="/{dsID}/history">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="dsID"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="template" name="pid"/>
                <method name="GET" id="getDatastreamHistory">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
        </resource>
        <resource path="/objects">
            <method name="GET" id="searchObjects">
                <request>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="terms"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="query"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="25" type="xs:int" style="query" name="maxResults"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="sessionToken"/>
                    <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="resultFormat"/>
                </request>
                <response>
                    <representation mediaType="text/html"/>
                    <representation mediaType="text/xml"/>
                </response>
            </method>
            <resource path="nextPID">
                <method name="POST" id="getNextPID">
                    <request>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="1" type="xs:int" style="query" name="numPIDs"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" type="xs:string" style="query" name="namespace"/>
                        <param xmlns:xs="http://www.w3.org/2001/XMLSchema" default="text/html" type="xs:string" style="query" name="format"/>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
        </resource>
    </resources>
</application>
'''