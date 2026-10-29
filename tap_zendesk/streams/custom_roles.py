from tap_zendesk.client import ZendeskStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/account-configuration/custom_roles

class CustomRolesStream(ZendeskStream):
    name = 'custom_roles'
    path = '/api/v2/custom_roles'
    records_jsonpath = '$.custom_roles[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('configuration', ObjectType(), description="Configuration settings for the role. See Configuration"),
        Property('created_at', StringType, description="The time the record was created"),
        Property('description', StringType, description="A description of the role"),
        Property('id', IntegerType, required=True, description="Automatically assigned on creation"),
        Property('name', StringType, description="Name of the custom role"),
        Property('role_type', IntegerType, description="The user's role. 0 stands for a custom agent, 1 for a light agent, 2 for a chat agent, 3 for a contributor, 4 for an admin and 5 for a billing admin. See Understanding standard agent roles in Zendesk Support in Zendesk help"),
        Property('team_member_count', IntegerType, description="The number of team members assigned to this role"),
        Property('updated_at', DateTimeType, description="The time the record was last updated"),
    ).to_dict()
