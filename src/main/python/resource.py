from src.main.python.page_iterator import PageIterator
from src.main.python.credentials import Credentials
import urllib.parse


class Resource:
    DEFAULT_MAX_DEPTH = 100
    PAGE_SIZE = 100
    SITE = "stackoverflow"
    URL_BASE = "https://api.stackexchange.com/2.2"

    KEY = Credentials.key()
    ACCESS_TOKEN = Credentials.access_token()

    def __init__(self, args):
        self.entity = args.pop('entity')
        self.ids = args.pop('ids', [])
        self.submethod = args.pop('submethod', None)
        self.max_depth = args.pop('max_depth', self.DEFAULT_MAX_DEPTH)
        self.query_params = args.pop('query_params', {})
        self._items = []

        self.url = self._url()

    def items(self):
        if not self._items:
            self.get()

        return self._items.copy()

    def get(self):
        self._items = []

        page_iterator = PageIterator(self._url(), self.max_depth)

        while page_iterator.has_next_page():
            page = page_iterator.next_page()

            if not page.error:
                self._print_current(page)

            self._items += page.items

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
            'site': self.SITE,
            'key': self.KEY,
            'access_token': self.ACCESS_TOKEN,
            'pagesize': self.PAGE_SIZE
        })

        elements = [f"{key}={value}" for key, value in query_params.items()]

        return '&'.join(elements)

    def _print_current(self, page):
        ids_marker = '{ids}' if self.ids else None

        location = '/'.join(filter(None,
            ['', self.entity, ids_marker, self.submethod]
        ))

        print(
            f"Location: {location}; "
            + f"page number: {page.page_number}; "
            + f"quota remaining: {page.quota_remaining}"
        )
