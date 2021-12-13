import os
from models.gl_query import GLQuery
from whoosh import index
from whoosh.qparser import QueryParser

class SearchService:
    def __init__(self):
        index_path = os.path.join(os.getcwd(), 'data', 'index')

        if os.environ['PROD'] == 'TRUE':
            print('loading index for prod', os.getcwd())
            index_path = os.path.join('..', 'data', 'index')

        self._index = index.open_dir(index_path)
 
    def search(self, query: GLQuery):
        with self._index.searcher() as searcher:
            query_parser = QueryParser('doc_content', schema=self._index.schema)
            print('parsed query', query_parser.parse(query.text))
            results = searcher.search_page(query_parser.parse(query.text), query.page_num, pagelen=query.page_size)
            return {
                'resultCount': results.total,
                'pageCount': results.pagecount,
                'pageSize': results.pagelen,
                'results': [dict(hit) for hit in results.results]
            }