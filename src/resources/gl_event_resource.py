from datetime import datetime
import json
from flask import jsonify
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
        parser.add_argument('text', type=str, help='The text of the search query', required=True)
        parser.add_argument('startDate', type=datetime, help='The start date for events to be returned by the query')
        parser.add_argument('endDate', type=datetime, help='The end date for events to be returned by the query')
        parser.add_argument('location', type=str, help='The location for events to be returned by the query')
        parser.add_argument('pageNum', type=int)
        parser.add_argument('pageSize', type=int)
        args = parser.parse_args()
        query = GLQuery(text=args.query, page_num=args.pageNum, page_size=args.pageSize)

        return jsonify(self._search_service.search(query))