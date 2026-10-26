from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships

class GroupMembershipsStream(ZendeskCursorStream):
    name = 'group_memberships'
    path = '/api/v2/group_memberships'
    records_jsonpath = '$.group_memberships[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="The time the group was created"),
        Property('default', BooleanType, description="If true, tickets assigned directly to the agent will assume this membership's group"),
        Property('group_id', IntegerType, description="The id of a group"),
        Property('id', IntegerType, required=True, description="Automatically assigned upon creation"),
        Property('updated_at', DateTimeType, description="The time of the last update of the group"),
        Property('url', StringType, description="The API url of this record"),
        Property('user_id', IntegerType, description="The id of an agent"),
    ).to_dict()
