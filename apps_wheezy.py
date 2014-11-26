from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory
import json

def welcome(request):
    response = HTTPResponse()
    response.write('Hello World!')
    return response

def json_view(request):
    response = HTTPResponse()
    json_data = {"message": "Hello, World!"}
    data = json.dumps(json_data)
    response.write(data)
    return response


all_urls = [
    url('', welcome, name='default'),
    url('json', json_view, name='json_view')
]


options = {}
app = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options=options
)
