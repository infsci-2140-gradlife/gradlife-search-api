class GLQuery:
    def constructor(self):
        self._page_num = 1
        self._page_size = 20
        
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
        return self.page_size