import falcon
import json

class TestResource(object):
    def on_get(self, request, response):
        json_data = {"message": "Hello, World!"}
        response.body = json.dumps(json_data)  

class IndexResource(object):
    def on_get(self, request, response):
        response.body = 'Hello World!'

app = falcon.API()
app.add_route('/', IndexResource())
app.add_route('/json', TestResource())
