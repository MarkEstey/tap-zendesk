from singer_sdk import Tap
from singer_sdk.typing import *
from tap_zendesk.streams import *

class TapZendesk(Tap):
    name = 'tap-zendesk'

    config_jsonschema = PropertiesList(
        Property('url_base', StringType, default='https://zendesk.com', description='Base url for the Zendesk API'),
        Property('email', StringType, required=True, description='Email address used to log in'),
        Property('api_token', StringType, secret=True, description='API token for the user'),
        Property('incremental_request_rate', IntegerType, default=10, description='Maximum number of incremental requests per minute (see: https://developer.zendesk.com/api-reference/introduction/rate-limits/#endpoint-rate-limits)'),
        Property('start_date', DateTimeType, default='2007-09-01T00:00:00Z', description='The earliest record date to sync'),
        Property(
            'stream_type_conformance',
            StringType,
            allowed_values=['none', 'root_only', 'recursive'],
            default='root_only',
            description='The level of type conformance to apply to streams '
                '(see: https://sdk.meltano.com/en/latest/classes/singer_sdk.Stream.html#singer_sdk.Stream.TYPE_CONFORMANCE_LEVEL). '
                'Defaults to root_only. Must be one of: none, root_only, recursive',
        ),
        Property('stream_maps', ObjectType(), description='Inline stream maps (see: https://sdk.meltano.com/en/latest/stream_maps.html)'),
        Property('stream_map_config', ObjectType(), description='Inline stream maps config (see: https://sdk.meltano.com/en/latest/stream_maps.html)'),
    ).to_dict()

    def discover_streams(self):
        return [
            BrandsStream(self),
            ConversationLogStream(self),
            CustomObjectFieldsStream(self),
            CustomObjectRecordsStream(self),
            CustomObjectsStream(self),
            CustomRolesStream(self),
            CustomStatusesStream(self),
            GroupMembershipsStream(self),
            GroupsStream(self),
            OrganizationFieldsStream(self),
            OrganizationMembershipsStream(self),
            OrganizationsStream(self),
            OrganizationSubscriptionsStream(self),
            SharingAgreementsStream(self),
            SLAPoliciesStream(self),
            SuspendedTicketsStream(self),
            TicketCommentsStream(self),
            TicketEventsStream(self),
            TicketFieldsStream(self),
            TicketFormsStream(self),
            TicketFormStatusesStream(self),
            TicketMetricEventsStream(self),
            TicketMetricsStream(self),
            TicketSkipsStream(self),
            TicketsStream(self),
            UserFieldsStream(self),
            UsersStream(self),
        ]

if __name__ == '__main__':
    TapZendesk.cli()
