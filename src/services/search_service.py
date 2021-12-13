import os
from models.gl_query import GLQuery
from whoosh import index
from whoosh.qparser import QueryParser

class SearchService:
    def __init__(self):
        index_path = os.path.join(os.getcwd(), 'data', 'index')

        # hacky stuff because i don't have time to figure out how real environment vars and dotenv interact
        if 'PROD' in os.environ and os.environ['PROD'] == 'TRUE':
            index_path = os.path.join('..', 'data', 'index')

        self._index = index.open_dir(index_path)
 
    def search(self, query: GLQuery):
        with self._index.searcher() as searcher:
            query_parser = QueryParser('doc_content', schema=self._index.schema)
            print('parsed query', query_parser.parse(query.text))
            
            # note that the page number is 0-indexed
            results = searcher.search_page(query_parser.parse(query.text), query.page_num + 1, pagelen=query.page_size)
            return {
                'resultCount': results.total,
                'pageCount': results.pagecount,
                'pageSize': results.pagelen,
                'results': [dict(hit) for hit in results.results]
            }