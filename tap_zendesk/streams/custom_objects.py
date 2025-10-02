from tap_zendesk.client import ZendeskStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_objects

class CustomObjectsStream(ZendeskStream):
    name = 'custom_objects'
    path = '/api/v2/custom_objects'
    records_jsonpath = '$.custom_objects[*]'
    primary_keys = ['key']
    #replication_key = 'updated_at'

    schema = PropertiesList(
        Property('allows_photos', BooleanType, description="If true, photos can be uploaded to the records of the object. If false, new photos cannot be uploaded but existing photos can still be viewed and removed"),
        Property('created_at', StringType, description="The time the object type was created"),
        Property('created_by_user_id', StringType, description="Id of a user who created the object"),
        Property('description', StringType, description="User-defined description of the object"),
        Property('include_in_list_view', BooleanType, description="A flag setting the visibility of the object in the agent's list view. If true, all agents and admins have viewing access to the object in the Custom objects record page in the Agent Workspace. If false, only admins have viewing access"),
        Property('key', StringType, required=True, description="A user-defined unique identifier. Writable on create only"),
        Property('raw_description', StringType, description="The dynamic content placeholder, if present, or the \"raw_description\" value, if not. See Dynamic Content Items"),
        Property('raw_title', StringType, description="The dynamic content placeholder, if present, or the \"title\" value, if not. See Dynamic Content Items"),
        Property('raw_title_pluralized', StringType, description="The dynamic content placeholder, if present, or the \"raw_title_pluralized\" value, if not. See Dynamic Content Items"),
        Property('title', StringType, description="User-defined display name for the object"),
        Property('title_pluralized', StringType, description="User-defined pluralized version of the object's title"),
        Property('updated_at', StringType, description="The time of the last update of the object"),
        Property('updated_by_user_id', StringType, description="Id of the last user who updated the object"),
        Property('url', StringType, description="Direct link to the specific custom object"),
    ).to_dict()

    def get_child_context(self, record, context):
        return {'custom_object_key': record['key']}

    # Temporary workaround, need to implement offset pagination
    def get_url_params(self, context, next_page_token):
        return {}
