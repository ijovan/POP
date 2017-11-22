from src.main.python.page import Page
import urllib.parse


class Request:
    DEFAULT_MAX_DEPTH    = 100
    PAGE_SIZE            = 100
    STARTING_PAGE_NUMBER = 1
    SITE                 = "stackoverflow"
    URL_BASE             = "https://api.stackexchange.com/2.2"

    KEY          = open('.key').read().strip()
    ACCESS_TOKEN = open('.access_token').read().strip()

    def __init__(self, args):
        self.entity       = args.pop('entity')
        self.ids          = args.pop('ids', [])
        self.submethod    = args.pop('submethod', None)
        self.max_depth    = args.pop('max_depth', self.DEFAULT_MAX_DEPTH)
        self.query_params = args.pop('query_params', {})
        self._page_number = self.STARTING_PAGE_NUMBER
        self._has_more    = True
        self._items       = []

        self.url = self._url()

    def items(self):
        if not self._items: self.get()

        return self._items.copy()

    def get(self):
        while self._has_next_page():
            self._items += self._next_page()

    def _next_page(self):
        page = Page(self.url, self._page_number)
        page.get()

        self._print_current(page)

        self._page_number += 1
        self._has_more     = page.has_more

        return page.items

    def _has_next_page(self):
        return self._page_number <= self.max_depth and self._has_more

    def _url(self):
        endpoint = '/'.join(filter(None, [
            self.URL_BASE, self.entity, self._ids(), self.submethod
        ]))

        return '?'.join([endpoint, self._query_params()])

    def _ids(self):
        raw_ids = ';'.join(str(_id) for _id in self.ids)

        return urllib.parse.quote_plus(raw_ids)

    def _query_params(self):
        query_params = self.query_params.copy()
        query_params.update({
            'site':         self.SITE,
            'key':          self.KEY,
            'access_token': self.ACCESS_TOKEN,
            'pagesize':     self.PAGE_SIZE
        })

        elements = [f"{key}={value}" for key, value in query_params.items()]

        return '&'.join(elements)

    def _print_current(self, page):
        ids_marker = '{ids}' if self.ids else None

        location = '/'.join(filter(None,
            ['', self.entity, ids_marker, self.submethod]
        ))

        message = f"Location: {location}; page number: {self._page_number}"

        if page.quota_remaining:
            message += f"; quota remaining: {page.quota_remaining}"

        print(message)
