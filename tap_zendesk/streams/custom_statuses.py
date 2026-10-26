from tap_zendesk.client import ZendeskStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/tickets/custom_ticket_statuses

class CustomStatusesStream(ZendeskStream):
    name = 'custom_statuses'
    path = '/api/v2/custom_statuses'
    records_jsonpath = '$.custom_statuses[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('active', BooleanType, description="If true, the custom status is set to active, If false, the custom status is set to inactive"),
        Property('agent_label', StringType, description="The label displayed to agents. Maximum length is 48 characters"),
        Property('created_at', DateTimeType, description="The date and time the custom ticket status was created"),
        Property('default', BooleanType, description="If true, the custom status is set to default. If false, the custom status is set to non-default"),
        Property('description', StringType, description="The description of when the user should select this custom ticket status"),
        Property('end_user_description', StringType, description="The description displayed to end users"),
        Property('end_user_label', StringType, description="The label displayed to end users. Maximum length is 48 characters"),
        Property('id', IntegerType, required=True, description="Automatically assigned when the custom ticket status is created"),
        Property('raw_agent_label', StringType, description="The dynamic content placeholder. If the dynamic content placeholder is not available, this is the \"agent_label\" value. See Dynamic Content Items"),
        Property('raw_description', StringType, description="The dynamic content placeholder. If the dynamic content placeholder is not available, this is the \"description\" value. Dynamic Content Items"),
        Property('raw_end_user_description', StringType, description="The dynamic content placeholder. If the dynamic content placeholder is not available, this is the \"end_user_description\" value. See Dynamic Content Items"),
        Property('raw_end_user_label', StringType, description="The dynamic content placeholder. If the dynamic content placeholder is not available, this is the \"end_user_label\" value. See Dynamic Content Items"),
        Property('status_category', StringType, description="The status category the custom ticket status belongs to. Allowed values are \"new\", \"open\", \"pending\", \"hold\", or \"solved\"."),
        Property('updated_at', DateTimeType, description="The date and time the custom ticket status was last updated"),
        Property('url', StringType, description="The URL for this resource"),
    ).to_dict()
