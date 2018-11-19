def app(environ, response):
    params=environ['QUERY_STRING'].replace('&','\n')
    headers=[('Content-Type', 'text/plain')]
    response('200 OK', headers)
    return [params.encode()]
