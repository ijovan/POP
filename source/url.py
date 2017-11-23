from source.credentials import Credentials
import urllib.parse


class URL:
    URL_BASE = "https://api.stackexchange.com/2.2"
    SITE = "stackoverflow"
    PAGE_SIZE = 100

    def __init__(self, args):
        self.entity = args.pop('entity')
        self.ids = args.pop('ids', [])
        self.submethod = args.pop('submethod', None)
        self.query_params = args.pop('query_params', {})
        self.string = self._string()

    def endpoint_format(self):
        ids_marker = '{ids}' if self.ids else None

        endpoint_format = '/'.join(filter(None, [
            '', self.entity, ids_marker, self.submethod
        ]))

        return endpoint_format

    def _string(self):
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
            'pagesize': self.PAGE_SIZE
        })

        if Credentials.valid():
            query_params.update({
                'key': Credentials.key(),
                'access_token': Credentials.access_token()
            })

        elements = [f"{key}={value}" for key, value in query_params.items()]

        return '&'.join(elements)
