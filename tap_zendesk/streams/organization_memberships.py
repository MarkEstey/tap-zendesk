from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_memberships

class OrganizationMembershipsStream(ZendeskCursorStream):
    name = 'organization_memberships'
    path = '/api/v2/organization_memberships'
    records_jsonpath = '$.organization_memberships[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('created_at', DateTimeType, description="When this record was created"),
        Property('default', BooleanType, description="Denotes whether this is the default organization membership for the user. If false, returns null"),
        Property('id', IntegerType, required=True, description="Automatically assigned when the membership is created"),
        Property('organization_id', IntegerType, description="The ID of the organization associated with this user, in this membership"),
        Property('organization_name', StringType, description="The name of the organization associated with this user, in this membership"),
        Property('updated_at', DateTimeType, description="When this record last got updated"),
        Property('url', StringType, description="The API url of this membership"),
        Property('user_id', IntegerType, description="The ID of the user for whom this membership belongs"),
        Property('view_tickets', BooleanType, description="Denotes whether the user can or cannot have access to all organization's tickets."),
    ).to_dict()
