from request import *

class App:
	def __init__( self , appid = None ):
		if ( not appid ):
			raise slAppException( 'No application ID provided' )
		self.appid = appid
	def request( self , resource , method , data = None ):
		return request( self.appid , resource , method , data )
	def run( self , code , language , stdin = None ):
		data = { "code" : code , "language" : language , "input" : stdin }
		return self.request( "exec" , "create" , data )

class slAppException( Exception ):
	def __init__( self , value ):
		self.value = value
	def __str__( self ):
		return repr( self.value )
