from datetime import datetime
import json
from flask import jsonify, request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from models.gl_query import GLQuery
from models.gl_event import GLEvent
from services.search_service import SearchService

class GLEventResource(Resource):
    def __init__(self, search_service: SearchService):
        self._search_service = search_service

    def get(self, id: int):
        return None

    def post(self) -> list[GLEvent]:
        parser = RequestParser()
        parser.add_argument('query', help='The query, which can have text, startDate, endDate, and location properties', required=True)
        parser.add_argument('pageNum', type=int)
        parser.add_argument('pageSize', type=int)
        # still calling this to throw errors if necessary
        parsed_argsargs = parser.parse_args()
        
        # using parse_args made nested JSON weird
        args = request.get_json()

        query = GLQuery(
            page_num=0 if 'pageNum' not in args else args['pageNum'], 
            page_size=10 if 'pageSize' not in args else args['pageSize'],
            text=args['query']['text'], 
            location=None if 'location' not in args['query'] else args['query']['location'],
            startDate=None if 'location' not in args['query'] else args['query']['startDate'],
            endDate=None if 'endDate' not in args['query'] else args['query']['endDate']
        )

        return jsonify(self._search_service.search(query))