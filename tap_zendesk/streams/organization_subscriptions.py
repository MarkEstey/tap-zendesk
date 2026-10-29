from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_subscriptions

class OrganizationSubscriptionsStream(ZendeskCursorStream):
    name = 'organization_subscriptions'
    path = '/api/v2/organization_subscriptions'
    records_jsonpath = '$.organization_subscriptions[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="The date the organization subscription was created"),
        Property('id', IntegerType, required=True, description="The ID of the organization subscription"),
        Property('organization_id', IntegerType, description="The ID of the organization"),
        Property('user_id', IntegerType, description="The ID of the user"),
    ).to_dict()
