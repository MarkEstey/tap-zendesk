from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/groups/groups

class GroupsStream(ZendeskCursorStream):
    name = 'groups'
    path = '/api/v2/groups'
    records_jsonpath = '$.groups[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="The time the group was created"),
        Property('default', BooleanType, description="If the group is the default one for the account"),
        Property('deleted', BooleanType, description="Deleted groups get marked as such"),
        Property('description', StringType, description="The description of the group"),
        Property('id', IntegerType, required=True, description="Automatically assigned when creating groups"),
        Property('is_public', BooleanType, description="If true, the group is public. If false, the group is private. You can't change a private group to a public group"),
        Property('name', StringType, description="The name of the group"),
        Property('updated_at', DateTimeType, description="The time of the last update of the group"),
        Property('url', StringType, description="The API url of the group"),
    ).to_dict()
