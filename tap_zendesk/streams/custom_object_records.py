from tap_zendesk.client import ZendeskIncrementalCursorStream
from tap_zendesk.streams.custom_objects import CustomObjectsStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_object_records/

class CustomObjectRecordsStream(ZendeskIncrementalCursorStream):
    name = 'custom_object_records'
    path = '/api/v2/incremental/custom_objects/{custom_object_key}/cursor'
    records_jsonpath = '$.custom_object_records[*]'
    parent_stream_type = CustomObjectsStream
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="The time the object was created"),
        Property('created_by_user_id', StringType, description="Id of a user who created the object"),
        Property('custom_object_fields', ObjectType(additional_properties=True)),
        Property('custom_object_key', StringType, description="A user-defined unique identifier"),
        Property('external_id', StringType, description="An id you can use to link custom object records to external data"),
        Property('id', StringType, required=True, description="Automatically assigned upon creation"),
        Property('name', StringType, description="User-defined display name for the object. If autonumbering is selected for the custom object's name field, the name isn't allowed because it's automatically generated. If uniqueness is enabled, the name must be unique."),
        Property('photo', ObjectType(additional_properties=True), description="The record photo represented as an Attachment. The allows_photos property must be set to true for the object. Record photos are publicly accessible via the photo content_url."),
        Property('updated_at', DateTimeType, description="The time of the last update of the object"),
        Property('updated_by_user_id', StringType, description="Id of the last user who updated the object"),
        Property('url', StringType, description="Direct link to the specific custom object"),
    ).to_dict()
