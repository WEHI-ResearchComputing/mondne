from typing import Any, Dict, Optional

from . import (
    BoardKind,
    BoardsOrderBy,
    CustomActivityColor,
    CustomActivityIcon,
    DocsOrderBy,
    State,
    SubscriptionStatus,
    UserKind,
    WorkspaceKind,
    WorkspacesOrderBy,
)
from .custom_fields import (
    AccountFields,
    AppInstallFields,
    AppMonetizationStatusFields,
    AppsMonetizationInfoFields,
    AppSubscriptionFields,
    AppSubscriptionOperationsCounterFields,
    AppSubscriptionsFields,
    AppTypeFields,
    AssetFields,
    BoardFields,
    ComplexityFields,
    CustomActivityFields,
    DocumentFields,
    FolderFields,
    ItemFields,
    ItemsResponseFields,
    MarketplaceAppDiscountFields,
    TagFields,
    TeamFields,
    TimelineItemFields,
    TimelineResponseFields,
    UpdateFields,
    UserFields,
    VersionFields,
    WebhookFields,
    WorkspaceFields,
)
from .input_types import ItemsPageByColumnValuesQuery


class Query:
    @classmethod
    def updates(
        cls,
        *,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        ids: Optional[str] = None
    ) -> UpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
            "ids": {"type": "ID", "value": ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields(field_name="updates", arguments=cleared_arguments)

    @classmethod
    def custom_activity(
        cls,
        *,
        ids: Optional[str] = None,
        name: Optional[str] = None,
        icon_id: Optional[CustomActivityIcon] = None,
        color: Optional[CustomActivityColor] = None
    ) -> CustomActivityFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "String", "value": ids},
            "name": {"type": "String", "value": name},
            "icon_id": {"type": "CustomActivityIcon", "value": icon_id},
            "color": {"type": "CustomActivityColor", "value": color},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomActivityFields(
            field_name="custom_activity", arguments=cleared_arguments
        )

    @classmethod
    def timeline_item(cls, id: str) -> TimelineItemFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "ID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimelineItemFields(
            field_name="timeline_item", arguments=cleared_arguments
        )

    @classmethod
    def timeline(cls, id: str) -> TimelineResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "ID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimelineResponseFields(
            field_name="timeline", arguments=cleared_arguments
        )

    @classmethod
    def marketplace_app_discounts(cls, app_id: str) -> MarketplaceAppDiscountFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_id": {"type": "ID!", "value": app_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return MarketplaceAppDiscountFields(
            field_name="marketplace_app_discounts", arguments=cleared_arguments
        )

    @classmethod
    def app_subscriptions(
        cls,
        app_id: str,
        *,
        status: Optional[SubscriptionStatus] = None,
        account_id: Optional[int] = None,
        cursor: Optional[str] = None,
        limit: Optional[int] = None
    ) -> AppSubscriptionsFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_id": {"type": "ID!", "value": app_id},
            "status": {"type": "SubscriptionStatus", "value": status},
            "account_id": {"type": "Int", "value": account_id},
            "cursor": {"type": "String", "value": cursor},
            "limit": {"type": "Int", "value": limit},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppSubscriptionsFields(
            field_name="app_subscriptions", arguments=cleared_arguments
        )

    @classmethod
    def app(cls, id: str) -> AppTypeFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "ID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppTypeFields(field_name="app", arguments=cleared_arguments)

    @classmethod
    def account(cls) -> AccountFields:
        return AccountFields(field_name="account")

    @classmethod
    def app_installs(
        cls,
        app_id: str,
        *,
        account_id: Optional[str] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None
    ) -> AppInstallFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "account_id": {"type": "ID", "value": account_id},
            "app_id": {"type": "ID!", "value": app_id},
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppInstallFields(field_name="app_installs", arguments=cleared_arguments)

    @classmethod
    def app_subscription(cls) -> AppSubscriptionFields:
        return AppSubscriptionFields(field_name="app_subscription")

    @classmethod
    def app_subscription_operations(
        cls, *, kind: Optional[str] = None
    ) -> AppSubscriptionOperationsCounterFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "kind": {"type": "String", "value": kind}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AppSubscriptionOperationsCounterFields(
            field_name="app_subscription_operations", arguments=cleared_arguments
        )

    @classmethod
    def apps_monetization_info(cls) -> AppsMonetizationInfoFields:
        return AppsMonetizationInfoFields(field_name="apps_monetization_info")

    @classmethod
    def apps_monetization_status(cls) -> AppMonetizationStatusFields:
        return AppMonetizationStatusFields(field_name="apps_monetization_status")

    @classmethod
    def assets(cls, ids: str) -> AssetFields:
        arguments: Dict[str, Dict[str, Any]] = {"ids": {"type": "ID!", "value": ids}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AssetFields(field_name="assets", arguments=cleared_arguments)

    @classmethod
    def boards(
        cls,
        *,
        board_kind: Optional[BoardKind] = None,
        ids: Optional[str] = None,
        limit: Optional[int] = None,
        order_by: Optional[BoardsOrderBy] = None,
        page: Optional[int] = None,
        state: Optional[State] = None,
        workspace_ids: Optional[str] = None
    ) -> BoardFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_kind": {"type": "BoardKind", "value": board_kind},
            "ids": {"type": "ID", "value": ids},
            "limit": {"type": "Int", "value": limit},
            "order_by": {"type": "BoardsOrderBy", "value": order_by},
            "page": {"type": "Int", "value": page},
            "state": {"type": "State", "value": state},
            "workspace_ids": {"type": "ID", "value": workspace_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BoardFields(field_name="boards", arguments=cleared_arguments)

    @classmethod
    def complexity(cls) -> ComplexityFields:
        return ComplexityFields(field_name="complexity")

    @classmethod
    def docs(
        cls,
        *,
        ids: Optional[str] = None,
        limit: Optional[int] = None,
        object_ids: Optional[str] = None,
        order_by: Optional[DocsOrderBy] = None,
        page: Optional[int] = None,
        workspace_ids: Optional[str] = None
    ) -> DocumentFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "ID", "value": ids},
            "limit": {"type": "Int", "value": limit},
            "object_ids": {"type": "ID", "value": object_ids},
            "order_by": {"type": "DocsOrderBy", "value": order_by},
            "page": {"type": "Int", "value": page},
            "workspace_ids": {"type": "ID", "value": workspace_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentFields(field_name="docs", arguments=cleared_arguments)

    @classmethod
    def folders(
        cls,
        *,
        ids: Optional[str] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        workspace_ids: Optional[str] = None
    ) -> FolderFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "ID", "value": ids},
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
            "workspace_ids": {"type": "ID", "value": workspace_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FolderFields(field_name="folders", arguments=cleared_arguments)

    @classmethod
    def items(
        cls,
        *,
        exclude_nonactive: Optional[bool] = None,
        ids: Optional[str] = None,
        limit: Optional[int] = None,
        newest_first: Optional[bool] = None,
        page: Optional[int] = None
    ) -> ItemFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "exclude_nonactive": {"type": "Boolean", "value": exclude_nonactive},
            "ids": {"type": "ID", "value": ids},
            "limit": {"type": "Int", "value": limit},
            "newest_first": {"type": "Boolean", "value": newest_first},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields(field_name="items", arguments=cleared_arguments)

    @classmethod
    def items_page_by_column_values(
        cls,
        board_id: str,
        limit: int,
        *,
        columns: Optional[ItemsPageByColumnValuesQuery] = None,
        cursor: Optional[str] = None
    ) -> ItemsResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "board_id": {"type": "ID!", "value": board_id},
            "columns": {"type": "ItemsPageByColumnValuesQuery", "value": columns},
            "cursor": {"type": "String", "value": cursor},
            "limit": {"type": "Int!", "value": limit},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemsResponseFields(
            field_name="items_page_by_column_values", arguments=cleared_arguments
        )

    @classmethod
    def me(cls) -> UserFields:
        return UserFields(field_name="me")

    @classmethod
    def next_items_page(cls, cursor: str, limit: int) -> ItemsResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "cursor": {"type": "String!", "value": cursor},
            "limit": {"type": "Int!", "value": limit},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemsResponseFields(
            field_name="next_items_page", arguments=cleared_arguments
        )

    @classmethod
    def tags(cls, *, ids: Optional[str] = None) -> TagFields:
        arguments: Dict[str, Dict[str, Any]] = {"ids": {"type": "ID", "value": ids}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TagFields(field_name="tags", arguments=cleared_arguments)

    @classmethod
    def teams(cls, *, ids: Optional[str] = None) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {"ids": {"type": "ID", "value": ids}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(field_name="teams", arguments=cleared_arguments)

    @classmethod
    def users(
        cls,
        *,
        emails: Optional[str] = None,
        ids: Optional[str] = None,
        kind: Optional[UserKind] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        newest_first: Optional[bool] = None,
        non_active: Optional[bool] = None,
        page: Optional[int] = None
    ) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "emails": {"type": "String", "value": emails},
            "ids": {"type": "ID", "value": ids},
            "kind": {"type": "UserKind", "value": kind},
            "limit": {"type": "Int", "value": limit},
            "name": {"type": "String", "value": name},
            "newest_first": {"type": "Boolean", "value": newest_first},
            "non_active": {"type": "Boolean", "value": non_active},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="users", arguments=cleared_arguments)

    @classmethod
    def version(cls) -> VersionFields:
        return VersionFields(field_name="version")

    @classmethod
    def versions(cls) -> VersionFields:
        return VersionFields(field_name="versions")

    @classmethod
    def webhooks(
        cls, board_id: str, *, app_webhooks_only: Optional[bool] = None
    ) -> WebhookFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "app_webhooks_only": {"type": "Boolean", "value": app_webhooks_only},
            "board_id": {"type": "ID!", "value": board_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookFields(field_name="webhooks", arguments=cleared_arguments)

    @classmethod
    def workspaces(
        cls,
        *,
        ids: Optional[str] = None,
        kind: Optional[WorkspaceKind] = None,
        limit: Optional[int] = None,
        order_by: Optional[WorkspacesOrderBy] = None,
        page: Optional[int] = None,
        state: Optional[State] = None
    ) -> WorkspaceFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "ID", "value": ids},
            "kind": {"type": "WorkspaceKind", "value": kind},
            "limit": {"type": "Int", "value": limit},
            "order_by": {"type": "WorkspacesOrderBy", "value": order_by},
            "page": {"type": "Int", "value": page},
            "state": {"type": "State", "value": state},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkspaceFields(field_name="workspaces", arguments=cleared_arguments)
