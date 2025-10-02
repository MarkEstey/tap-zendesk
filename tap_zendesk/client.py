from requests.auth import HTTPBasicAuth

from singer_sdk.helpers._typing import TypeConformanceLevel
from singer_sdk.pagination import BaseAPIPaginator
from singer_sdk.streams import RESTStream

# Base API documentation: https://developer.zendesk.com/api-reference

class ZendeskCursorPaginator(BaseAPIPaginator):
    def __init__(self):
        super().__init__(start_value=None)

    def get_next(self, response):
        meta = response.json().get('meta', {})
        return meta.get('after_cursor')

    def has_more(self, response):
        meta = response.json().get('meta', {})
        return meta.get('has_more', False)

class ZendeskStream(RESTStream):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.TYPE_CONFORMANCE_LEVEL = {
            'none': TypeConformanceLevel.NONE,
            'root_only': TypeConformanceLevel.ROOT_ONLY,
            'recursive': TypeConformanceLevel.RECURSIVE,
        }.get(self.config['stream_type_conformance'])

    @property
    def url_base(self):
        return self.config['url_base']

    @property
    def authenticator(self):
        return HTTPBasicAuth(username=self.config['email'] + '/token', password=self.config['api_token'])

    def get_new_paginator(self):
        return ZendeskCursorPaginator()

    def get_url_params(self, context, next_page_token):
        params = {'page[size]': 100}

        if next_page_token:
            params['page[after]'] = next_page_token

        return params
