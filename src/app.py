from flask import Flask
from flask_restful import Api
from resources.gl_event_resource import GLEventResource
from resources.hello_world import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(GLEventResource, '/event')

if __name__ == '__main__':
    app.run(debug=True)