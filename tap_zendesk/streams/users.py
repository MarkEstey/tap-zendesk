from tap_zendesk.client import ZendeskIncrementalCursorStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/users/users
# Incremental Documentation: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/#incremental-user-export-cursor-based

class UsersStream(ZendeskIncrementalCursorStream):
    name = 'users'
    path = '/api/v2/incremental/users'
    records_jsonpath = '$.users[*]'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('active', BooleanType, description="false if the user has been deleted"),
        Property('alias', StringType, description="An alias displayed to end users"),
        Property('chat_only', BooleanType, description="Whether or not the user is a chat-only agent"),
        Property('created_at', DateTimeType, description="The time the user was created"),
        Property('custom_role_id', IntegerType, description="A custom role if the user is an agent on the Enterprise plan or above"),
        Property('default_group_id', IntegerType, description="The id of the user's default group"),
        Property('details', StringType, description="Any details you want to store about the user, such as an address"),
        Property('email', StringType, description="The user's primary email address. *Writeable on create only. On update, a secondary email is added. See Email Address"),
        Property('external_id', StringType, description="A unique identifier from another system. The API treats the id as case insensitive. Example: \"ian1\" and \"IAN1\" are the same value."),
        Property('iana_time_zone', StringType, description="The time zone for the user"),
        Property('id', IntegerType, description="Automatically assigned when the user is created"),
        Property('last_login_at', DateTimeType, description="Last time the user signed in to Zendesk Support or made an API request using an API token"),
        Property('locale', StringType, description="The user's locale. A BCP-47 compliant tag for the locale. If both \"locale\" and \"locale_id\" are present on create or update, \"locale_id\" is ignored and only \"locale\" is used."),
        Property('locale_id', IntegerType, description="The user's language identifier"),
        Property('moderator', BooleanType, description="Designates whether the user has forum moderation capabilities"),
        Property('name', StringType, description="The user's name"),
        Property('notes', StringType, description="Any notes you want to store about the user"),
        Property('only_private_comments', BooleanType, description="true if the user can only create private comments"),
        Property('organization_id', IntegerType, description="The id of the user's organization. If the user has more than one organization memberships, the id of the user's default organization. If updating, see Organization ID"),
        Property('phone', StringType, description="The user's primary phone number. See Phone Number below"),
        Property('photo', ObjectType(), description="The user's profile picture represented as an Attachment object"),
        Property('remote_photo_url', StringType, description="A URL pointing to the user's profile picture."),
        Property('report_csv', BooleanType, description="This parameter is inert and has no effect. It may be deprecated in the future. Previously, this parameter determined whether a user could access a CSV report in a legacy Guide dashboard. This dashboard has been removed. See Announcing Guide legacy reporting upgrade to Explore"),
        Property('restricted_agent', BooleanType, description="If the agent has any restrictions; false for admins and unrestricted agents, true for other agents"),
        Property('role', StringType, description="The user's role. Possible values are \"end-user\", \"agent\", or \"admin\""),
        Property('role_type', IntegerType, description="The user's role id. 0 for a custom agent, 1 for a light agent, 2 for a chat agent, 3 for a chat agent added to the Support account as a contributor (Chat Phase 4), 4 for an admin, and 5 for a billing admin"),
        Property('shared', BooleanType, description="If the user is shared from a different Zendesk Support instance. Shared users can be added to organizations but cannot be modified through update requests. Any attempt to update a shared user results in a 403 Forbidden error. Ticket sharing accounts only"),
        Property('shared_agent', BooleanType, description="If the user is a shared agent from a different Zendesk Support instance. Ticket sharing accounts only"),
        Property('shared_phone_number', BooleanType, description="Whether the phone number is shared or not. See Phone Number below"),
        Property('signature', StringType, description="The user's signature. Only agents and admins can have signatures"),
        Property('suspended', BooleanType, description="If the agent is suspended. Tickets from suspended users are also suspended, and these users cannot sign in to the end user portal"),
        Property('suspension_details', ObjectType(), description="Channel-level suspension state for the user. The value is null if the user has no active channel-level suspension"),
        Property('tags', ArrayType(StringType), description="The user's tags. Only present if your account has user tagging enabled"),
        Property('ticket_restriction', StringType, description="Specifies which tickets the user has access to. Possible values are: \"organization\", \"groups\", \"assigned\", \"requested\", null. \"groups\" and \"assigned\" are valid only for agents. If you pass an invalid value to an end user (for example, \"groups\"), they will be assigned to \"requested\", regardless of their previous access"),
        Property('time_zone', StringType, description="The user's time zone. See Time Zone"),
        Property('two_factor_auth_enabled', BooleanType, description="If two factor authentication is enabled"),
        Property('updated_at', DateTimeType, description="The time the user was last updated"),
        Property('url', StringType, description="The user's API url"),
        Property('user_fields', ObjectType(), description="Values of custom fields in the user's profile. See User Fields"),
        Property('verified', BooleanType, description="Any of the user's identities is verified. See User Identities"),
    ).to_dict()
