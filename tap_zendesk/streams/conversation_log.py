from tap_zendesk.client import ZendeskCursorStream
from tap_zendesk.streams.tickets import TicketsStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/conversation_log

class ConversationLogStream(ZendeskCursorStream):
    name = 'conversation_log'
    path = '/api/v2/tickets/{ticket_id}/conversation_log'
    records_jsonpath = '$.events[*]'
    primary_keys = ['id']
    parent_stream_type = TicketsStream

    schema = PropertiesList(
        Property('attachments', ArrayType(ObjectType()), description="A collection of attachments (image or file) associated with the event"),
        Property('author', ObjectType(), description="Object that describes the user who created the event"),
        Property('content', ObjectType(), description="Object that describes the content of the message. The inner fields depends on the record type"),
        Property('created_at', DateTimeType, description="The timestamp of when this record was created"),
        Property('id', StringType, description="Unique record identifier"),
        Property('metadata', ObjectType(), description="Various additional data that further describes this record"),
        Property('reference', StringType, description="A Zendesk resource name value that uniquely identifies this record. Example: zen:ticket_event:<id>"),
        Property('type', StringType, description="The type of record, representing one of the conversational ticket events. Examples: Comment or Messaging::ConversationMessage"),
    ).to_dict()
