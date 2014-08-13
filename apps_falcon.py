import falcon

class TestResource(object):
    def on_get(self, request, response):
        json_data = {"message": "Hello, World!"}
        response.body = json.dumps(json_data)  

app = falcon.API()
app.add_route('/json', TestResource())
