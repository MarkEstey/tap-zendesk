from tap_zendesk.client import ZendeskIncrementalCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metric_events/#list-ticket-metric-events

class TicketMetricEventsStream(ZendeskIncrementalCursorStream):
    name = 'ticket_metric_events'
    path = '/api/v2/incremental/ticket_metric_events'
    records_jsonpath = '$.ticket_metric_events[*]'
    primary_keys = ['id']
    replication_key = 'time'

    schema = PropertiesList(
        Property('deleted', BooleanType, description="If true, the event has been deleted"),
        Property('id', IntegerType, description="Automatically assigned when the record is created"),
        Property('instance_id', IntegerType, description="The instance of the metric associated with the event. See instance_id"),
        Property('metric', StringType, description="The metric being tracked. Allowed values are \"agent_work_time\", \"pausable_update_time\", \"periodic_update_time\", \"reply_time\", \"requester_wait_time\", \"resolution_time\", or \"group_ownership_time\"."),
        Property('ticket_id', IntegerType, description="Id of the associated ticket"),
        Property('time', DateTimeType, description="The time the event occurred"),
        Property('type', StringType, description="The type of the metric event. See Ticket metric event types reference. Allowed values are \"activate\", \"pause\", \"fulfill\", \"apply_sla\", \"apply_group_sla\", \"breach\", \"update_status\", or \"measure\"."),
        Property('sla', ObjectType(), description="Available if type is \"apply_sla\". The SLA policy and target being enforced on the ticket and metric in question, if any. See sla"),
        Property('group_sla', ObjectType(), description="Available if type is \"apply_group_sla\". The Group SLA policy and target being enforced on the ticket and metric in question, if any. See group_sla"),
        Property('status', ObjectType(), description="Available if type is \"update_status\". Minutes since the metric has been open. See status"),
    ).to_dict()

    def get_url_params(self, *args, **kwargs):
        return super().get_url_params(*args, **kwargs) | {'include_changes': 'true'}
