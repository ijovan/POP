from source.page import Page


class PageIterator:
    STARTING_PAGE_NUMBER = 1

    def __init__(self, url, max_depth):
        self._page_number = self.STARTING_PAGE_NUMBER
        self._has_more = True
        self._max_depth = max_depth
        self.url = url

    def next_page(self):
        page = Page(self.url, self._page_number)
        page.get()

        if page.error:
            page.print_error()
            print(f"Error URL {self.url}")

        self._page_number += 1
        self._has_more = page.has_more

        return page

    def has_next_page(self):
        return self._page_number <= self._max_depth and self._has_more
