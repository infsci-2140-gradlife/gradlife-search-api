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
        parser.add_argument('query', help='The query, which can have text, startDate, endDate, and location properties', required=True)
        parser.add_argument('pageNum', type=int)
        parser.add_argument('pageSize', type=int)
        
        args = parser.parse_args()
        args.pageNum = 0 if 'pageNum' not in args.__dict__ else args.pageNum
        args.pageSize = 10 if 'pageSize' not in args.__dict__ else args.pageSize

        print('args', args)

        query = GLQuery(
            text=args.query, 
            page_num=args.pageNum, 
            page_size=args.pageSize,
            location=None if 'location' not in args.query else args.query['location'],
            startDate=None if 'location' not in args.query else args.query['startDate'],
            endDate=None if 'endDate' not in args.query else args.query['endDate']
        )

        return jsonify(self._search_service.search(query))