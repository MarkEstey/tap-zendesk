from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_memberships

class OrganizationFieldsStream(ZendeskCursorStream):
    name = 'organization_fields'
    path = '/api/v2/organization_fields'
    records_jsonpath = '$.organization_fields[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('active', BooleanType, description="If true, this field is available for use"),
        Property('created_at', DateTimeType, description="The time the field was created"),
        Property('custom_field_options', ArrayType(ObjectType()), description="Required and presented for a custom field of type \"dropdown\". Each option is represented by an object with a name and value property"),
        Property('description', StringType, description="User-defined description of this field's purpose"),
        Property('id', IntegerType, required=True, description="Automatically assigned upon creation"),
        Property('key', StringType, description="A unique key that identifies this custom field. This is used for updating the field and referencing in placeholders. The key must consist of only letters, numbers, and underscores. It can't be only numbers"),
        Property('position', IntegerType, description="Ordering of the field relative to other fields"),
        Property('raw_description', StringType, description="The dynamic content placeholder, if present, or the description value, if not. See Dynamic Content Items"),
        Property('raw_title', StringType, description="The dynamic content placeholder, if present, or the title value, if not. See Dynamic Content Items"),
        Property('regexp_for_validation', StringType, description="Regular expression field only. The validation pattern for a field value to be deemed valid"),
        Property('relationship_filter', ObjectType(), description="A filter definition that allows your autocomplete to filter down results"),
        Property('relationship_target_type', StringType, description="A representation of what type of object the field references. Options are \"zen:user\", \"zen:organization\", \"zen:ticket\", and \"zen:custom_object:{key}\" where key is a custom object key. For example \"zen:custom_object:apartment\"."),
        Property('system', BooleanType, description="If true, only active and position values of this field can be changed"),
        Property('tag', StringType, description="Optional for custom field of type \"checkbox\"; not presented otherwise."),
        Property('title', StringType, description="The title of the custom field"),
        Property('type', StringType, description="The custom field type: \"checkbox\", \"currency\", \"date\", \"decimal\", \"dropdown\", \"integer\", \"lookup\", \"multiselect\", \"parent\" (custom objects only), \"regexp\", \"text\", or \"textarea\""),
        Property('updated_at', DateTimeType, description="The time of the last update of the field"),
        Property('url', StringType, description="The URL for this resource"),
    ).to_dict()
