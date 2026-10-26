from tap_zendesk.client import ZendeskIncrementalTimeStream
from singer_sdk.typing import *

# Incremental Documentation: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-event-export

class TicketEventsStream(ZendeskIncrementalTimeStream):
    name = 'ticket_events'
    path = '/api/v2/incremental/ticket_events'
    records_jsonpath = '$.ticket_events[*]'
    primary_keys = ['id']
    replication_key = 'timestamp'

    schema = PropertiesList(
        Property('child_events', ArrayType(ObjectType())),
        Property('id', IntegerType, required=True),
        Property('ticket_id', IntegerType),
        Property('timestamp', IntegerType, required=True),
        Property('created_at', DateTimeType),
        Property('updater_id', IntegerType),
        Property('via', StringType),
        Property('system', ObjectType()),
        Property('metadata', ObjectType()),
        Property('event_type', StringType),
        Property('merged_ticket_ids', ArrayType(IntegerType)),
    ).to_dict()

    def get_url_params(self, *args, **kwargs):
        return super().get_url_params(*args, **kwargs) | {'include': 'comment_events'}
