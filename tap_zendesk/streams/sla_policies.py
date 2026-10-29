from tap_zendesk.client import ZendeskStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/business-rules/sla_policies

class SLAPoliciesStream(ZendeskStream):
    name = 'sla_policies'
    path = '/api/v2/slas/policies'
    records_jsonpath = '$.sla_policies[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="The time the SLA policy was created"),
        Property('description', StringType, description="The description of the SLA policy"),
        Property('filter', ObjectType(), description="An object that describes the conditions that a ticket must match in order for an SLA policy to be applied to that ticket. See Filter."),
        Property('id', IntegerType, required=True, description="Automatically assigned when created"),
        Property('policy_metrics', ArrayType(ObjectType()), description="Array of Policy Metric objects"),
        Property('position', IntegerType, description="Position of the SLA policy that determines the order they will be matched. If not specified, the SLA policy is added as the last position"),
        Property('title', StringType, description="The title of the SLA policy"),
        Property('updated_at', DateTimeType, description="The time of the last update of the SLA policy"),
        Property('url', StringType, description="URL of the SLA policy record"),
    ).to_dict()
