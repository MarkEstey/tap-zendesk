from tap_zendesk.client import ZendeskIncrementalTimeStream
from singer_sdk.typing import *

# API Reference: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-export-time-based

class TicketsStream(ZendeskIncrementalTimeStream):
    name = 'tickets'
    path = '/api/v2/incremental/tickets'
    records_jsonpath = '$.tickets[*]'
    primary_keys = ['id']
    replication_key = 'generated_timestamp'

    schema = PropertiesList(
        Property('allow_attachments', BooleanType, description="Permission for agents to add add attachments to a comment. Defaults to true"),
        Property('allow_channelback', BooleanType, description="Is false if channelback is disabled, true otherwise. Only applicable for channels framework ticket"),
        Property('assignee_id', IntegerType, description="The agent currently assigned to the ticket"),
        Property('brand_id', IntegerType, description="The id of the brand this ticket is associated with. See Setting up multiple brands"),
        Property('collaborator_ids', ArrayType(IntegerType), description="The ids of users currently CC'ed on the ticket"),
        Property('created_at', DateTimeType, description="When this record was created"),
        Property('custom_fields', ArrayType(ObjectType()), description="Custom fields for the ticket. See Setting custom field values"),
        Property('custom_status_id', IntegerType, description="The custom ticket status id of the ticket. See custom ticket statuses"),
        Property('description', StringType, description="Read-only first comment on the ticket. When creating a ticket, use comment to set the description. See Description and first comment"),
        Property('due_at', DateTimeType, description="If this is a ticket of type \"task\" it has a due date. Due date format uses ISO 8601 format"),
        Property('email_cc_ids', ArrayType(IntegerType), description="The ids of agents or end users currently CC'ed on the ticket. Ignored when CCs and followers is not enabled"),
        Property('encoded_id', StringType, description="An encoded string representing the ticket's unique identifier"),
        Property('external_id', StringType, description="An id you can use to link Zendesk Support tickets to local records"),
        Property('follower_ids', ArrayType(IntegerType), description="The ids of agents currently following the ticket. Ignored when CCs and followers is not enabled"),
        Property('followup_ids', ArrayType(IntegerType), description="The ids of the followups created from this ticket. Ids are only visible once the ticket is closed"),
        Property('forum_topic_id', IntegerType, description="The topic in the Zendesk Web portal this ticket originated from, if any. The Web portal is deprecated"),
        Property('from_messaging_channel', BooleanType, description="If true, the ticket's via type is a messaging channel."),
        Property('generated_timestamp', IntegerType, description="A Unix timestamp that represents the most accurate reading of when this record was last updated. It is updated for all ticket updates, including system updates"),
        Property('group_id', IntegerType, description="The group this ticket is assigned to"),
        Property('has_incidents', BooleanType, description="Is true if a ticket is a problem type and has one or more incidents linked to it. Otherwise, the value is false."),
        Property('id', IntegerType, required=True, description="Automatically assigned when the ticket is created"),
        Property('is_public', BooleanType, description="Is true if any comments are public, false otherwise"),
        Property('organization_id', IntegerType, description="The organization of the requester. You can only specify the ID of an organization associated with the requester. See Organization Memberships"),
        Property('priority', StringType, description="The urgency with which the ticket should be addressed. Allowed values are \"urgent\", \"high\", \"normal\", or \"low\"."),
        Property('problem_id', IntegerType, description="For tickets of type \"incident\", the ID of the problem the incident is linked to"),
        Property('raw_subject', StringType, description="The dynamic content placeholder, if present, or the \"subject\" value, if not. See Dynamic Content Items"),
        Property('recipient', StringType, description="The original recipient e-mail address of the ticket. Notification emails for the ticket are sent from this address"),
        Property('requester_id', IntegerType, description="The user who requested this ticket"),
        Property('satisfaction_rating', ObjectType(), description="The satisfaction rating of the ticket, if it exists, or the state of satisfaction, \"offered\" or \"unoffered\". The value is null for plan types that don't support CSAT"),
        Property('sharing_agreement_ids', ArrayType(IntegerType), description="The ids of the sharing agreements used for this ticket"),
        Property('status', StringType, description="The state of the ticket. If your account has activated custom ticket statuses, this is the ticket's status category. See custom ticket statuses. Allowed values are \"new\", \"open\", \"pending\", \"hold\", \"solved\", or \"closed\"."),
        Property('subject', StringType, description="The value of the subject field for this ticket. See Subject"),
        Property('submitter_id', IntegerType, description="The user who submitted the ticket. The submitter always becomes the author of the first comment on the ticket"),
        Property('tags', ArrayType(StringType), description="The array of tags applied to this ticket. Unless otherwise specified, the set tag behavior is used, which overwrites and replaces existing tags"),
        Property('ticket_form_id', IntegerType, description="Enterprise only. The id of the ticket form to render for the ticket"),
        Property('type', StringType, description="The type of this ticket. Allowed values are \"problem\", \"incident\", \"question\", or \"task\"."),
        Property('updated_at', DateTimeType, description="When this record last got updated. It is updated only if the update generates a ticket event"),
        Property('url', StringType, description="The API url of this ticket"),
        Property('via', ObjectType(), description="For more information, see the Via object reference"),
    ).to_dict()

    def get_url_params(self, *args, **kwargs):
        return super().get_url_params(*args, **kwargs) | {'support_type_scope': 'all', 'include': 'comment_events'}

    def get_child_context(self, record, context):
        if record.get('status') != 'deleted':
            return {'ticket_id': record['id']}
