import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.gl_event_resource import GLEventResource
from resources.hello_world import HelloWorld
from services.search_service import SearchService

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# services
search_service = SearchService()

api.add_resource(HelloWorld, '/')
api.add_resource(GLEventResource, '/event', resource_class_kwargs={'search_service': search_service})

if __name__ == '__main__':
    print('OS environ prod', os.environ['PROD'])
    debug = True if os.environ['PROD'] == 'TRUE' else False
    app.run(debug=debug, port=os.environ['PORT'] or 5000)