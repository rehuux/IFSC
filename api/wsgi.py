from index import app
from vercel_wsgi import handle_wsgi

def handler(request, context):
    return handle_wsgi(app, request, context)
