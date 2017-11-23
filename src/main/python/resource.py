from src.main.python.url import URL
from src.main.python.page_iterator import PageIterator


class Resource:
    DEFAULT_MAX_DEPTH = 100

    def __init__(self, args):
        self.url = URL({
            'entity': args.pop('entity'),
            'ids': args.pop('ids', []),
            'submethod': args.pop('submethod', None),
            'query_params': args.pop('query_params', {})
        })

        self.max_depth = args.pop('max_depth', self.DEFAULT_MAX_DEPTH)
        self._items = []

    def items(self):
        if not self._items:
            self.get()

        return self._items.copy()

    def get(self):
        self._items = []

        page_iterator = PageIterator(self.url.string, self.max_depth)

        while page_iterator.has_next_page():
            page = page_iterator.next_page()

            if not page.error:
                self._print_current(page)

            self._items += page.items

    def _print_current(self, page):
        print(
            f"Location: {self.url.endpoint_format()}; "
            + f"page number: {page.page_number}; "
            + f"quota remaining: {page.quota_remaining}"
        )
