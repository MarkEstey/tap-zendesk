from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_skips

class TicketSkipsStream(ZendeskCursorStream):
    name = 'ticket_skips'
    path = '/api/v2/skips'
    records_jsonpath = '$.skips[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="Time the skip was created"),
        Property('id', IntegerType, required=True, description="Automatically assigned upon creation"),
        Property('reason', StringType, description="Reason for skipping the ticket"),
        Property('ticket', ObjectType(), description="The skipped ticket. See the Ticket object reference"),
        Property('ticket_id', IntegerType, description="ID of the skipped ticket"),
        Property('updated_at', DateTimeType, description="Time the skip was last updated"),
        Property('user_id', IntegerType, description="ID of the skipping agent"),
    ).to_dict()
