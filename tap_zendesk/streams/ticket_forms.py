from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms

class TicketFormsStream(ZendeskCursorStream):
    name = 'ticket_forms'
    path = '/api/v2/ticket_forms'
    records_jsonpath = '$.ticket_forms[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('active', BooleanType, description="If the form is set as active"),
        Property('agent_conditions', ArrayType(ObjectType()), description="Array of condition sets for agent workspaces"),
        Property('created_at', DateTimeType, description="The time the ticket form was created"),
        Property('default', BooleanType, description="Is the form the default form for this account"),
        Property('deleted_at', DateTimeType, description="The time the ticket form was deleted"),
        Property('display_name', StringType, description="The name of the form that is displayed to an end user"),
        Property('end_user_conditions', ArrayType(ObjectType()), description="Array of condition sets for end user products"),
        Property('end_user_visible', BooleanType, description="Is the form visible to the end user"),
        Property('id', IntegerType, required=True, description="Automatically assigned when creating ticket form"),
        Property('in_all_brands', BooleanType, description="Is the form available for use in all brands on this account"),
        Property('name', StringType, description="The name of the form"),
        Property('position', IntegerType, description="The position of this form among other forms in the account, i.e. dropdown"),
        Property('raw_display_name', StringType, description="The dynamic content placeholder, if present, or the \"display_name\" value, if not. See Dynamic Content Items"),
        Property('raw_name', StringType, description="The dynamic content placeholder, if present, or the \"name\" value, if not. See Dynamic Content Items"),
        Property('restricted_brand_ids', ArrayType(IntegerType), description="IDs of all brands that this ticket form is restricted to"),
        Property('ticket_field_ids', ArrayType(IntegerType), description="IDs of all ticket fields which are in this ticket form. The products use the order of the IDs to show the field values in the tickets"),
        Property('updated_at', DateTimeType, description="The time of the last update of the ticket form"),
        Property('url', StringType, description="URL of the ticket form"),
    ).to_dict()
