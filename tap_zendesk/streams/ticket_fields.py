from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields

class TicketFieldsStream(ZendeskCursorStream):
    name = 'ticket_fields'
    path = '/api/v2/ticket_fields'
    records_jsonpath = '$.ticket_fields[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('active', BooleanType, description="Whether this field is available"),
        Property('active_forms_count', IntegerType, description="The number of active ticket forms using this field. Only present when the active_forms_count query parameter is passed"),
        Property('agent_can_edit', BooleanType, description="Whether this field is editable by agents"),
        Property('agent_description', StringType, description="A description of the ticket field that only agents can see"),
        Property('collapsed_for_agents', BooleanType, description="If true, the field is shown to agents by default. If false, the field is hidden alongside infrequently used fields. Classic interface only"),
        Property('created_at', DateTimeType, description="The time the custom ticket field was created"),
        Property('creator_app_name', StringType, description="Name of the app that created the ticket field, or a null value if no app created the ticket field"),
        Property('creator_user_id', IntegerType, description="The id of the user that created the ticket field, or a value of \"-1\" if an app created the ticket field"),
        Property('custom_field_options', ArrayType(ObjectType()), description="Required and presented for a custom ticket field of type \"multiselect\" or \"tagger\""),
        Property('custom_statuses', ArrayType(ObjectType()), description="List of customized ticket statuses. Only present for a system ticket field of type \"custom_status\""),
        Property('description', StringType, description="Describes the purpose of the ticket field to users"),
        Property('editable_in_portal', BooleanType, description="Whether this field is editable by end users in Help Center"),
        Property('id', IntegerType, required=True, description="Automatically assigned when created"),
        Property('key', StringType, description="A unique key that identifies the ticket field. System-managed fields use a standard:: prefix."),
        Property('max_selections', IntegerType, description="Present for multi_lookup fields only. The maximum number of target records the field accepts. Defaults to 20"),
        Property('position', IntegerType, description="The relative position of the ticket field on a ticket. Note that for accounts with ticket forms, positions are controlled by the different forms"),
        Property('raw_description', StringType, description="The dynamic content placeholder if present, or the description value if not. See Dynamic Content"),
        Property('raw_title', StringType, description="The dynamic content placeholder if present, or the title value if not. See Dynamic Content"),
        Property('raw_title_in_portal', StringType, description="The dynamic content placeholder if present, or the \"title_in_portal\" value if not. See Dynamic Content"),
        Property('regexp_for_validation', StringType, description="For \"regexp\" fields only. The validation pattern for a field value to be deemed valid"),
        Property('relationship_filter', ObjectType(), description="A filter definition that allows your autocomplete to filter down results"),
        Property('relationship_target_type', StringType, description="Present for \"lookup\" and \"multi_lookup\" fields. A representation of what type of object the field references. Options are \"zen:user\", \"zen:organization\", \"zen:ticket\", or \"zen:custom_object:{key}\", where key is a custom object key. For example, \"zen:custom_object:apartment\"."),
        Property('removable', BooleanType, description="If false, this field is a system field that must be present on all tickets"),
        Property('required', BooleanType, description="If true, agents must enter a value in the field to change the ticket status to solved"),
        Property('required_in_portal', BooleanType, description="If true, end users must enter a value in the field to create the request"),
        Property('sub_type_id', IntegerType, description="For system ticket fields of type \"priority\" and \"status\". Defaults to 0. A \"priority\" sub type of 1 removes the \"Low\" and \"Urgent\" options. A \"status\" sub type of 1 adds the \"On-Hold\" option"),
        Property('system_field_options', ArrayType(ObjectType()), description="Presented for a system ticket field of type \"tickettype\", \"priority\" or \"status\""),
        Property('tag', StringType, description="For \"checkbox\" fields only. A tag added to tickets when the checkbox field is selected"),
        Property('title', StringType, description="The title of the ticket field"),
        Property('title_in_portal', StringType, description="The title of the ticket field for end users in Help Center"),
        Property('type', StringType, description="System or custom field type. Editable for custom field types and only on creation. See Create Ticket Field"),
        Property('updated_at', DateTimeType, description="The time the custom ticket field was last updated"),
        Property('url', StringType, description="The URL for this resource"),
        Property('visible_in_portal', BooleanType, description="Whether this field is visible to end users in Help Center"),
    ).to_dict()
