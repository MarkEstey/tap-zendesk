from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics

class TicketMetricsStream(ZendeskCursorStream):
    name = 'ticket_metrics'
    path = '/api/v2/ticket_metrics'
    records_jsonpath = '$.ticket_metrics[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('agent_wait_time_in_minutes', ObjectType(), description="Number of minutes the agent spent waiting during calendar and business hours"),
        Property('assigned_at', DateTimeType, description="When the ticket was assigned"),
        Property('assignee_stations', IntegerType, description="Number of assignees the ticket had"),
        Property('assignee_updated_at', StringType, description="When the assignee last updated the ticket"),
        Property('created_at', DateTimeType, description="When the record was created"),
        Property('custom_status_updated_at', StringType, description="The date and time the ticket's custom status was last updated"),
        Property('first_resolution_time_in_minutes', ObjectType(), description="Number of minutes to the first resolution time during calendar and business hours"),
        Property('full_resolution_time_in_minutes', ObjectType(), description="Number of minutes to the full resolution during calendar and business hours"),
        Property('group_stations', IntegerType, description="Number of groups the ticket passed through"),
        Property('id', IntegerType, required=True, description="Automatically assigned when the client is created"),
        Property('initially_assigned_at', DateTimeType, description="When the ticket was initially assigned"),
        Property('latest_comment_added_at', DateTimeType, description="When the latest comment was added"),
        Property('on_hold_time_in_minutes', ObjectType(), description="Number of minutes on hold"),
        Property('reopens', IntegerType, description="Total number of times the ticket was reopened"),
        Property('replies', IntegerType, description="The number of public replies added to a ticket by an agent"),
        Property('reply_time_in_minutes', ObjectType(), description="Number of minutes to the first reply during calendar and business hours"),
        Property('reply_time_in_seconds', ObjectType(), description="Number of seconds to the first reply during calendar hours, only available for Messaging tickets"),
        Property('requester_updated_at', DateTimeType, description="When the requester last updated the ticket"),
        Property('requester_wait_time_in_minutes', ObjectType(), description="Number of minutes the requester spent waiting during calendar and business hours"),
        Property('solved_at', DateTimeType, description="When the ticket was solved"),
        Property('status_updated_at', DateTimeType, description="When the status of the ticket was last updated"),
        Property('ticket_id', IntegerType, description="Id of the associated ticket"),
        Property('updated_at', DateTimeType, description="When the record was last updated"),
        Property('url', StringType, description="The API url of the ticket metric"),
    ).to_dict()
