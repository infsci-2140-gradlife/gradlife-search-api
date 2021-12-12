from flask_restful import Resource
from models.gl_query import GLQuery
from models.gl_event import GLEvent
from services.search_service import SearchService

class GLEventResource(Resource):
    def constructor(self):
        self._search_service = SearchService()

    def get(self, id: int):
        return None

    def post(self, query: GLQuery) -> list[GLEvent]:
        return self._search_service.search(query)