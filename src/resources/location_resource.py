from flask_restful import Resource

from services.search_service import SearchService

class LocationResource(Resource):
    def __init__(self, search_service: SearchService):
        self._search_service = search_service

    def get(self):
        return self._search_service.get_lexicon('doc_location')
