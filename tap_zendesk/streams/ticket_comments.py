from tap_zendesk.client import ZendeskCursorStream
from tap_zendesk.streams.tickets import TicketsStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments

class TicketCommentsStream(ZendeskCursorStream):
    name = 'ticket_comments'
    path = '/api/v2/tickets/{ticket_id}/comments'
    parent_stream_type = TicketsStream
    state_partitioning_keys = []
    records_jsonpath = '$.comments[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('attachments', ArrayType(ObjectType()), description="Attachments, if any. See Attachment"),
        Property('audit_id', IntegerType, description="The id of the ticket audit record. See Show Audit"),
        Property('author_id', IntegerType, description="The id of the comment author. If null or omitted on create, defaults to the authenticated user. See Author id"),
        Property('body', StringType, description="The comment string. See Bodies"),
        Property('created_at', DateTimeType, description="The time the comment was created"),
        Property('html_body', StringType, description="The comment formatted as HTML. See Bodies"),
        Property('id', IntegerType, required=True, description="Automatically assigned when the comment is created"),
        Property('metadata', ObjectType(), description="System information (web client, IP address, etc.) and comment flags, if any. See Comment flags"),
        Property('plain_body', StringType, description="The comment presented as plain text. See Bodies"),
        Property('public', BooleanType, description="true if a public comment; false if an internal note. The initial value set on ticket creation persists for any additional comment unless you change it"),
        Property('type', StringType, description="Comment or VoiceComment. The JSON object for adding voice comments to tickets is different. See Adding voice comments to tickets"),
        Property('via', ObjectType(), description="Describes how the object was created. See the Via object reference"),
    ).to_dict()
