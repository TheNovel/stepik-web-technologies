def app(env, start_response):
	body = []
	for elem in environ['QUERY_STRING'].split('&'):
		body += [elem]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return body