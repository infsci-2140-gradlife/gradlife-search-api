class GLQuery:
    def __init__(self, **kwargs):
        self._page_num = 1 if 'page_num' not in kwargs else kwargs ['page_num']
        self._page_size = 20 if 'page_size' not in kwargs else kwargs['page_size']
        self._text = kwargs['text']
        self._location = kwargs['location']
        self._start_date = kwargs['startDate']
        self._end_date = kwargs['endDate']
        
    @property
    def text(self):
        return self._text

    @property
    def start_date(self):
        return self._start_date
    
    @property
    def end_date(self):
        return self._end_date

    @property
    def location(self):
        return self._location

    @property
    def page_num(self):
        return self._page_num

    @property
    def page_size(self):
        return self._page_size