import time
from datetime import datetime
from requests.auth import HTTPBasicAuth

from singer_sdk.authenticators import OAuthAuthenticator
from singer_sdk.helpers._typing import TypeConformanceLevel
from singer_sdk.pagination import BaseAPIPaginator, BasePageNumberPaginator
from singer_sdk.streams import RESTStream

# Base API documentation: https://developer.zendesk.com/api-reference

class ZendeskOAuthAuthenticator(OAuthAuthenticator):
    @property
    def oauth_request_body(self):
        return {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': '',
            'scope': 'read',
        }

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
        if self.config['api_token']:
            return HTTPBasicAuth(username=self.config['email'] + '/token', password=self.config['api_token'])
        elif self.config['client_id']:
            return ZendeskOAuthAuthenticator(client_id=self.config['client_id'], client_secret=self.config['client_secret'])

class ZendeskCursorPaginator(BaseAPIPaginator):
    def __init__(self):
        super().__init__(start_value=None)

    def get_next(self, response):
        return response.json()['meta']['after_cursor']

    def has_more(self, response):
        return response.json()['meta']['has_more']

class ZendeskCursorStream(ZendeskStream):
    def get_new_paginator(self):
        return ZendeskCursorPaginator()

    def get_url_params(self, context, next_page_token):
        if next_page_token:
            return {'page[size]': 100, 'page[after]': next_page_token}
        else:
            return {'page[size]': 100}

class ZendeskOffsetPaginator(BasePageNumberPaginator):
    def __init__(self):
        super().__init__(start_value=1)

    def has_more(self, response):
        return response.json().get('next_page') is not None

class ZendeskOffsetStream(ZendeskStream):
    def get_new_paginator(self):
        return ZendeskOffsetPaginator()

    def get_url_params(self, context, next_page_token):
        return {
            'page_size': 100,
            'page': next_page_token,
        }

class ZendeskIncrementalTimePaginator(BaseAPIPaginator):
    def __init__(self):
        super().__init__(start_value=None)

    def get_next(self, response):
        return response.json()['end_time']

    def has_more(self, response):
        return not response.json()['end_of_stream']

class ZendeskIncrementalTimeStream(ZendeskStream):
    def get_new_paginator(self):
        return ZendeskIncrementalTimePaginator()

    def get_url_params(self, context, next_page_token):
        if next_page_token is not None:
            return {'start_time': next_page_token }

        if type(self.get_starting_replication_key_value(context)) == int:
            return {'start_time': self.get_starting_replication_key_value(context) }

        if type(self.get_starting_replication_key_value(context)) == str:
            timestamp = int(datetime.fromisoformat(self.get_starting_replication_key_value(context)).timestamp())
            return {'start_time': timestamp }

        else:
            return {'start_time': 0 }

    def parse_response(self, response):
        limit = 60 / self.config['incremental_request_rate']
        delay = limit - response.elapsed.total_seconds()
        if delay > 0:
            time.sleep(limit - response.elapsed.total_seconds())

        return super().parse_response(response)

class ZendeskIncrementalCursorPaginator(BaseAPIPaginator):
    def __init__(self):
        super().__init__(start_value=None)

    def get_next(self, response):
        return response.json()['after_cursor']

    def has_more(self, response):
        response = response.json()

        if 'end_of_stream' in response:
            return not response['end_of_stream']

        if 'meta' in response:
            return response['meta']['has_more']

        return False

class ZendeskIncrementalCursorStream(ZendeskStream):
    def get_new_paginator(self):
        return ZendeskIncrementalCursorPaginator()

    def get_url_params(self, context, next_page_token):
        if next_page_token is not None:
            return {'cursor': next_page_token}

        else:
            return {'start_time': int(self.get_starting_timestamp(context).timestamp())}

    def parse_response(self, response):
        limit = 60 / self.config['incremental_request_rate']
        delay = limit - response.elapsed.total_seconds()
        if delay > 0:
            time.sleep(limit - response.elapsed.total_seconds())

        return super().parse_response(response)
