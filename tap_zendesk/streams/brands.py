from tap_zendesk.client import ZendeskCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/account-configuration/brands/

class BrandsStream(ZendeskCursorStream):
    name = 'brands'
    path = '/api/v2/brands'
    records_jsonpath = '$.brands[*]'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('active', BooleanType, description="If the brand is set as active"),
        Property('brand_url', StringType, description="The url of the brand"),
        Property('created_at', DateTimeType, description="The time the brand was created"),
        Property('default', BooleanType, description="Is the brand the default brand for this account"),
        Property('has_help_center', BooleanType, description="If the brand has a Help Center"),
        Property('help_center_state', StringType, description="The state of the Help Center. Allowed values are \"enabled\", \"disabled\", or \"restricted\"."),
        Property('host_mapping', StringType, description="The hostmapping to this brand, if any. Only admins view this property."),
        Property('id', IntegerType, required=True, description="The ID automatically assigned when the brand is created"),
        Property('is_deleted', BooleanType, description="If the brand object is deleted or not"),
        Property('logo', ObjectType(), description="A file represented as an Attachment object"),
        Property('name', StringType, description="The name of the brand"),
        Property('signature_template', StringType, description="The signature template for a brand"),
        Property('subdomain', StringType, description="The subdomain of the brand"),
        Property('ticket_form_ids', ArrayType(IntegerType), description="The ids of ticket forms that are available for use by a brand"),
        Property('updated_at', DateTimeType, description="The time of the last update of the brand"),
        Property('url', StringType, description="The API url of this brand"),
    ).to_dict()
