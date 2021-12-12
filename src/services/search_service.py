import os
from models.gl_query import GLQuery
from whoosh import index
from whoosh.qparser import QueryParser

class SearchService:
    def constructor(self):
        index_path = os.path.join(os.getcwd(), 'data')
        print('loading index from', index_path)
        self._index = index.open_dir(index_path)
 
    def search(self, query: GLQuery):
        with self._index.searcher() as searcher:
            query_parser = QueryParser('content', schema=self._index.schema)
            print('parsed query', query_parser.parse(query.text))
            results = searcher.search_page(query_parser.parse(query.text), query.page_num, pagelen=query.page_size)
            return results