def app(environ, start_response):
	body = ''
	for elem in environ['QUERY_STRING'].split('&'):
		body = body + elem + '\n'
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return body.strip()