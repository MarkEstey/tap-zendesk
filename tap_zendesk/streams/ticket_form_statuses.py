from tap_zendesk.client import ZendeskStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_form_statuses

class TicketFormStatusesStream(ZendeskStream):
    name = 'ticket_form_statuses'
    path = '/api/v2/ticket_form_statuses'
    records_jsonpath = '$.ticket_form_statuses[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('custom_status_id', IntegerType, description="The id of the associated custom status"),
        Property('id', StringType, required=True, description="Automatically assigned when creating a ticket form"),
        Property('ticket_form_id', IntegerType, description="The id of the associated ticket form"),
    ).to_dict()
