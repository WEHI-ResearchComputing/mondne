from typing import Any, Dict, Optional

from . import (
    BaseRoleName,
    BoardAttributes,
    BoardKind,
    BoardSubscriberKind,
    ColumnProperty,
    ColumnType,
    CustomActivityColor,
    CustomActivityIcon,
    DocBlockContentType,
    DuplicateBoardType,
    FolderColor,
    FolderCustomIcon,
    FolderFontWeight,
    GroupAttributes,
    NotificationTargetType,
    PositionRelative,
    WebhookEventType,
    WorkspaceKind,
    WorkspaceSubscriberKind,
)
from .custom_fields import (
    ActivateUsersResultFields,
    AppSubscriptionFields,
    AppSubscriptionOperationsCounterFields,
    AssetFields,
    AssignTeamOwnersResultFields,
    BatchExtendTrialPeriodFields,
    BoardDuplicationFields,
    BoardFields,
    ChangeTeamMembershipsResultFields,
    ColumnFields,
    ComplexityFields,
    CustomActivityFields,
    DeactivateUsersResultFields,
    DeleteMarketplaceAppDiscountResultFields,
    DocumentBlockFields,
    DocumentBlockIdOnlyFields,
    DocumentFields,
    FolderFields,
    GrantMarketplaceAppDiscountResultFields,
    GroupFields,
    ItemFields,
    NotificationFields,
    RemoveTeamOwnersResultFields,
    TagFields,
    TeamFields,
    TemplateFields,
    TimelineItemFields,
    UpdateEmailDomainResultFields,
    UpdateFields,
    UpdateUsersRoleResultFields,
    UserFields,
    WebhookFields,
    WorkspaceFields,
)
from .custom_typing_fields import GraphQLField
from .input_types import (
    ColumnMappingInput,
    CreateDocInput,
    CreateTeamAttributesInput,
    CreateTeamOptionsInput,
    GrantMarketplaceAppDiscountData,
    TimelineItemTimeRange,
    UpdateEmailDomainAttributesInput,
    UpdateWorkspaceAttributesInput,
)


