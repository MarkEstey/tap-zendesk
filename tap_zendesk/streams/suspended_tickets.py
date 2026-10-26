from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/suspended_tickets

class SuspendedTicketsStream(ZendeskCursorStream):
    name = 'suspended_tickets'
    path = '/api/v2/suspended_tickets'
    records_jsonpath = '$.suspended_tickets[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('attachments', ArrayType(ObjectType()), description="The attachments, if any associated to this suspended ticket. See Attachments"),
        Property('author', ObjectType(), description="The author id (if available), name and email"),
        Property('brand_id', IntegerType, description="The id of the brand this ticket is associated with. Only applicable for Enterprise accounts"),
        Property('cause', StringType, description="Why the ticket was suspended"),
        Property('cause_id', IntegerType, description="The ID of the cause"),
        Property('content', StringType, description="The content that was flagged"),
        Property('content_html', StringType, description="Sanitized HTML content when the suspended ticket was created from rich content. Omitted for plain-text suspended tickets."),
        Property('created_at', DateTimeType, description="The ticket ID this suspended email is associated with, if available"),
        Property('error_messages', ArrayType(StringType), description="The error messages if any associated to this suspended ticket"),
        Property('id', IntegerType, required=True, description="Automatically assigned"),
        Property('message_id', StringType, description="The ID of the email, if available"),
        Property('recipient', StringType, description="The original recipient e-mail address of the ticket"),
        Property('subject', StringType, description="The value of the subject field for this ticket"),
        Property('ticket_id', IntegerType, description="The ticket ID this suspended email is associated with, if available"),
        Property('updated_at', DateTimeType, description="When the ticket was assigned"),
        Property('url', StringType, description="The API url of this ticket"),
        Property('via', ObjectType(), description="An object explaining how the ticket was created. See the Via object reference"),
    ).to_dict()
