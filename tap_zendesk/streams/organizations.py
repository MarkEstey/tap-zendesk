from tap_zendesk.client import ZendeskIncrementalCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations
# Incremental Documentation: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/#incremental-organization-export

class OrganizationsStream(ZendeskIncrementalCursorStream):
    name = 'organizations'
    path = '/api/v2/incremental/organizations'
    records_jsonpath = '$.organizations[*]'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('children_count', IntegerType, description="Number of direct children when organization hierarchy is enabled, 0 otherwise"),
        Property('created_at', DateTimeType, description="The time the organization was created"),
        Property('details', StringType, description="Any details obout the organization, such as the address"),
        Property('domain_names', ArrayType(StringType), description="An array of domain names associated with this organization"),
        Property('external_id', StringType, description="A unique external id to associate organizations to an external record. The id is case-insensitive. For example, \"company1\" and \"Company1\" are considered the same"),
        Property('group_id', IntegerType, description="New tickets from users in this organization are automatically put in this group"),
        Property('id', IntegerType, description="Automatically assigned when the organization is created"),
        Property('name', StringType, description="A unique name for the organization"),
        Property('notes', StringType, description="Any notes you have about the organization"),
        Property('organization_fields', ObjectType(), description="Custom fields for this organization. See Custom organization fields"),
        Property('shared_comments', BooleanType, description="End users in this organization are able to comment on each other's tickets"),
        Property('shared_tickets', BooleanType, description="End users in this organization are able to see each other's tickets. This property will be deprecated in the future. Use ticket_restriction instead."),
        Property('tags', ArrayType(StringType), description="The tags of the organization"),
        Property('ticket_restriction', StringType, description="Which tickets end users in this organization can see. Possible values are \"restricted\" or \"organization\". Takes precedence over the shared_tickets property. Allowed values are \"restricted\", or \"organization\"."),
        Property('updated_at', DateTimeType, description="The time of the last update of the organization"),
        Property('url', StringType, description="The API url of this organization"),
    ).to_dict()
