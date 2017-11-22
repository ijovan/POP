import urllib.request
import urllib.error
import zlib
import json


class Page:
    def __init__(self, url, page_number):
        self.url             = url + f"&page={str(page_number)}"
        self.items           = []
        self.has_more        = False
        self.quota_remaining = None
        self.error           = None

    def get(self):
        try:
            body = urllib.request.urlopen(self.url).read()

            content = json.loads(Page._decompress(body))

            self.items           = content['items']
            self.has_more        = content['has_more']
            self.quota_remaining = content['quota_remaining']
        except urllib.error.HTTPError as error:
            self.error = error

            self.print_error()

    def print_error(self):
        try:
            message = Page._decompress(self.error.read())
        except:
            message = "Error message decompression failed."

        print(f"Error encountered:\n{message}")

    @staticmethod
    def _decompress(text):
        return zlib.decompress(text, 16+zlib.MAX_WBITS)