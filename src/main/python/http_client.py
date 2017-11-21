import urllib.request
import urllib.parse
import zlib
import json


class HttpClient:
    URL_BASE = "https://api.stackexchange.com/2.2"
    KEY = open('.key').read().strip()
    ACCESS_TOKEN = open('.access_token').read().strip()

    @classmethod
    def get(cls, entity, ids=[], submethod=None,
            query_params={}, args={'depth': 100}):
        ids_string = urllib.parse.quote_plus(cls._ids(ids))
        identification = '/'.join([cls.URL_BASE, entity, ids_string])
        query = '&'.join([
            cls._query_params(query_params),
            "site=stackoverflow",
            f"key={cls.KEY}",
            f"access_token={cls.ACCESS_TOKEN}"
        ])

        if submethod is not None:
            identification = '/'.join([identification, submethod])

        url = '?'.join([identification, query])
        page_number = 1
        items = []

        while True:
            cls._log(entity, ids, submethod, page_number)

            page = cls.get_page(url, page_number)

            items += page['items']
            page_number += 1

            if page_number >= args['depth'] or not page['has_more']:
                break

        return items

    def get_page(url, page_number):
        body = urllib.request.urlopen(url + f"&page={str(page_number)}").read()

        content_json = zlib.decompress(body, 16+zlib.MAX_WBITS)
        content = json.loads(content_json)

        print(f"Quota remaining: {content['quota_remaining']}")

        return {'items': content['items'], 'has_more': content['has_more']}

    def _log(entity, ids, submethod, page_number):
        line = ['', entity]

        if ids: line.append('{ids}')
        if submethod: line.append(submethod)

        print(f"Request: {'/'.join(line)}; page: {page_number}")

    def _ids(ids):
        return ';'.join(str(_id) for _id in ids)

    def _query_params(query_params_dict):
        elements = \
            list(f"{key}={value}" for key, value in query_params_dict.items())

        return '&'.join(str(element) for element in elements)
