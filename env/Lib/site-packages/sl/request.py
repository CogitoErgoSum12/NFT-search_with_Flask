import httplib, urllib , json
def request( appid , resource , method , data = None ):
	resources = [ "exec" ]
	if ( not resource in resources ):
		raise Exception( "Invalid resource" )
	methods = [ "list" , "view" , "create" , "update" , "delete" ]
	if ( not method in methods ):
		raise Exception( "Invalid method" )
	request_methods = { "list" : "GET" , "view" : "GET" , "create" : "POST" , "update" : "POST" , "delete" : "POST" }
	request_method = request_methods[ method ]
	conn = httplib.HTTPConnection( "api.sourcelair.com" )
	urldir = "/" + resource + "/" + method + "?app=" + appid
	params = urllib.urlencode( data )
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "*/*"}
	conn.request( "POST" , urldir , params , headers )
	response = conn.getresponse()
	data = response.read()
	if ( response.status == 400 ):
		raise slRequestException( data )
	return json.loads( data ) 


class slRequestException( Exception ):
	def __init__( self , value ):
		self.value = value
	def __str__( self ):
		return repr( self.value )

