import urllib.request
import urllib.parse
import zlib
import json


class HttpClient:
    URL_BASE = "https://api.stackexchange.com/2.2"

    @classmethod
    def get(cls, entity, ids=[], submethod=None, params={}):
        ids_string = urllib.parse.quote_plus(cls._ids(ids))
        identification = '/'.join([cls.URL_BASE, entity, ids_string])
        query = '&'.join([cls._params(params), "site=stackoverflow"])

        if submethod is not None:
            identification = '/'.join([identification, submethod])

        url = '?'.join([identification, query])

        body = urllib.request.urlopen(url).read()
        content_json = zlib.decompress(body, 16+zlib.MAX_WBITS)
        content = json.loads(content_json)

        return content

    def _ids(ids):
        return ';'.join(str(_id) for _id in ids)

    def _params(params_dict):
        elements = \
            list(f"{key}={value}" for key, value in params_dict.items())

        return '&'.join(str(element) for element in elements)