class Mutation:
    @classmethod
    def like_update(cls, update_id: str) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "update_id": {"type": "ID!", "value": update_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="like_update", arguments=cleared_arguments)

    @classmethod
    def unlike_update(cls, update_id: str) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "update_id": {"type": "ID!", "value": update_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="unlike_update", arguments=cleared_arguments)

    @classmethod
    def delete_update(cls, id: str) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "ID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="delete_update", arguments=cleared_arguments)

    @classmethod
    def edit_update(cls, id: str, body: str) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "id": {"type": "ID!", "value": id},
            "body": {"type": "String!", "value": body},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="edit_update", arguments=cleared_arguments)

    @classmethod
    def pin_to_top(cls, id: str, *, item_id: Optional[str] = None) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "id": {"type": "ID!", "value": id},
            "item_id": {"type": "ID", "value": item_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="pin_to_top", arguments=cleared_arguments)

    @classmethod
    def unpin_from_top(cls, id: str, *, item_id: Optional[str] = None) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "id": {"type": "ID!", "value": id},
            "item_id": {"type": "ID", "value": item_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="unpin_from_top", arguments=cleared_arguments)

    @classmethod
    def create_update(
        cls,
        body: str,
        *,
        item_id: Optional[str] = None,
        parent_id: Optional[str] = None
    ) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "body": {"type": "String!", "value": body},
            "item_id": {"type": "ID", "value": item_id},
            "parent_id": {"type": "ID", "value": parent_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="create_update", arguments=cleared_arguments)

    @classmethod
    def create_timeline_item(
        cls,
        item_id: str,
        title: str,
        timestamp: Any,
        custom_activity_id: str,
        *,
        user_id: Optional[int] = None,
        summary: Optional[str] = None,
        content: Optional[str] = None,
        location: Optional[str] = None,
        phone: Optional[str] = None,
        url: Optional[str] = None,
        time_range: Optional[TimelineItemTimeRange] = None
    ) -> TimelineItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "item_id": {"type": "ID!", "value": item_id},
            "user_id": {"type": "Int", "value": user_id},
            "title": {"type": "String!", "value": title},
            "timestamp": {"type": "ISO8601DateTime!", "value": timestamp},
            "summary": {"type": "String", "value": summary},
            "content": {"type": "String", "value": content},
            "location": {"type": "String", "value": location},
            "phone": {"type": "String", "value": phone},
            "url": {"type": "String", "value": url},
            "time_range": {"type": "TimelineItemTimeRange", "value": time_range},
            "custom_activity_id": {"type": "String!", "value": custom_activity_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimelineItemFields(
            field_name="create_timeline_item", arguments=cleared_arguments
        )

    @classmethod
    def delete_timeline_item(cls, id: str) -> TimelineItemFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimelineItemFields(
            field_name="delete_timeline_item", arguments=cleared_arguments
        )

    @classmethod
    def create_custom_activity(
        cls, name: str, icon_id: CustomActivityIcon, color: CustomActivityColor
    ) -> CustomActivityFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "name": {"type": "String!", "value": name},
            "icon_id": {"type": "CustomActivityIcon!", "value": icon_id},
            "color": {"type": "CustomActivityColor!", "value": color},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomActivityFields(
            field_name="create_custom_activity", arguments=cleared_arguments
        )

    @classmethod
    def delete_custom_activity(cls, id: str) -> CustomActivityFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomActivityFields(
            field_name="delete_custom_activity", arguments=cleared_arguments
        )

    @classmethod
    def grant_marketplace_app_discount(
        cls, app_id: str, account_slug: str, data: GrantMarketplaceAppDiscountData
    ) -> GrantMarketplaceAppDiscountResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_id": {"type": "ID!", "value": app_id},
            "account_slug": {"type": "String!", "value": account_slug},
            "data": {"type": "GrantMarketplaceAppDiscountData!", "value": data},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GrantMarketplaceAppDiscountResultFields(
            field_name="grant_marketplace_app_discount", arguments=cleared_arguments
        )

    @classmethod
    def delete_marketplace_app_discount(
        cls, app_id: str, account_slug: str
    ) -> DeleteMarketplaceAppDiscountResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_id": {"type": "ID!", "value": app_id},
            "account_slug": {"type": "String!", "value": account_slug},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeleteMarketplaceAppDiscountResultFields(
            field_name="delete_marketplace_app_discount", arguments=cleared_arguments
        )

    @classmethod
    def add_file_to_column(cls, column_id: str, file: Any, item_id: str) -> AssetFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "column_id": {"type": "String!", "value": column_id},
            "file": {"type": "File!", "value": file},
            "item_id": {"type": "ID!", "value": item_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AssetFields(field_name="add_file_to_column", arguments=cleared_arguments)

    @classmethod
    def add_file_to_update(cls, file: Any, update_id: str) -> AssetFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "file": {"type": "File!", "value": file},
            "update_id": {"type": "ID!", "value": update_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AssetFields(field_name="add_file_to_update", arguments=cleared_arguments)

    @classmethod
    def add_subscribers_to_board(
        cls, board_id: str, user_ids: str, *, kind: Optional[BoardSubscriberKind] = None
    ) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "kind": {"type": "BoardSubscriberKind", "value": kind},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(
            field_name="add_subscribers_to_board", arguments=cleared_arguments
        )

    @classmethod
    def add_teams_to_board(
        cls, board_id: str, team_ids: str, *, kind: Optional[BoardSubscriberKind] = None
    ) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "kind": {"type": "BoardSubscriberKind", "value": kind},
            "team_ids": {"type": "ID!", "value": team_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(field_name="add_teams_to_board", arguments=cleared_arguments)

    @classmethod
    def add_teams_to_workspace(
        cls,
        team_ids: str,
        workspace_id: str,
        *,
        kind: Optional[WorkspaceSubscriberKind] = None
    ) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "kind": {"type": "WorkspaceSubscriberKind", "value": kind},
            "team_ids": {"type": "ID!", "value": team_ids},
            "workspace_id": {"type": "ID!", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(
            field_name="add_teams_to_workspace", arguments=cleared_arguments
        )

    @classmethod
    def add_users_to_board(
        cls, board_id: str, user_ids: str, *, kind: Optional[BoardSubscriberKind] = None
    ) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "kind": {"type": "BoardSubscriberKind", "value": kind},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="add_users_to_board", arguments=cleared_arguments)

    @classmethod
    def add_users_to_team(
        cls, team_id: str, user_ids: str
    ) -> ChangeTeamMembershipsResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "team_id": {"type": "ID!", "value": team_id},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ChangeTeamMembershipsResultFields(
            field_name="add_users_to_team", arguments=cleared_arguments
        )

    @classmethod
    def add_users_to_workspace(
        cls,
        user_ids: str,
        workspace_id: str,
        *,
        kind: Optional[WorkspaceSubscriberKind] = None
    ) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "kind": {"type": "WorkspaceSubscriberKind", "value": kind},
            "user_ids": {"type": "ID!", "value": user_ids},
            "workspace_id": {"type": "ID!", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(
            field_name="add_users_to_workspace", arguments=cleared_arguments
        )

    @classmethod
    def archive_board(cls, board_id: str) -> BoardFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BoardFields(field_name="archive_board", arguments=cleared_arguments)

    @classmethod
    def archive_group(cls, board_id: str, group_id: str) -> GroupFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "group_id": {"type": "String!", "value": group_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GroupFields(field_name="archive_group", arguments=cleared_arguments)

    @classmethod
    def archive_item(cls, *, item_id: Optional[str] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "item_id": {"type": "ID", "value": item_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="archive_item", arguments=cleared_arguments)

    @classmethod
    def batch_extend_trial_period(
        cls, account_slugs: str, app_id: str, duration_in_days: int, plan_id: str
    ) -> BatchExtendTrialPeriodFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "account_slugs": {"type": "String!", "value": account_slugs},
            "app_id": {"type": "ID!", "value": app_id},
            "duration_in_days": {"type": "Int!", "value": duration_in_days},
            "plan_id": {"type": "String!", "value": plan_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BatchExtendTrialPeriodFields(
            field_name="batch_extend_trial_period", arguments=cleared_arguments
        )

    @classmethod
    def change_column_metadata(
        cls,
        board_id: str,
        column_id: str,
        *,
        column_property: Optional[ColumnProperty] = None,
        value: Optional[str] = None
    ) -> ColumnFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_id": {"type": "String!", "value": column_id},
            "column_property": {"type": "ColumnProperty", "value": column_property},
            "value": {"type": "String", "value": value},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ColumnFields(
            field_name="change_column_metadata", arguments=cleared_arguments
        )

    @classmethod
    def change_column_title(
        cls, board_id: str, column_id: str, title: str
    ) -> ColumnFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_id": {"type": "String!", "value": column_id},
            "title": {"type": "String!", "value": title},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ColumnFields(
            field_name="change_column_title", arguments=cleared_arguments
        )

    @classmethod
    def change_column_value(
        cls,
        board_id: str,
        column_id: str,
        value: Any,
        *,
        create_labels_if_missing: Optional[bool] = None,
        item_id: Optional[str] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_id": {"type": "String!", "value": column_id},
            "create_labels_if_missing": {
                "type": "Boolean",
                "value": create_labels_if_missing,
            },
            "item_id": {"type": "ID", "value": item_id},
            "value": {"type": "JSON!", "value": value},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="change_column_value", arguments=cleared_arguments)

    @classmethod
    def change_multiple_column_values(
        cls,
        board_id: str,
        column_values: Any,
        *,
        create_labels_if_missing: Optional[bool] = None,
        item_id: Optional[str] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_values": {"type": "JSON!", "value": column_values},
            "create_labels_if_missing": {
                "type": "Boolean",
                "value": create_labels_if_missing,
            },
            "item_id": {"type": "ID", "value": item_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(
            field_name="change_multiple_column_values", arguments=cleared_arguments
        )

    @classmethod
    def change_simple_column_value(
        cls,
        board_id: str,
        column_id: str,
        *,
        create_labels_if_missing: Optional[bool] = None,
        item_id: Optional[str] = None,
        value: Optional[str] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_id": {"type": "String!", "value": column_id},
            "create_labels_if_missing": {
                "type": "Boolean",
                "value": create_labels_if_missing,
            },
            "item_id": {"type": "ID", "value": item_id},
            "value": {"type": "String", "value": value},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(
            field_name="change_simple_column_value", arguments=cleared_arguments
        )

    @classmethod
    def clear_item_updates(cls, item_id: str) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "item_id": {"type": "ID!", "value": item_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="clear_item_updates", arguments=cleared_arguments)

    @classmethod
    def complexity(cls) -> ComplexityFields:
        return ComplexityFields(field_name="complexity")

    @classmethod
    def create_board(
        cls,
        board_kind: BoardKind,
        board_name: str,
        *,
        board_owner_ids: Optional[str] = None,
        board_owner_team_ids: Optional[str] = None,
        board_subscriber_ids: Optional[str] = None,
        board_subscriber_teams_ids: Optional[str] = None,
        description: Optional[str] = None,
        empty: Optional[bool] = None,
        folder_id: Optional[str] = None,
        template_id: Optional[str] = None,
        workspace_id: Optional[str] = None
    ) -> BoardFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_kind": {"type": "BoardKind!", "value": board_kind},
            "board_name": {"type": "String!", "value": board_name},
            "board_owner_ids": {"type": "ID", "value": board_owner_ids},
            "board_owner_team_ids": {"type": "ID", "value": board_owner_team_ids},
            "board_subscriber_ids": {"type": "ID", "value": board_subscriber_ids},
            "board_subscriber_teams_ids": {
                "type": "ID",
                "value": board_subscriber_teams_ids,
            },
            "description": {"type": "String", "value": description},
            "empty": {"type": "Boolean", "value": empty},
            "folder_id": {"type": "ID", "value": folder_id},
            "template_id": {"type": "ID", "value": template_id},
            "workspace_id": {"type": "ID", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BoardFields(field_name="create_board", arguments=cleared_arguments)

    @classmethod
    def create_column(
        cls,
        board_id: str,
        column_type: ColumnType,
        title: str,
        *,
        after_column_id: Optional[str] = None,
        defaults: Optional[Any] = None,
        description: Optional[str] = None,
        id: Optional[str] = None
    ) -> ColumnFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "after_column_id": {"type": "ID", "value": after_column_id},
            "board_id": {"type": "ID!", "value": board_id},
            "column_type": {"type": "ColumnType!", "value": column_type},
            "defaults": {"type": "JSON", "value": defaults},
            "description": {"type": "String", "value": description},
            "id": {"type": "String", "value": id},
            "title": {"type": "String!", "value": title},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ColumnFields(field_name="create_column", arguments=cleared_arguments)

    @classmethod
    def create_doc(cls, location: CreateDocInput) -> DocumentFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "location": {"type": "CreateDocInput!", "value": location}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentFields(field_name="create_doc", arguments=cleared_arguments)

    @classmethod
    def create_doc_block(
        cls,
        content: Any,
        doc_id: str,
        type: DocBlockContentType,
        *,
        after_block_id: Optional[str] = None,
        parent_block_id: Optional[str] = None
    ) -> DocumentBlockFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "after_block_id": {"type": "String", "value": after_block_id},
            "content": {"type": "JSON!", "value": content},
            "doc_id": {"type": "ID!", "value": doc_id},
            "parent_block_id": {"type": "String", "value": parent_block_id},
            "type": {"type": "DocBlockContentType!", "value": type},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentBlockFields(
            field_name="create_doc_block", arguments=cleared_arguments
        )

    @classmethod
    def create_folder(
        cls,
        name: str,
        *,
        color: Optional[FolderColor] = None,
        custom_icon: Optional[FolderCustomIcon] = None,
        font_weight: Optional[FolderFontWeight] = None,
        parent_folder_id: Optional[str] = None,
        workspace_id: Optional[str] = None
    ) -> FolderFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "color": {"type": "FolderColor", "value": color},
            "custom_icon": {"type": "FolderCustomIcon", "value": custom_icon},
            "font_weight": {"type": "FolderFontWeight", "value": font_weight},
            "name": {"type": "String!", "value": name},
            "parent_folder_id": {"type": "ID", "value": parent_folder_id},
            "workspace_id": {"type": "ID", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FolderFields(field_name="create_folder", arguments=cleared_arguments)

    @classmethod
    def create_group(
        cls,
        board_id: str,
        group_name: str,
        *,
        group_color: Optional[str] = None,
        position: Optional[str] = None,
        position_relative_method: Optional[PositionRelative] = None,
        relative_to: Optional[str] = None
    ) -> GroupFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "group_color": {"type": "String", "value": group_color},
            "group_name": {"type": "String!", "value": group_name},
            "position": {"type": "String", "value": position},
            "position_relative_method": {
                "type": "PositionRelative",
                "value": position_relative_method,
            },
            "relative_to": {"type": "String", "value": relative_to},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GroupFields(field_name="create_group", arguments=cleared_arguments)

    @classmethod
    def create_item(
        cls,
        board_id: str,
        item_name: str,
        *,
        column_values: Optional[Any] = None,
        create_labels_if_missing: Optional[bool] = None,
        group_id: Optional[str] = None,
        position_relative_method: Optional[PositionRelative] = None,
        relative_to: Optional[str] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_values": {"type": "JSON", "value": column_values},
            "create_labels_if_missing": {
                "type": "Boolean",
                "value": create_labels_if_missing,
            },
            "group_id": {"type": "String", "value": group_id},
            "item_name": {"type": "String!", "value": item_name},
            "position_relative_method": {
                "type": "PositionRelative",
                "value": position_relative_method,
            },
            "relative_to": {"type": "ID", "value": relative_to},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="create_item", arguments=cleared_arguments)

    @classmethod
    def create_notification(
        cls,
        target_id: str,
        target_type: NotificationTargetType,
        text: str,
        user_id: str,
    ) -> NotificationFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "target_id": {"type": "ID!", "value": target_id},
            "target_type": {"type": "NotificationTargetType!", "value": target_type},
            "text": {"type": "String!", "value": text},
            "user_id": {"type": "ID!", "value": user_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationFields(
            field_name="create_notification", arguments=cleared_arguments
        )

    @classmethod
    def create_or_get_tag(
        cls, *, board_id: Optional[str] = None, tag_name: Optional[str] = None
    ) -> TagFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID", "value": board_id},
            "tag_name": {"type": "String", "value": tag_name},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TagFields(field_name="create_or_get_tag", arguments=cleared_arguments)

    @classmethod
    def create_subitem(
        cls,
        item_name: str,
        parent_item_id: str,
        *,
        column_values: Optional[Any] = None,
        create_labels_if_missing: Optional[bool] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "column_values": {"type": "JSON", "value": column_values},
            "create_labels_if_missing": {
                "type": "Boolean",
                "value": create_labels_if_missing,
            },
            "item_name": {"type": "String!", "value": item_name},
            "parent_item_id": {"type": "ID!", "value": parent_item_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="create_subitem", arguments=cleared_arguments)

    @classmethod
    def create_webhook(
        cls,
        board_id: str,
        event: WebhookEventType,
        url: str,
        *,
        config: Optional[Any] = None
    ) -> WebhookFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "config": {"type": "JSON", "value": config},
            "event": {"type": "WebhookEventType!", "value": event},
            "url": {"type": "String!", "value": url},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookFields(field_name="create_webhook", arguments=cleared_arguments)

    @classmethod
    def create_workspace(
        cls, kind: WorkspaceKind, name: str, *, description: Optional[str] = None
    ) -> WorkspaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "description": {"type": "String", "value": description},
            "kind": {"type": "WorkspaceKind!", "value": kind},
            "name": {"type": "String!", "value": name},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkspaceFields(
            field_name="create_workspace", arguments=cleared_arguments
        )

    @classmethod
    def delete_board(cls, board_id: str) -> BoardFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BoardFields(field_name="delete_board", arguments=cleared_arguments)

    @classmethod
    def delete_column(cls, board_id: str, column_id: str) -> ColumnFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "column_id": {"type": "String!", "value": column_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ColumnFields(field_name="delete_column", arguments=cleared_arguments)

    @classmethod
    def delete_doc_block(cls, block_id: str) -> DocumentBlockIdOnlyFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "block_id": {"type": "String!", "value": block_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentBlockIdOnlyFields(
            field_name="delete_doc_block", arguments=cleared_arguments
        )

    @classmethod
    def delete_folder(cls, folder_id: str) -> FolderFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "folder_id": {"type": "ID!", "value": folder_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FolderFields(field_name="delete_folder", arguments=cleared_arguments)

    @classmethod
    def delete_group(cls, board_id: str, group_id: str) -> GroupFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "group_id": {"type": "String!", "value": group_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GroupFields(field_name="delete_group", arguments=cleared_arguments)

    @classmethod
    def delete_item(cls, *, item_id: Optional[str] = None) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "item_id": {"type": "ID", "value": item_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="delete_item", arguments=cleared_arguments)

    @classmethod
    def delete_subscribers_from_board(cls, board_id: str, user_ids: str) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(
            field_name="delete_subscribers_from_board", arguments=cleared_arguments
        )

    @classmethod
    def delete_teams_from_board(cls, board_id: str, team_ids: str) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "team_ids": {"type": "ID!", "value": team_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(
            field_name="delete_teams_from_board", arguments=cleared_arguments
        )

    @classmethod
    def delete_teams_from_workspace(
        cls, team_ids: str, workspace_id: str
    ) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "team_ids": {"type": "ID!", "value": team_ids},
            "workspace_id": {"type": "ID!", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(
            field_name="delete_teams_from_workspace", arguments=cleared_arguments
        )

    @classmethod
    def delete_users_from_workspace(
        cls, user_ids: str, workspace_id: str
    ) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "user_ids": {"type": "ID!", "value": user_ids},
            "workspace_id": {"type": "ID!", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(
            field_name="delete_users_from_workspace", arguments=cleared_arguments
        )

    @classmethod
    def delete_webhook(cls, id: str) -> WebhookFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "ID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookFields(field_name="delete_webhook", arguments=cleared_arguments)

    @classmethod
    def delete_workspace(cls, workspace_id: str) -> WorkspaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "workspace_id": {"type": "ID!", "value": workspace_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkspaceFields(
            field_name="delete_workspace", arguments=cleared_arguments
        )

    @classmethod
    def duplicate_board(
        cls,
        board_id: str,
        duplicate_type: DuplicateBoardType,
        *,
        board_name: Optional[str] = None,
        folder_id: Optional[str] = None,
        keep_subscribers: Optional[bool] = None,
        workspace_id: Optional[str] = None
    ) -> BoardDuplicationFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "board_name": {"type": "String", "value": board_name},
            "duplicate_type": {"type": "DuplicateBoardType!", "value": duplicate_type},
            "folder_id": {"type": "ID", "value": folder_id},
            "keep_subscribers": {"type": "Boolean", "value": keep_subscribers},
            "workspace_id": {"type": "ID", "value": workspace_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BoardDuplicationFields(
            field_name="duplicate_board", arguments=cleared_arguments
        )

    @classmethod
    def duplicate_group(
        cls,
        board_id: str,
        group_id: str,
        *,
        add_to_top: Optional[bool] = None,
        group_title: Optional[str] = None
    ) -> GroupFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "add_to_top": {"type": "Boolean", "value": add_to_top},
            "board_id": {"type": "ID!", "value": board_id},
            "group_id": {"type": "String!", "value": group_id},
            "group_title": {"type": "String", "value": group_title},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GroupFields(field_name="duplicate_group", arguments=cleared_arguments)

    @classmethod
    def duplicate_item(
        cls,
        board_id: str,
        *,
        item_id: Optional[str] = None,
        with_updates: Optional[bool] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "item_id": {"type": "ID", "value": item_id},
            "with_updates": {"type": "Boolean", "value": with_updates},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="duplicate_item", arguments=cleared_arguments)

    @classmethod
    def increase_app_subscription_operations(
        cls, *, increment_by: Optional[int] = None, kind: Optional[str] = None
    ) -> AppSubscriptionOperationsCounterFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "increment_by": {"type": "Int", "value": increment_by},
            "kind": {"type": "String", "value": kind},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppSubscriptionOperationsCounterFields(
            field_name="increase_app_subscription_operations",
            arguments=cleared_arguments,
        )

    @classmethod
    def move_item_to_board(
        cls,
        board_id: str,
        group_id: str,
        item_id: str,
        *,
        columns_mapping: Optional[ColumnMappingInput] = None,
        subitems_columns_mapping: Optional[ColumnMappingInput] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "columns_mapping": {"type": "ColumnMappingInput", "value": columns_mapping},
            "group_id": {"type": "ID!", "value": group_id},
            "item_id": {"type": "ID!", "value": item_id},
            "subitems_columns_mapping": {
                "type": "ColumnMappingInput",
                "value": subitems_columns_mapping,
            },
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="move_item_to_board", arguments=cleared_arguments)

    @classmethod
    def move_item_to_group(
        cls, group_id: str, *, item_id: Optional[str] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "group_id": {"type": "String!", "value": group_id},
            "item_id": {"type": "ID", "value": item_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="move_item_to_group", arguments=cleared_arguments)

    @classmethod
    def remove_mock_app_subscription(
        cls, app_id: str, partial_signing_secret: str
    ) -> AppSubscriptionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_id": {"type": "ID!", "value": app_id},
            "partial_signing_secret": {
                "type": "String!",
                "value": partial_signing_secret,
            },
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppSubscriptionFields(
            field_name="remove_mock_app_subscription", arguments=cleared_arguments
        )

    @classmethod
    def remove_users_from_team(
        cls, team_id: str, user_ids: str
    ) -> ChangeTeamMembershipsResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "team_id": {"type": "ID!", "value": team_id},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ChangeTeamMembershipsResultFields(
            field_name="remove_users_from_team", arguments=cleared_arguments
        )

    @classmethod
    def set_mock_app_subscription(
        cls,
        app_id: str,
        partial_signing_secret: str,
        *,
        billing_period: Optional[str] = None,
        is_trial: Optional[bool] = None,
        plan_id: Optional[str] = None,
        pricing_version: Optional[int] = None,
        renewal_date: Optional[Any] = None
    ) -> AppSubscriptionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_id": {"type": "ID!", "value": app_id},
            "billing_period": {"type": "String", "value": billing_period},
            "is_trial": {"type": "Boolean", "value": is_trial},
            "partial_signing_secret": {
                "type": "String!",
                "value": partial_signing_secret,
            },
            "plan_id": {"type": "String", "value": plan_id},
            "pricing_version": {"type": "Int", "value": pricing_version},
            "renewal_date": {"type": "Date", "value": renewal_date},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppSubscriptionFields(
            field_name="set_mock_app_subscription", arguments=cleared_arguments
        )

    @classmethod
    def update_board(
        cls, board_attribute: BoardAttributes, board_id: str, new_value: str
    ) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_attribute": {"type": "BoardAttributes!", "value": board_attribute},
            "board_id": {"type": "ID!", "value": board_id},
            "new_value": {"type": "String!", "value": new_value},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(field_name="update_board", arguments=cleared_arguments)

    @classmethod
    def update_doc_block(cls, block_id: str, content: Any) -> DocumentBlockFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "block_id": {"type": "String!", "value": block_id},
            "content": {"type": "JSON!", "value": content},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentBlockFields(
            field_name="update_doc_block", arguments=cleared_arguments
        )

    @classmethod
    def update_folder(
        cls,
        folder_id: str,
        *,
        color: Optional[FolderColor] = None,
        custom_icon: Optional[FolderCustomIcon] = None,
        font_weight: Optional[FolderFontWeight] = None,
        name: Optional[str] = None,
        parent_folder_id: Optional[str] = None
    ) -> FolderFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "color": {"type": "FolderColor", "value": color},
            "custom_icon": {"type": "FolderCustomIcon", "value": custom_icon},
            "folder_id": {"type": "ID!", "value": folder_id},
            "font_weight": {"type": "FolderFontWeight", "value": font_weight},
            "name": {"type": "String", "value": name},
            "parent_folder_id": {"type": "ID", "value": parent_folder_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FolderFields(field_name="update_folder", arguments=cleared_arguments)

    @classmethod
    def update_group(
        cls,
        board_id: str,
        group_attribute: GroupAttributes,
        group_id: str,
        new_value: str,
    ) -> GroupFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "group_attribute": {"type": "GroupAttributes!", "value": group_attribute},
            "group_id": {"type": "String!", "value": group_id},
            "new_value": {"type": "String!", "value": new_value},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GroupFields(field_name="update_group", arguments=cleared_arguments)

    @classmethod
    def update_workspace(
        cls, attributes: UpdateWorkspaceAttributesInput, *, id: Optional[str] = None
    ) -> WorkspaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "attributes": {
                "type": "UpdateWorkspaceAttributesInput!",
                "value": attributes,
            },
            "id": {"type": "ID", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkspaceFields(
            field_name="update_workspace", arguments=cleared_arguments
        )

    @classmethod
    def use_template(
        cls,
        template_id: int,
        *,
        board_kind: Optional[BoardKind] = None,
        board_owner_ids: Optional[int] = None,
        board_owner_team_ids: Optional[int] = None,
        board_subscriber_ids: Optional[int] = None,
        board_subscriber_teams_ids: Optional[int] = None,
        callback_url_on_complete: Optional[str] = None,
        destination_folder_id: Optional[int] = None,
        destination_folder_name: Optional[str] = None,
        destination_name: Optional[str] = None,
        destination_workspace_id: Optional[int] = None,
        skip_target_folder_creation: Optional[bool] = None,
        solution_extra_options: Optional[Any] = None
    ) -> TemplateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_kind": {"type": "BoardKind", "value": board_kind},
            "board_owner_ids": {"type": "Int", "value": board_owner_ids},
            "board_owner_team_ids": {"type": "Int", "value": board_owner_team_ids},
            "board_subscriber_ids": {"type": "Int", "value": board_subscriber_ids},
            "board_subscriber_teams_ids": {
                "type": "Int",
                "value": board_subscriber_teams_ids,
            },
            "callback_url_on_complete": {
                "type": "String",
                "value": callback_url_on_complete,
            },
            "destination_folder_id": {"type": "Int", "value": destination_folder_id},
            "destination_folder_name": {
                "type": "String",
                "value": destination_folder_name,
            },
            "destination_name": {"type": "String", "value": destination_name},
            "destination_workspace_id": {
                "type": "Int",
                "value": destination_workspace_id,
            },
            "skip_target_folder_creation": {
                "type": "Boolean",
                "value": skip_target_folder_creation,
            },
            "solution_extra_options": {"type": "JSON", "value": solution_extra_options},
            "template_id": {"type": "Int!", "value": template_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TemplateFields(field_name="use_template", arguments=cleared_arguments)

    @classmethod
    def create_team(
        cls,
        input: CreateTeamAttributesInput,
        *,
        options: Optional[CreateTeamOptionsInput] = None
    ) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CreateTeamAttributesInput!", "value": input},
            "options": {"type": "CreateTeamOptionsInput", "value": options},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(field_name="create_team", arguments=cleared_arguments)

    @classmethod
    def activate_users(cls, user_ids: str) -> ActivateUsersResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "user_ids": {"type": "ID!", "value": user_ids}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ActivateUsersResultFields(
            field_name="activate_users", arguments=cleared_arguments
        )

    @classmethod
    def deactivate_users(cls, user_ids: str) -> DeactivateUsersResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "user_ids": {"type": "ID!", "value": user_ids}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeactivateUsersResultFields(
            field_name="deactivate_users", arguments=cleared_arguments
        )

    @classmethod
    def delete_team(cls, team_id: str) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "team_id": {"type": "ID!", "value": team_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(field_name="delete_team", arguments=cleared_arguments)

    @classmethod
    def update_users_role(
        cls, user_ids: str, new_role: BaseRoleName
    ) -> UpdateUsersRoleResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "user_ids": {"type": "ID!", "value": user_ids},
            "new_role": {"type": "BaseRoleName!", "value": new_role},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateUsersRoleResultFields(
            field_name="update_users_role", arguments=cleared_arguments
        )

    @classmethod
    def assign_team_owners(
        cls, team_id: str, user_ids: str
    ) -> AssignTeamOwnersResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "team_id": {"type": "ID!", "value": team_id},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AssignTeamOwnersResultFields(
            field_name="assign_team_owners", arguments=cleared_arguments
        )

    @classmethod
    def remove_team_owners(
        cls, team_id: str, user_ids: str
    ) -> RemoveTeamOwnersResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "team_id": {"type": "ID!", "value": team_id},
            "user_ids": {"type": "ID!", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RemoveTeamOwnersResultFields(
            field_name="remove_team_owners", arguments=cleared_arguments
        )

    @classmethod
    def update_email_domain(
        cls, input: UpdateEmailDomainAttributesInput
    ) -> UpdateEmailDomainResultFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "UpdateEmailDomainAttributesInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateEmailDomainResultFields(
            field_name="update_email_domain", arguments=cleared_arguments
        )
