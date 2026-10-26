from tap_zendesk.client import ZendeskStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/sharing_agreements

class SharingAgreementsStream(ZendeskStream):
    name = 'sharing_agreements'
    path = '/api/v2/sharing_agreements'
    records_jsonpath = '$.sharing_agreements[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="The time the record was created"),
        Property('id', IntegerType, required=True, description="Automatically assigned upon creation"),
        Property('name', StringType, description="Name of this sharing agreement"),
        Property('partner_name', StringType, description="Can be one of the following: \"jira\", null"),
        Property('remote_subdomain', StringType, description="Subdomain of the remote account or null if not associated with an account"),
        Property('status', StringType, description="Can be one of the following: \"accepted\", \"declined\", \"pending\", \"inactive\", \"failed\", \"ssl_error\", \"configuration_error\""),
        Property('type', StringType, description="Can be one of the following: \"inbound\", \"outbound\""),
        Property('updated_at', DateTimeType, description="The time the record was updated"),
        Property('url', StringType, description="URL of the sharing agreement record"),
    ).to_dict()
