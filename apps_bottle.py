from bottle import Bottle, route, request, run, template, response
import json

app = Bottle()

@app.route("/json")
def hello():
    response.content_type = 'application/json'
    resp = {"message": "Hello, World!"}
    return json.dumps(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
