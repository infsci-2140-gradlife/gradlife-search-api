import os
from models.gl_query import GLQuery
from whoosh import index, query
from whoosh.qparser import QueryParser
from whoosh.query import Query

class SearchService:
    def __init__(self):
        index_path = os.path.join(os.getcwd(), 'data', 'index')

        # hacky stuff because i don't have time to figure out how real environment vars and dotenv interact
        if 'PROD' in os.environ and os.environ['PROD'] == 'TRUE':
            index_path = os.path.join('..', 'data', 'index')

        self._index = index.open_dir(index_path)
    
    def get_lexicon(self, field_name: str) -> list[str]:
        with self._index.searcher() as searcher:
            return searcher.lexicon('location')
 
    def search(self, gl_query: GLQuery):
        with self._index.searcher() as searcher:
            # text query
            query_parser = QueryParser('doc_content', schema=self._index.schema)
            parsed_query:Query = query_parser.parse(gl_query.text)

            # date query
            date_query: Query = None
            if gl_query.start_date is not None or gl_query.end_date is not None:
                date_query = query.DateRange('date', gl_query.start_date, gl_query.end_date)

            # note that the page number is 0-indexed
            results = searcher.search_page(parsed_query, pagenum=gl_query.page_num + 1, pagelen=gl_query.page_size, filter=date_query)
            
            return {
                'resultCount': results.total,
                'pageCount': results.pagecount,
                'pageSize': results.pagelen,
                'results': [dict(hit) for hit in results.results[results.offset:]]
            }