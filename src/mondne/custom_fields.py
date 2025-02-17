from typing import Any, Dict, Optional, Union

from . import AssetsSource, ColumnType, UserKind
from .base_operation import GraphQLField
from .custom_typing_fields import (
    AccountGraphQLField,
    AccountProductGraphQLField,
    ActivateUsersErrorGraphQLField,
    ActivateUsersResultGraphQLField,
    ActivityLogTypeGraphQLField,
    AppInstallAccountGraphQLField,
    AppInstallGraphQLField,
    AppInstallPermissionsGraphQLField,
    AppInstallUserGraphQLField,
    AppMonetizationStatusGraphQLField,
    AppsMonetizationInfoGraphQLField,
    AppSubscriptionDetailsGraphQLField,
    AppSubscriptionGraphQLField,
    AppSubscriptionOperationsCounterGraphQLField,
    AppSubscriptionsGraphQLField,
    AppTypeGraphQLField,
    AppVersionGraphQLField,
    AssetGraphQLField,
    AssignTeamOwnersErrorGraphQLField,
    AssignTeamOwnersResultGraphQLField,
    BatchExtendTrialPeriodGraphQLField,
    BoardDuplicationGraphQLField,
    BoardGraphQLField,
    BoardViewGraphQLField,
    ChangeTeamMembershipsResultGraphQLField,
    ColumnGraphQLField,
    ComplexityGraphQLField,
    CustomActivityGraphQLField,
    CustomFieldMetasGraphQLField,
    CustomFieldValueGraphQLField,
    DeactivateUsersErrorGraphQLField,
    DeactivateUsersResultGraphQLField,
    DeleteMarketplaceAppDiscountGraphQLField,
    DeleteMarketplaceAppDiscountResultGraphQLField,
    DocumentBlockGraphQLField,
    DocumentBlockIdOnlyGraphQLField,
    DocumentGraphQLField,
    ExtendTrialPeriodGraphQLField,
    FolderGraphQLField,
    GrantMarketplaceAppDiscountGraphQLField,
    GrantMarketplaceAppDiscountResultGraphQLField,
    GroupGraphQLField,
    ItemGraphQLField,
    ItemsResponseGraphQLField,
    LikeGraphQLField,
    MarketplaceAppDiscountGraphQLField,
    NotificationGraphQLField,
    OutOfOfficeGraphQLField,
    PlanGraphQLField,
    RemoveTeamOwnersErrorGraphQLField,
    RemoveTeamOwnersResultGraphQLField,
    ReplyGraphQLField,
    SubscriptionDiscountGraphQLField,
    TagGraphQLField,
    TeamGraphQLField,
    TemplateGraphQLField,
    TimelineItemGraphQLField,
    TimelineItemsPageGraphQLField,
    TimelineResponseGraphQLField,
    UpdateEmailDomainErrorGraphQLField,
    UpdateEmailDomainResultGraphQLField,
    UpdateGraphQLField,
    UpdatePinGraphQLField,
    UpdateUsersRoleErrorGraphQLField,
    UpdateUsersRoleResultGraphQLField,
    UserGraphQLField,
    VersionGraphQLField,
    WatcherGraphQLField,
    WebhookGraphQLField,
    WorkspaceGraphQLField,
    WorkspaceIconGraphQLField,
    WorkspaceSettingsGraphQLField,
)
from .input_types import ItemsQuery


class AccountFields(GraphQLField):
    active_members_count: "AccountGraphQLField" = AccountGraphQLField(
        "active_members_count"
    )
    country_code: "AccountGraphQLField" = AccountGraphQLField("country_code")
    first_day_of_the_week: "AccountGraphQLField" = AccountGraphQLField(
        "first_day_of_the_week"
    )
    id: "AccountGraphQLField" = AccountGraphQLField("id")
    logo: "AccountGraphQLField" = AccountGraphQLField("logo")
    name: "AccountGraphQLField" = AccountGraphQLField("name")

    @classmethod
    def plan(cls) -> "PlanFields":
        return PlanFields("plan")

    @classmethod
    def products(cls) -> "AccountProductFields":
        return AccountProductFields("products")

    show_timeline_weekends: "AccountGraphQLField" = AccountGraphQLField(
        "show_timeline_weekends"
    )
    sign_up_product_kind: "AccountGraphQLField" = AccountGraphQLField(
        "sign_up_product_kind"
    )
    slug: "AccountGraphQLField" = AccountGraphQLField("slug")
    tier: "AccountGraphQLField" = AccountGraphQLField("tier")

    def fields(
        self,
        *subfields: Union[AccountGraphQLField, "AccountProductFields", "PlanFields"]
    ) -> "AccountFields":
        """Subfields should come from the AccountFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AccountFields":
        self._alias = alias
        return self


class AccountProductFields(GraphQLField):
    default_workspace_id: "AccountProductGraphQLField" = AccountProductGraphQLField(
        "default_workspace_id"
    )
    id: "AccountProductGraphQLField" = AccountProductGraphQLField("id")
    kind: "AccountProductGraphQLField" = AccountProductGraphQLField("kind")

    def fields(self, *subfields: AccountProductGraphQLField) -> "AccountProductFields":
        """Subfields should come from the AccountProductFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AccountProductFields":
        self._alias = alias
        return self


class ActivateUsersErrorFields(GraphQLField):
    message: "ActivateUsersErrorGraphQLField" = ActivateUsersErrorGraphQLField(
        "message"
    )
    code: "ActivateUsersErrorGraphQLField" = ActivateUsersErrorGraphQLField("code")
    user_id: "ActivateUsersErrorGraphQLField" = ActivateUsersErrorGraphQLField(
        "user_id"
    )

    def fields(
        self, *subfields: ActivateUsersErrorGraphQLField
    ) -> "ActivateUsersErrorFields":
        """Subfields should come from the ActivateUsersErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ActivateUsersErrorFields":
        self._alias = alias
        return self


class ActivateUsersResultFields(GraphQLField):
    @classmethod
    def activated_users(cls) -> "UserFields":
        return UserFields("activated_users")

    @classmethod
    def errors(cls) -> "ActivateUsersErrorFields":
        return ActivateUsersErrorFields("errors")

    def fields(
        self,
        *subfields: Union[
            ActivateUsersResultGraphQLField, "ActivateUsersErrorFields", "UserFields"
        ]
    ) -> "ActivateUsersResultFields":
        """Subfields should come from the ActivateUsersResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ActivateUsersResultFields":
        self._alias = alias
        return self


class ActivityLogTypeFields(GraphQLField):
    account_id: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField(
        "account_id"
    )
    created_at: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField(
        "created_at"
    )
    data: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField("data")
    entity: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField("entity")
    event: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField("event")
    id: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField("id")
    user_id: "ActivityLogTypeGraphQLField" = ActivityLogTypeGraphQLField("user_id")

    def fields(
        self, *subfields: ActivityLogTypeGraphQLField
    ) -> "ActivityLogTypeFields":
        """Subfields should come from the ActivityLogTypeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ActivityLogTypeFields":
        self._alias = alias
        return self


class AppInstallFields(GraphQLField):
    app_id: "AppInstallGraphQLField" = AppInstallGraphQLField("app_id")

    @classmethod
    def app_install_account(cls) -> "AppInstallAccountFields":
        return AppInstallAccountFields("app_install_account")

    @classmethod
    def app_install_user(cls) -> "AppInstallUserFields":
        return AppInstallUserFields("app_install_user")

    @classmethod
    def app_version(cls) -> "AppVersionFields":
        return AppVersionFields("app_version")

    @classmethod
    def permissions(cls) -> "AppInstallPermissionsFields":
        return AppInstallPermissionsFields("permissions")

    timestamp: "AppInstallGraphQLField" = AppInstallGraphQLField("timestamp")

    def fields(
        self,
        *subfields: Union[
            AppInstallGraphQLField,
            "AppInstallAccountFields",
            "AppInstallPermissionsFields",
            "AppInstallUserFields",
            "AppVersionFields",
        ]
    ) -> "AppInstallFields":
        """Subfields should come from the AppInstallFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppInstallFields":
        self._alias = alias
        return self


class AppInstallAccountFields(GraphQLField):
    id: "AppInstallAccountGraphQLField" = AppInstallAccountGraphQLField("id")

    def fields(
        self, *subfields: AppInstallAccountGraphQLField
    ) -> "AppInstallAccountFields":
        """Subfields should come from the AppInstallAccountFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppInstallAccountFields":
        self._alias = alias
        return self


class AppInstallPermissionsFields(GraphQLField):
    approved_scopes: "AppInstallPermissionsGraphQLField" = (
        AppInstallPermissionsGraphQLField("approved_scopes")
    )
    required_scopes: "AppInstallPermissionsGraphQLField" = (
        AppInstallPermissionsGraphQLField("required_scopes")
    )

    def fields(
        self, *subfields: AppInstallPermissionsGraphQLField
    ) -> "AppInstallPermissionsFields":
        """Subfields should come from the AppInstallPermissionsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppInstallPermissionsFields":
        self._alias = alias
        return self


class AppInstallUserFields(GraphQLField):
    id: "AppInstallUserGraphQLField" = AppInstallUserGraphQLField("id")

    def fields(self, *subfields: AppInstallUserGraphQLField) -> "AppInstallUserFields":
        """Subfields should come from the AppInstallUserFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppInstallUserFields":
        self._alias = alias
        return self


class AppMonetizationStatusFields(GraphQLField):
    is_supported: "AppMonetizationStatusGraphQLField" = (
        AppMonetizationStatusGraphQLField("is_supported")
    )

    def fields(
        self, *subfields: AppMonetizationStatusGraphQLField
    ) -> "AppMonetizationStatusFields":
        """Subfields should come from the AppMonetizationStatusFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppMonetizationStatusFields":
        self._alias = alias
        return self


class AppSubscriptionFields(GraphQLField):
    billing_period: "AppSubscriptionGraphQLField" = AppSubscriptionGraphQLField(
        "billing_period"
    )
    days_left: "AppSubscriptionGraphQLField" = AppSubscriptionGraphQLField("days_left")
    is_trial: "AppSubscriptionGraphQLField" = AppSubscriptionGraphQLField("is_trial")
    plan_id: "AppSubscriptionGraphQLField" = AppSubscriptionGraphQLField("plan_id")
    pricing_version: "AppSubscriptionGraphQLField" = AppSubscriptionGraphQLField(
        "pricing_version"
    )
    renewal_date: "AppSubscriptionGraphQLField" = AppSubscriptionGraphQLField(
        "renewal_date"
    )

    def fields(
        self, *subfields: AppSubscriptionGraphQLField
    ) -> "AppSubscriptionFields":
        """Subfields should come from the AppSubscriptionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppSubscriptionFields":
        self._alias = alias
        return self


class AppSubscriptionDetailsFields(GraphQLField):
    account_id: "AppSubscriptionDetailsGraphQLField" = (
        AppSubscriptionDetailsGraphQLField("account_id")
    )
    plan_id: "AppSubscriptionDetailsGraphQLField" = AppSubscriptionDetailsGraphQLField(
        "plan_id"
    )
    pricing_version_id: "AppSubscriptionDetailsGraphQLField" = (
        AppSubscriptionDetailsGraphQLField("pricing_version_id")
    )
    monthly_price: "AppSubscriptionDetailsGraphQLField" = (
        AppSubscriptionDetailsGraphQLField("monthly_price")
    )
    currency: "AppSubscriptionDetailsGraphQLField" = AppSubscriptionDetailsGraphQLField(
        "currency"
    )
    period_type: "AppSubscriptionDetailsGraphQLField" = (
        AppSubscriptionDetailsGraphQLField("period_type")
    )
    renewal_date: "AppSubscriptionDetailsGraphQLField" = (
        AppSubscriptionDetailsGraphQLField("renewal_date")
    )
    status: "AppSubscriptionDetailsGraphQLField" = AppSubscriptionDetailsGraphQLField(
        "status"
    )

    @classmethod
    def discounts(cls) -> "SubscriptionDiscountFields":
        return SubscriptionDiscountFields("discounts")

    days_left: "AppSubscriptionDetailsGraphQLField" = (
        AppSubscriptionDetailsGraphQLField("days_left")
    )

    def fields(
        self,
        *subfields: Union[
            AppSubscriptionDetailsGraphQLField, "SubscriptionDiscountFields"
        ]
    ) -> "AppSubscriptionDetailsFields":
        """Subfields should come from the AppSubscriptionDetailsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppSubscriptionDetailsFields":
        self._alias = alias
        return self


class AppSubscriptionOperationsCounterFields(GraphQLField):
    @classmethod
    def app_subscription(cls) -> "AppSubscriptionFields":
        return AppSubscriptionFields("app_subscription")

    counter_value: "AppSubscriptionOperationsCounterGraphQLField" = (
        AppSubscriptionOperationsCounterGraphQLField("counter_value")
    )
    kind: "AppSubscriptionOperationsCounterGraphQLField" = (
        AppSubscriptionOperationsCounterGraphQLField("kind")
    )
    period_key: "AppSubscriptionOperationsCounterGraphQLField" = (
        AppSubscriptionOperationsCounterGraphQLField("period_key")
    )

    def fields(
        self,
        *subfields: Union[
            AppSubscriptionOperationsCounterGraphQLField, "AppSubscriptionFields"
        ]
    ) -> "AppSubscriptionOperationsCounterFields":
        """Subfields should come from the AppSubscriptionOperationsCounterFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppSubscriptionOperationsCounterFields":
        self._alias = alias
        return self


class AppSubscriptionsFields(GraphQLField):
    @classmethod
    def subscriptions(cls) -> "AppSubscriptionDetailsFields":
        return AppSubscriptionDetailsFields("subscriptions")

    total_count: "AppSubscriptionsGraphQLField" = AppSubscriptionsGraphQLField(
        "total_count"
    )
    cursor: "AppSubscriptionsGraphQLField" = AppSubscriptionsGraphQLField("cursor")

    def fields(
        self,
        *subfields: Union[AppSubscriptionsGraphQLField, "AppSubscriptionDetailsFields"]
    ) -> "AppSubscriptionsFields":
        """Subfields should come from the AppSubscriptionsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppSubscriptionsFields":
        self._alias = alias
        return self


class AppTypeFields(GraphQLField):
    id: "AppTypeGraphQLField" = AppTypeGraphQLField("id")
    created_at: "AppTypeGraphQLField" = AppTypeGraphQLField("created_at")
    updated_at: "AppTypeGraphQLField" = AppTypeGraphQLField("updated_at")
    name: "AppTypeGraphQLField" = AppTypeGraphQLField("name")
    api_app_id: "AppTypeGraphQLField" = AppTypeGraphQLField("api_app_id")
    client_id: "AppTypeGraphQLField" = AppTypeGraphQLField("client_id")
    kind: "AppTypeGraphQLField" = AppTypeGraphQLField("kind")
    state: "AppTypeGraphQLField" = AppTypeGraphQLField("state")
    user_id: "AppTypeGraphQLField" = AppTypeGraphQLField("user_id")

    def fields(self, *subfields: AppTypeGraphQLField) -> "AppTypeFields":
        """Subfields should come from the AppTypeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppTypeFields":
        self._alias = alias
        return self


class AppVersionFields(GraphQLField):
    major: "AppVersionGraphQLField" = AppVersionGraphQLField("major")
    minor: "AppVersionGraphQLField" = AppVersionGraphQLField("minor")
    patch: "AppVersionGraphQLField" = AppVersionGraphQLField("patch")
    text: "AppVersionGraphQLField" = AppVersionGraphQLField("text")
    type: "AppVersionGraphQLField" = AppVersionGraphQLField("type")

    def fields(self, *subfields: AppVersionGraphQLField) -> "AppVersionFields":
        """Subfields should come from the AppVersionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppVersionFields":
        self._alias = alias
        return self


class AppsMonetizationInfoFields(GraphQLField):
    seats_count: "AppsMonetizationInfoGraphQLField" = AppsMonetizationInfoGraphQLField(
        "seats_count"
    )

    def fields(
        self, *subfields: AppsMonetizationInfoGraphQLField
    ) -> "AppsMonetizationInfoFields":
        """Subfields should come from the AppsMonetizationInfoFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AppsMonetizationInfoFields":
        self._alias = alias
        return self


class AssetFields(GraphQLField):
    created_at: "AssetGraphQLField" = AssetGraphQLField("created_at")
    file_extension: "AssetGraphQLField" = AssetGraphQLField("file_extension")
    file_size: "AssetGraphQLField" = AssetGraphQLField("file_size")
    id: "AssetGraphQLField" = AssetGraphQLField("id")
    name: "AssetGraphQLField" = AssetGraphQLField("name")
    original_geometry: "AssetGraphQLField" = AssetGraphQLField("original_geometry")
    public_url: "AssetGraphQLField" = AssetGraphQLField("public_url")

    @classmethod
    def uploaded_by(cls) -> "UserFields":
        return UserFields("uploaded_by")

    url: "AssetGraphQLField" = AssetGraphQLField("url")
    url_thumbnail: "AssetGraphQLField" = AssetGraphQLField("url_thumbnail")

    def fields(
        self, *subfields: Union[AssetGraphQLField, "UserFields"]
    ) -> "AssetFields":
        """Subfields should come from the AssetFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AssetFields":
        self._alias = alias
        return self


class AssignTeamOwnersErrorFields(GraphQLField):
    message: "AssignTeamOwnersErrorGraphQLField" = AssignTeamOwnersErrorGraphQLField(
        "message"
    )
    code: "AssignTeamOwnersErrorGraphQLField" = AssignTeamOwnersErrorGraphQLField(
        "code"
    )
    user_id: "AssignTeamOwnersErrorGraphQLField" = AssignTeamOwnersErrorGraphQLField(
        "user_id"
    )

    def fields(
        self, *subfields: AssignTeamOwnersErrorGraphQLField
    ) -> "AssignTeamOwnersErrorFields":
        """Subfields should come from the AssignTeamOwnersErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AssignTeamOwnersErrorFields":
        self._alias = alias
        return self


class AssignTeamOwnersResultFields(GraphQLField):
    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def errors(cls) -> "AssignTeamOwnersErrorFields":
        return AssignTeamOwnersErrorFields("errors")

    def fields(
        self,
        *subfields: Union[
            AssignTeamOwnersResultGraphQLField,
            "AssignTeamOwnersErrorFields",
            "TeamFields",
        ]
    ) -> "AssignTeamOwnersResultFields":
        """Subfields should come from the AssignTeamOwnersResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AssignTeamOwnersResultFields":
        self._alias = alias
        return self


class BatchExtendTrialPeriodFields(GraphQLField):
    @classmethod
    def details(cls) -> "ExtendTrialPeriodFields":
        return ExtendTrialPeriodFields("details")

    reason: "BatchExtendTrialPeriodGraphQLField" = BatchExtendTrialPeriodGraphQLField(
        "reason"
    )
    success: "BatchExtendTrialPeriodGraphQLField" = BatchExtendTrialPeriodGraphQLField(
        "success"
    )

    def fields(
        self,
        *subfields: Union[BatchExtendTrialPeriodGraphQLField, "ExtendTrialPeriodFields"]
    ) -> "BatchExtendTrialPeriodFields":
        """Subfields should come from the BatchExtendTrialPeriodFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "BatchExtendTrialPeriodFields":
        self._alias = alias
        return self


class BoardFields(GraphQLField):
    id: "BoardGraphQLField" = BoardGraphQLField("id")

    @classmethod
    def updates(
        cls,
        *,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        ids: Optional[str] = None
    ) -> "UpdateFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
            "ids": {"type": "ID", "value": ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields("updates", arguments=cleared_arguments)

    @classmethod
    def activity_logs(
        cls,
        *,
        column_ids: Optional[str] = None,
        from_: Optional[Any] = None,
        group_ids: Optional[str] = None,
        item_ids: Optional[str] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        to: Optional[Any] = None,
        user_ids: Optional[str] = None
    ) -> "ActivityLogTypeFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "column_ids": {"type": "String", "value": column_ids},
            "from": {"type": "ISO8601DateTime", "value": from_},
            "group_ids": {"type": "String", "value": group_ids},
            "item_ids": {"type": "ID", "value": item_ids},
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
            "to": {"type": "ISO8601DateTime", "value": to},
            "user_ids": {"type": "ID", "value": user_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ActivityLogTypeFields("activity_logs", arguments=cleared_arguments)

    board_folder_id: "BoardGraphQLField" = BoardGraphQLField("board_folder_id")
    board_kind: "BoardGraphQLField" = BoardGraphQLField("board_kind")

    @classmethod
    def collaborators(cls) -> "UserFields":
        return UserFields("collaborators")

    @classmethod
    def columns(
        cls, *, ids: Optional[str] = None, types: Optional[ColumnType] = None
    ) -> "ColumnFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "String", "value": ids},
            "types": {"type": "ColumnType", "value": types},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ColumnFields("columns", arguments=cleared_arguments)

    communication: "BoardGraphQLField" = BoardGraphQLField("communication")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    description: "BoardGraphQLField" = BoardGraphQLField("description")

    @classmethod
    def groups(cls, *, ids: Optional[str] = None) -> "GroupFields":
        arguments: Dict[str, Dict[str, Any]] = {"ids": {"type": "String", "value": ids}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GroupFields("groups", arguments=cleared_arguments)

    item_terminology: "BoardGraphQLField" = BoardGraphQLField("item_terminology")
    items_count: "BoardGraphQLField" = BoardGraphQLField("items_count")

    @classmethod
    def items_page(
        cls,
        limit: int,
        *,
        cursor: Optional[str] = None,
        query_params: Optional[ItemsQuery] = None
    ) -> "ItemsResponseFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "cursor": {"type": "String", "value": cursor},
            "limit": {"type": "Int!", "value": limit},
            "query_params": {"type": "ItemsQuery", "value": query_params},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemsResponseFields("items_page", arguments=cleared_arguments)

    name: "BoardGraphQLField" = BoardGraphQLField("name")

    @classmethod
    def owner(cls) -> "UserFields":
        return UserFields("owner")

    @classmethod
    def owners(cls) -> "UserFields":
        return UserFields("owners")

    permissions: "BoardGraphQLField" = BoardGraphQLField("permissions")
    state: "BoardGraphQLField" = BoardGraphQLField("state")

    @classmethod
    def subscribers(cls) -> "UserFields":
        return UserFields("subscribers")

    @classmethod
    def tags(cls) -> "TagFields":
        return TagFields("tags")

    @classmethod
    def team_owners(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "TeamFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields("team_owners", arguments=cleared_arguments)

    @classmethod
    def team_subscribers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "TeamFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields("team_subscribers", arguments=cleared_arguments)

    @classmethod
    def top_group(cls) -> "GroupFields":
        return GroupFields("top_group")

    type: "BoardGraphQLField" = BoardGraphQLField("type")
    updated_at: "BoardGraphQLField" = BoardGraphQLField("updated_at")
    url: "BoardGraphQLField" = BoardGraphQLField("url")

    @classmethod
    def views(
        cls, *, ids: Optional[str] = None, type: Optional[str] = None
    ) -> "BoardViewFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "ID", "value": ids},
            "type": {"type": "String", "value": type},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return BoardViewFields("views", arguments=cleared_arguments)

    @classmethod
    def workspace(cls) -> "WorkspaceFields":
        return WorkspaceFields("workspace")

    workspace_id: "BoardGraphQLField" = BoardGraphQLField("workspace_id")

    def fields(
        self,
        *subfields: Union[
            BoardGraphQLField,
            "ActivityLogTypeFields",
            "BoardViewFields",
            "ColumnFields",
            "GroupFields",
            "ItemsResponseFields",
            "TagFields",
            "TeamFields",
            "UpdateFields",
            "UserFields",
            "WorkspaceFields",
        ]
    ) -> "BoardFields":
        """Subfields should come from the BoardFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "BoardFields":
        self._alias = alias
        return self


class BoardDuplicationFields(GraphQLField):
    @classmethod
    def board(cls) -> "BoardFields":
        return BoardFields("board")

    is_async: "BoardDuplicationGraphQLField" = BoardDuplicationGraphQLField("is_async")

    def fields(
        self, *subfields: Union[BoardDuplicationGraphQLField, "BoardFields"]
    ) -> "BoardDuplicationFields":
        """Subfields should come from the BoardDuplicationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "BoardDuplicationFields":
        self._alias = alias
        return self


class BoardViewFields(GraphQLField):
    id: "BoardViewGraphQLField" = BoardViewGraphQLField("id")
    name: "BoardViewGraphQLField" = BoardViewGraphQLField("name")
    settings_str: "BoardViewGraphQLField" = BoardViewGraphQLField("settings_str")
    source_view_id: "BoardViewGraphQLField" = BoardViewGraphQLField("source_view_id")
    type: "BoardViewGraphQLField" = BoardViewGraphQLField("type")
    view_specific_data_str: "BoardViewGraphQLField" = BoardViewGraphQLField(
        "view_specific_data_str"
    )

    def fields(self, *subfields: BoardViewGraphQLField) -> "BoardViewFields":
        """Subfields should come from the BoardViewFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "BoardViewFields":
        self._alias = alias
        return self


class ChangeTeamMembershipsResultFields(GraphQLField):
    @classmethod
    def failed_users(cls) -> "UserFields":
        return UserFields("failed_users")

    @classmethod
    def successful_users(cls) -> "UserFields":
        return UserFields("successful_users")

    def fields(
        self, *subfields: Union[ChangeTeamMembershipsResultGraphQLField, "UserFields"]
    ) -> "ChangeTeamMembershipsResultFields":
        """Subfields should come from the ChangeTeamMembershipsResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ChangeTeamMembershipsResultFields":
        self._alias = alias
        return self


class ColumnFields(GraphQLField):
    archived: "ColumnGraphQLField" = ColumnGraphQLField("archived")
    description: "ColumnGraphQLField" = ColumnGraphQLField("description")
    id: "ColumnGraphQLField" = ColumnGraphQLField("id")
    settings_str: "ColumnGraphQLField" = ColumnGraphQLField("settings_str")
    title: "ColumnGraphQLField" = ColumnGraphQLField("title")
    type: "ColumnGraphQLField" = ColumnGraphQLField("type")
    width: "ColumnGraphQLField" = ColumnGraphQLField("width")

    def fields(self, *subfields: ColumnGraphQLField) -> "ColumnFields":
        """Subfields should come from the ColumnFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ColumnFields":
        self._alias = alias
        return self


class ComplexityFields(GraphQLField):
    after: "ComplexityGraphQLField" = ComplexityGraphQLField("after")
    before: "ComplexityGraphQLField" = ComplexityGraphQLField("before")
    query: "ComplexityGraphQLField" = ComplexityGraphQLField("query")
    reset_in_x_seconds: "ComplexityGraphQLField" = ComplexityGraphQLField(
        "reset_in_x_seconds"
    )

    def fields(self, *subfields: ComplexityGraphQLField) -> "ComplexityFields":
        """Subfields should come from the ComplexityFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ComplexityFields":
        self._alias = alias
        return self


class CustomActivityFields(GraphQLField):
    id: "CustomActivityGraphQLField" = CustomActivityGraphQLField("id")
    type: "CustomActivityGraphQLField" = CustomActivityGraphQLField("type")
    name: "CustomActivityGraphQLField" = CustomActivityGraphQLField("name")
    icon_id: "CustomActivityGraphQLField" = CustomActivityGraphQLField("icon_id")
    color: "CustomActivityGraphQLField" = CustomActivityGraphQLField("color")

    def fields(self, *subfields: CustomActivityGraphQLField) -> "CustomActivityFields":
        """Subfields should come from the CustomActivityFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomActivityFields":
        self._alias = alias
        return self


class CustomFieldMetasFields(GraphQLField):
    description: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField(
        "description"
    )
    editable: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField("editable")
    field_type: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField(
        "field_type"
    )
    flagged: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField("flagged")
    icon: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField("icon")
    id: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField("id")
    position: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField("position")
    title: "CustomFieldMetasGraphQLField" = CustomFieldMetasGraphQLField("title")

    def fields(
        self, *subfields: CustomFieldMetasGraphQLField
    ) -> "CustomFieldMetasFields":
        """Subfields should come from the CustomFieldMetasFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomFieldMetasFields":
        self._alias = alias
        return self


class CustomFieldValueFields(GraphQLField):
    custom_field_meta_id: "CustomFieldValueGraphQLField" = CustomFieldValueGraphQLField(
        "custom_field_meta_id"
    )
    value: "CustomFieldValueGraphQLField" = CustomFieldValueGraphQLField("value")

    def fields(
        self, *subfields: CustomFieldValueGraphQLField
    ) -> "CustomFieldValueFields":
        """Subfields should come from the CustomFieldValueFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomFieldValueFields":
        self._alias = alias
        return self


class DeactivateUsersErrorFields(GraphQLField):
    message: "DeactivateUsersErrorGraphQLField" = DeactivateUsersErrorGraphQLField(
        "message"
    )
    code: "DeactivateUsersErrorGraphQLField" = DeactivateUsersErrorGraphQLField("code")
    user_id: "DeactivateUsersErrorGraphQLField" = DeactivateUsersErrorGraphQLField(
        "user_id"
    )

    def fields(
        self, *subfields: DeactivateUsersErrorGraphQLField
    ) -> "DeactivateUsersErrorFields":
        """Subfields should come from the DeactivateUsersErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DeactivateUsersErrorFields":
        self._alias = alias
        return self


class DeactivateUsersResultFields(GraphQLField):
    @classmethod
    def deactivated_users(cls) -> "UserFields":
        return UserFields("deactivated_users")

    @classmethod
    def errors(cls) -> "DeactivateUsersErrorFields":
        return DeactivateUsersErrorFields("errors")

    def fields(
        self,
        *subfields: Union[
            DeactivateUsersResultGraphQLField,
            "DeactivateUsersErrorFields",
            "UserFields",
        ]
    ) -> "DeactivateUsersResultFields":
        """Subfields should come from the DeactivateUsersResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DeactivateUsersResultFields":
        self._alias = alias
        return self


class DeleteMarketplaceAppDiscountFields(GraphQLField):
    account_slug: "DeleteMarketplaceAppDiscountGraphQLField" = (
        DeleteMarketplaceAppDiscountGraphQLField("account_slug")
    )
    app_id: "DeleteMarketplaceAppDiscountGraphQLField" = (
        DeleteMarketplaceAppDiscountGraphQLField("app_id")
    )

    def fields(
        self, *subfields: DeleteMarketplaceAppDiscountGraphQLField
    ) -> "DeleteMarketplaceAppDiscountFields":
        """Subfields should come from the DeleteMarketplaceAppDiscountFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DeleteMarketplaceAppDiscountFields":
        self._alias = alias
        return self


class DeleteMarketplaceAppDiscountResultFields(GraphQLField):
    @classmethod
    def deleted_discount(cls) -> "DeleteMarketplaceAppDiscountFields":
        return DeleteMarketplaceAppDiscountFields("deleted_discount")

    def fields(
        self,
        *subfields: Union[
            DeleteMarketplaceAppDiscountResultGraphQLField,
            "DeleteMarketplaceAppDiscountFields",
        ]
    ) -> "DeleteMarketplaceAppDiscountResultFields":
        """Subfields should come from the DeleteMarketplaceAppDiscountResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DeleteMarketplaceAppDiscountResultFields":
        self._alias = alias
        return self


class DocumentFields(GraphQLField):
    @classmethod
    def blocks(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "DocumentBlockFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentBlockFields("blocks", arguments=cleared_arguments)

    created_at: "DocumentGraphQLField" = DocumentGraphQLField("created_at")

    @classmethod
    def created_by(cls) -> "UserFields":
        return UserFields("created_by")

    doc_folder_id: "DocumentGraphQLField" = DocumentGraphQLField("doc_folder_id")
    doc_kind: "DocumentGraphQLField" = DocumentGraphQLField("doc_kind")
    id: "DocumentGraphQLField" = DocumentGraphQLField("id")
    name: "DocumentGraphQLField" = DocumentGraphQLField("name")
    object_id: "DocumentGraphQLField" = DocumentGraphQLField("object_id")
    relative_url: "DocumentGraphQLField" = DocumentGraphQLField("relative_url")
    settings: "DocumentGraphQLField" = DocumentGraphQLField("settings")
    url: "DocumentGraphQLField" = DocumentGraphQLField("url")

    @classmethod
    def workspace(cls) -> "WorkspaceFields":
        return WorkspaceFields("workspace")

    workspace_id: "DocumentGraphQLField" = DocumentGraphQLField("workspace_id")

    def fields(
        self,
        *subfields: Union[
            DocumentGraphQLField, "DocumentBlockFields", "UserFields", "WorkspaceFields"
        ]
    ) -> "DocumentFields":
        """Subfields should come from the DocumentFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentFields":
        self._alias = alias
        return self


class DocumentBlockFields(GraphQLField):
    content: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("content")
    created_at: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("created_at")

    @classmethod
    def created_by(cls) -> "UserFields":
        return UserFields("created_by")

    doc_id: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("doc_id")
    id: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("id")
    parent_block_id: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField(
        "parent_block_id"
    )
    position: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("position")
    type: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("type")
    updated_at: "DocumentBlockGraphQLField" = DocumentBlockGraphQLField("updated_at")

    def fields(
        self, *subfields: Union[DocumentBlockGraphQLField, "UserFields"]
    ) -> "DocumentBlockFields":
        """Subfields should come from the DocumentBlockFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentBlockFields":
        self._alias = alias
        return self


class DocumentBlockIdOnlyFields(GraphQLField):
    id: "DocumentBlockIdOnlyGraphQLField" = DocumentBlockIdOnlyGraphQLField("id")

    def fields(
        self, *subfields: DocumentBlockIdOnlyGraphQLField
    ) -> "DocumentBlockIdOnlyFields":
        """Subfields should come from the DocumentBlockIdOnlyFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentBlockIdOnlyFields":
        self._alias = alias
        return self


class ExtendTrialPeriodFields(GraphQLField):
    account_slug: "ExtendTrialPeriodGraphQLField" = ExtendTrialPeriodGraphQLField(
        "account_slug"
    )
    reason: "ExtendTrialPeriodGraphQLField" = ExtendTrialPeriodGraphQLField("reason")
    success: "ExtendTrialPeriodGraphQLField" = ExtendTrialPeriodGraphQLField("success")

    def fields(
        self, *subfields: ExtendTrialPeriodGraphQLField
    ) -> "ExtendTrialPeriodFields":
        """Subfields should come from the ExtendTrialPeriodFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ExtendTrialPeriodFields":
        self._alias = alias
        return self


class FolderFields(GraphQLField):
    @classmethod
    def children(cls) -> "BoardFields":
        return BoardFields("children")

    color: "FolderGraphQLField" = FolderGraphQLField("color")
    created_at: "FolderGraphQLField" = FolderGraphQLField("created_at")
    custom_icon: "FolderGraphQLField" = FolderGraphQLField("custom_icon")
    font_weight: "FolderGraphQLField" = FolderGraphQLField("font_weight")
    id: "FolderGraphQLField" = FolderGraphQLField("id")
    name: "FolderGraphQLField" = FolderGraphQLField("name")
    owner_id: "FolderGraphQLField" = FolderGraphQLField("owner_id")

    @classmethod
    def parent(cls) -> "FolderFields":
        return FolderFields("parent")

    @classmethod
    def sub_folders(cls) -> "FolderFields":
        return FolderFields("sub_folders")

    @classmethod
    def workspace(cls) -> "WorkspaceFields":
        return WorkspaceFields("workspace")

    def fields(
        self,
        *subfields: Union[
            FolderGraphQLField, "BoardFields", "FolderFields", "WorkspaceFields"
        ]
    ) -> "FolderFields":
        """Subfields should come from the FolderFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FolderFields":
        self._alias = alias
        return self


class GrantMarketplaceAppDiscountFields(GraphQLField):
    days_valid: "GrantMarketplaceAppDiscountGraphQLField" = (
        GrantMarketplaceAppDiscountGraphQLField("days_valid")
    )
    discount: "GrantMarketplaceAppDiscountGraphQLField" = (
        GrantMarketplaceAppDiscountGraphQLField("discount")
    )
    is_recurring: "GrantMarketplaceAppDiscountGraphQLField" = (
        GrantMarketplaceAppDiscountGraphQLField("is_recurring")
    )
    period: "GrantMarketplaceAppDiscountGraphQLField" = (
        GrantMarketplaceAppDiscountGraphQLField("period")
    )
    app_plan_ids: "GrantMarketplaceAppDiscountGraphQLField" = (
        GrantMarketplaceAppDiscountGraphQLField("app_plan_ids")
    )
    app_id: "GrantMarketplaceAppDiscountGraphQLField" = (
        GrantMarketplaceAppDiscountGraphQLField("app_id")
    )

    def fields(
        self, *subfields: GrantMarketplaceAppDiscountGraphQLField
    ) -> "GrantMarketplaceAppDiscountFields":
        """Subfields should come from the GrantMarketplaceAppDiscountFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GrantMarketplaceAppDiscountFields":
        self._alias = alias
        return self


class GrantMarketplaceAppDiscountResultFields(GraphQLField):
    @classmethod
    def granted_discount(cls) -> "GrantMarketplaceAppDiscountFields":
        return GrantMarketplaceAppDiscountFields("granted_discount")

    def fields(
        self,
        *subfields: Union[
            GrantMarketplaceAppDiscountResultGraphQLField,
            "GrantMarketplaceAppDiscountFields",
        ]
    ) -> "GrantMarketplaceAppDiscountResultFields":
        """Subfields should come from the GrantMarketplaceAppDiscountResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GrantMarketplaceAppDiscountResultFields":
        self._alias = alias
        return self


class GroupFields(GraphQLField):
    archived: "GroupGraphQLField" = GroupGraphQLField("archived")
    color: "GroupGraphQLField" = GroupGraphQLField("color")
    deleted: "GroupGraphQLField" = GroupGraphQLField("deleted")
    id: "GroupGraphQLField" = GroupGraphQLField("id")

    @classmethod
    def items_page(
        cls,
        limit: int,
        *,
        cursor: Optional[str] = None,
        query_params: Optional[ItemsQuery] = None
    ) -> "ItemsResponseFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "cursor": {"type": "String", "value": cursor},
            "limit": {"type": "Int!", "value": limit},
            "query_params": {"type": "ItemsQuery", "value": query_params},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemsResponseFields("items_page", arguments=cleared_arguments)

    position: "GroupGraphQLField" = GroupGraphQLField("position")
    title: "GroupGraphQLField" = GroupGraphQLField("title")

    def fields(
        self, *subfields: Union[GroupGraphQLField, "ItemsResponseFields"]
    ) -> "GroupFields":
        """Subfields should come from the GroupFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GroupFields":
        self._alias = alias
        return self


class ItemFields(GraphQLField):
    id: "ItemGraphQLField" = ItemGraphQLField("id")

    @classmethod
    def updates(
        cls,
        *,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        ids: Optional[str] = None
    ) -> "UpdateFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
            "ids": {"type": "ID", "value": ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UpdateFields("updates", arguments=cleared_arguments)

    @classmethod
    def assets(
        cls,
        *,
        assets_source: Optional[AssetsSource] = None,
        column_ids: Optional[str] = None
    ) -> "AssetFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "assets_source": {"type": "AssetsSource", "value": assets_source},
            "column_ids": {"type": "String", "value": column_ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AssetFields("assets", arguments=cleared_arguments)

    @classmethod
    def board(cls) -> "BoardFields":
        return BoardFields("board")

    @classmethod
    def column_values(
        cls, *, ids: Optional[str] = None, types: Optional[ColumnType] = None
    ) -> "ColumnValueInterface":
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "String", "value": ids},
            "types": {"type": "ColumnType", "value": types},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ColumnValueInterface("column_values", arguments=cleared_arguments)

    created_at: "ItemGraphQLField" = ItemGraphQLField("created_at")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    creator_id: "ItemGraphQLField" = ItemGraphQLField("creator_id")
    email: "ItemGraphQLField" = ItemGraphQLField("email")

    @classmethod
    def group(cls) -> "GroupFields":
        return GroupFields("group")

    @classmethod
    def linked_items(
        cls, link_to_item_column_id: str, linked_board_id: str
    ) -> "ItemFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "link_to_item_column_id": {
                "type": "String!",
                "value": link_to_item_column_id,
            },
            "linked_board_id": {"type": "ID!", "value": linked_board_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ItemFields("linked_items", arguments=cleared_arguments)

    name: "ItemGraphQLField" = ItemGraphQLField("name")

    @classmethod
    def parent_item(cls) -> "ItemFields":
        return ItemFields("parent_item")

    relative_link: "ItemGraphQLField" = ItemGraphQLField("relative_link")
    state: "ItemGraphQLField" = ItemGraphQLField("state")

    @classmethod
    def subitems(cls) -> "ItemFields":
        return ItemFields("subitems")

    @classmethod
    def subscribers(cls) -> "UserFields":
        return UserFields("subscribers")

    updated_at: "ItemGraphQLField" = ItemGraphQLField("updated_at")
    url: "ItemGraphQLField" = ItemGraphQLField("url")

    def fields(
        self,
        *subfields: Union[
            ItemGraphQLField,
            "AssetFields",
            "BoardFields",
            "ColumnValueInterface",
            "GroupFields",
            "ItemFields",
            "UpdateFields",
            "UserFields",
        ]
    ) -> "ItemFields":
        """Subfields should come from the ItemFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ItemFields":
        self._alias = alias
        return self


class ItemsResponseFields(GraphQLField):
    cursor: "ItemsResponseGraphQLField" = ItemsResponseGraphQLField("cursor")

    @classmethod
    def items(cls) -> "ItemFields":
        return ItemFields("items")

    def fields(
        self, *subfields: Union[ItemsResponseGraphQLField, "ItemFields"]
    ) -> "ItemsResponseFields":
        """Subfields should come from the ItemsResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ItemsResponseFields":
        self._alias = alias
        return self


class LikeFields(GraphQLField):
    id: "LikeGraphQLField" = LikeGraphQLField("id")
    creator_id: "LikeGraphQLField" = LikeGraphQLField("creator_id")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    reaction_type: "LikeGraphQLField" = LikeGraphQLField("reaction_type")
    created_at: "LikeGraphQLField" = LikeGraphQLField("created_at")
    updated_at: "LikeGraphQLField" = LikeGraphQLField("updated_at")

    def fields(self, *subfields: Union[LikeGraphQLField, "UserFields"]) -> "LikeFields":
        """Subfields should come from the LikeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "LikeFields":
        self._alias = alias
        return self


class MarketplaceAppDiscountFields(GraphQLField):
    account_slug: "MarketplaceAppDiscountGraphQLField" = (
        MarketplaceAppDiscountGraphQLField("account_slug")
    )
    account_id: "MarketplaceAppDiscountGraphQLField" = (
        MarketplaceAppDiscountGraphQLField("account_id")
    )
    discount: "MarketplaceAppDiscountGraphQLField" = MarketplaceAppDiscountGraphQLField(
        "discount"
    )
    is_recurring: "MarketplaceAppDiscountGraphQLField" = (
        MarketplaceAppDiscountGraphQLField("is_recurring")
    )
    app_plan_ids: "MarketplaceAppDiscountGraphQLField" = (
        MarketplaceAppDiscountGraphQLField("app_plan_ids")
    )
    period: "MarketplaceAppDiscountGraphQLField" = MarketplaceAppDiscountGraphQLField(
        "period"
    )
    valid_until: "MarketplaceAppDiscountGraphQLField" = (
        MarketplaceAppDiscountGraphQLField("valid_until")
    )
    created_at: "MarketplaceAppDiscountGraphQLField" = (
        MarketplaceAppDiscountGraphQLField("created_at")
    )

    def fields(
        self, *subfields: MarketplaceAppDiscountGraphQLField
    ) -> "MarketplaceAppDiscountFields":
        """Subfields should come from the MarketplaceAppDiscountFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "MarketplaceAppDiscountFields":
        self._alias = alias
        return self


class NotificationFields(GraphQLField):
    id: "NotificationGraphQLField" = NotificationGraphQLField("id")
    text: "NotificationGraphQLField" = NotificationGraphQLField("text")

    def fields(self, *subfields: NotificationGraphQLField) -> "NotificationFields":
        """Subfields should come from the NotificationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationFields":
        self._alias = alias
        return self


class OutOfOfficeFields(GraphQLField):
    active: "OutOfOfficeGraphQLField" = OutOfOfficeGraphQLField("active")
    disable_notifications: "OutOfOfficeGraphQLField" = OutOfOfficeGraphQLField(
        "disable_notifications"
    )
    end_date: "OutOfOfficeGraphQLField" = OutOfOfficeGraphQLField("end_date")
    start_date: "OutOfOfficeGraphQLField" = OutOfOfficeGraphQLField("start_date")
    type: "OutOfOfficeGraphQLField" = OutOfOfficeGraphQLField("type")

    def fields(self, *subfields: OutOfOfficeGraphQLField) -> "OutOfOfficeFields":
        """Subfields should come from the OutOfOfficeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OutOfOfficeFields":
        self._alias = alias
        return self


class PlanFields(GraphQLField):
    max_users: "PlanGraphQLField" = PlanGraphQLField("max_users")
    period: "PlanGraphQLField" = PlanGraphQLField("period")
    tier: "PlanGraphQLField" = PlanGraphQLField("tier")
    version: "PlanGraphQLField" = PlanGraphQLField("version")

    def fields(self, *subfields: PlanGraphQLField) -> "PlanFields":
        """Subfields should come from the PlanFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PlanFields":
        self._alias = alias
        return self


class RemoveTeamOwnersErrorFields(GraphQLField):
    message: "RemoveTeamOwnersErrorGraphQLField" = RemoveTeamOwnersErrorGraphQLField(
        "message"
    )
    code: "RemoveTeamOwnersErrorGraphQLField" = RemoveTeamOwnersErrorGraphQLField(
        "code"
    )
    user_id: "RemoveTeamOwnersErrorGraphQLField" = RemoveTeamOwnersErrorGraphQLField(
        "user_id"
    )

    def fields(
        self, *subfields: RemoveTeamOwnersErrorGraphQLField
    ) -> "RemoveTeamOwnersErrorFields":
        """Subfields should come from the RemoveTeamOwnersErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RemoveTeamOwnersErrorFields":
        self._alias = alias
        return self


class RemoveTeamOwnersResultFields(GraphQLField):
    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def errors(cls) -> "RemoveTeamOwnersErrorFields":
        return RemoveTeamOwnersErrorFields("errors")

    def fields(
        self,
        *subfields: Union[
            RemoveTeamOwnersResultGraphQLField,
            "RemoveTeamOwnersErrorFields",
            "TeamFields",
        ]
    ) -> "RemoveTeamOwnersResultFields":
        """Subfields should come from the RemoveTeamOwnersResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RemoveTeamOwnersResultFields":
        self._alias = alias
        return self


class ReplyFields(GraphQLField):
    id: "ReplyGraphQLField" = ReplyGraphQLField("id")
    body: "ReplyGraphQLField" = ReplyGraphQLField("body")
    kind: "ReplyGraphQLField" = ReplyGraphQLField("kind")
    creator_id: "ReplyGraphQLField" = ReplyGraphQLField("creator_id")
    edited_at: "ReplyGraphQLField" = ReplyGraphQLField("edited_at")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def likes(cls) -> "LikeFields":
        return LikeFields("likes")

    @classmethod
    def pinned_to_top(cls) -> "UpdatePinFields":
        return UpdatePinFields("pinned_to_top")

    @classmethod
    def viewers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "WatcherFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WatcherFields("viewers", arguments=cleared_arguments)

    created_at: "ReplyGraphQLField" = ReplyGraphQLField("created_at")
    updated_at: "ReplyGraphQLField" = ReplyGraphQLField("updated_at")
    text_body: "ReplyGraphQLField" = ReplyGraphQLField("text_body")

    def fields(
        self,
        *subfields: Union[
            ReplyGraphQLField,
            "LikeFields",
            "UpdatePinFields",
            "UserFields",
            "WatcherFields",
        ]
    ) -> "ReplyFields":
        """Subfields should come from the ReplyFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ReplyFields":
        self._alias = alias
        return self


class SubscriptionDiscountFields(GraphQLField):
    value: "SubscriptionDiscountGraphQLField" = SubscriptionDiscountGraphQLField(
        "value"
    )
    discount_model_type: "SubscriptionDiscountGraphQLField" = (
        SubscriptionDiscountGraphQLField("discount_model_type")
    )
    discount_type: "SubscriptionDiscountGraphQLField" = (
        SubscriptionDiscountGraphQLField("discount_type")
    )

    def fields(
        self, *subfields: SubscriptionDiscountGraphQLField
    ) -> "SubscriptionDiscountFields":
        """Subfields should come from the SubscriptionDiscountFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SubscriptionDiscountFields":
        self._alias = alias
        return self


class TagFields(GraphQLField):
    color: "TagGraphQLField" = TagGraphQLField("color")
    id: "TagGraphQLField" = TagGraphQLField("id")
    name: "TagGraphQLField" = TagGraphQLField("name")

    def fields(self, *subfields: TagGraphQLField) -> "TagFields":
        """Subfields should come from the TagFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TagFields":
        self._alias = alias
        return self


class TeamFields(GraphQLField):
    id: "TeamGraphQLField" = TeamGraphQLField("id")

    @classmethod
    def owners(cls, *, ids: Optional[str] = None) -> "UserFields":
        arguments: Dict[str, Dict[str, Any]] = {"ids": {"type": "ID", "value": ids}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields("owners", arguments=cleared_arguments)

    picture_url: "TeamGraphQLField" = TeamGraphQLField("picture_url")

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
    ) -> "UserFields":
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
        return UserFields("users", arguments=cleared_arguments)

    name: "TeamGraphQLField" = TeamGraphQLField("name")
    is_guest: "TeamGraphQLField" = TeamGraphQLField("is_guest")

    def fields(self, *subfields: Union[TeamGraphQLField, "UserFields"]) -> "TeamFields":
        """Subfields should come from the TeamFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamFields":
        self._alias = alias
        return self


class TemplateFields(GraphQLField):
    process_id: "TemplateGraphQLField" = TemplateGraphQLField("process_id")

    def fields(self, *subfields: TemplateGraphQLField) -> "TemplateFields":
        """Subfields should come from the TemplateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TemplateFields":
        self._alias = alias
        return self


class TimelineItemFields(GraphQLField):
    id: "TimelineItemGraphQLField" = TimelineItemGraphQLField("id")
    type: "TimelineItemGraphQLField" = TimelineItemGraphQLField("type")

    @classmethod
    def item(cls) -> "ItemFields":
        return ItemFields("item")

    @classmethod
    def board(cls) -> "BoardFields":
        return BoardFields("board")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    title: "TimelineItemGraphQLField" = TimelineItemGraphQLField("title")
    custom_activity_id: "TimelineItemGraphQLField" = TimelineItemGraphQLField(
        "custom_activity_id"
    )
    content: "TimelineItemGraphQLField" = TimelineItemGraphQLField("content")
    created_at: "TimelineItemGraphQLField" = TimelineItemGraphQLField("created_at")

    def fields(
        self,
        *subfields: Union[
            TimelineItemGraphQLField, "BoardFields", "ItemFields", "UserFields"
        ]
    ) -> "TimelineItemFields":
        """Subfields should come from the TimelineItemFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimelineItemFields":
        self._alias = alias
        return self


class TimelineItemsPageFields(GraphQLField):
    @classmethod
    def timeline_items(cls) -> "TimelineItemFields":
        return TimelineItemFields("timeline_items")

    cursor: "TimelineItemsPageGraphQLField" = TimelineItemsPageGraphQLField("cursor")

    def fields(
        self, *subfields: Union[TimelineItemsPageGraphQLField, "TimelineItemFields"]
    ) -> "TimelineItemsPageFields":
        """Subfields should come from the TimelineItemsPageFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimelineItemsPageFields":
        self._alias = alias
        return self


class TimelineResponseFields(GraphQLField):
    @classmethod
    def timeline_items_page(
        cls, *, cursor: Optional[str] = None, limit: Optional[int] = None
    ) -> "TimelineItemsPageFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "cursor": {"type": "String", "value": cursor},
            "limit": {"type": "Int", "value": limit},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimelineItemsPageFields(
            "timeline_items_page", arguments=cleared_arguments
        )

    def fields(
        self, *subfields: Union[TimelineResponseGraphQLField, "TimelineItemsPageFields"]
    ) -> "TimelineResponseFields":
        """Subfields should come from the TimelineResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimelineResponseFields":
        self._alias = alias
        return self


class UpdateFields(GraphQLField):
    id: "UpdateGraphQLField" = UpdateGraphQLField("id")
    body: "UpdateGraphQLField" = UpdateGraphQLField("body")
    creator_id: "UpdateGraphQLField" = UpdateGraphQLField("creator_id")
    edited_at: "UpdateGraphQLField" = UpdateGraphQLField("edited_at")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def likes(cls) -> "LikeFields":
        return LikeFields("likes")

    @classmethod
    def pinned_to_top(cls) -> "UpdatePinFields":
        return UpdatePinFields("pinned_to_top")

    @classmethod
    def viewers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "WatcherFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WatcherFields("viewers", arguments=cleared_arguments)

    created_at: "UpdateGraphQLField" = UpdateGraphQLField("created_at")
    updated_at: "UpdateGraphQLField" = UpdateGraphQLField("updated_at")
    item_id: "UpdateGraphQLField" = UpdateGraphQLField("item_id")

    @classmethod
    def item(cls) -> "ItemFields":
        return ItemFields("item")

    @classmethod
    def replies(cls) -> "ReplyFields":
        return ReplyFields("replies")

    @classmethod
    def assets(cls) -> "AssetFields":
        return AssetFields("assets")

    text_body: "UpdateGraphQLField" = UpdateGraphQLField("text_body")

    def fields(
        self,
        *subfields: Union[
            UpdateGraphQLField,
            "AssetFields",
            "ItemFields",
            "LikeFields",
            "ReplyFields",
            "UpdatePinFields",
            "UserFields",
            "WatcherFields",
        ]
    ) -> "UpdateFields":
        """Subfields should come from the UpdateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UpdateFields":
        self._alias = alias
        return self


class UpdateEmailDomainErrorFields(GraphQLField):
    message: "UpdateEmailDomainErrorGraphQLField" = UpdateEmailDomainErrorGraphQLField(
        "message"
    )
    code: "UpdateEmailDomainErrorGraphQLField" = UpdateEmailDomainErrorGraphQLField(
        "code"
    )
    user_id: "UpdateEmailDomainErrorGraphQLField" = UpdateEmailDomainErrorGraphQLField(
        "user_id"
    )

    def fields(
        self, *subfields: UpdateEmailDomainErrorGraphQLField
    ) -> "UpdateEmailDomainErrorFields":
        """Subfields should come from the UpdateEmailDomainErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UpdateEmailDomainErrorFields":
        self._alias = alias
        return self


class UpdateEmailDomainResultFields(GraphQLField):
    @classmethod
    def updated_users(cls) -> "UserFields":
        return UserFields("updated_users")

    @classmethod
    def errors(cls) -> "UpdateEmailDomainErrorFields":
        return UpdateEmailDomainErrorFields("errors")

    def fields(
        self,
        *subfields: Union[
            UpdateEmailDomainResultGraphQLField,
            "UpdateEmailDomainErrorFields",
            "UserFields",
        ]
    ) -> "UpdateEmailDomainResultFields":
        """Subfields should come from the UpdateEmailDomainResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UpdateEmailDomainResultFields":
        self._alias = alias
        return self


class UpdatePinFields(GraphQLField):
    item_id: "UpdatePinGraphQLField" = UpdatePinGraphQLField("item_id")

    def fields(self, *subfields: UpdatePinGraphQLField) -> "UpdatePinFields":
        """Subfields should come from the UpdatePinFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UpdatePinFields":
        self._alias = alias
        return self


class UpdateUsersRoleErrorFields(GraphQLField):
    message: "UpdateUsersRoleErrorGraphQLField" = UpdateUsersRoleErrorGraphQLField(
        "message"
    )
    code: "UpdateUsersRoleErrorGraphQLField" = UpdateUsersRoleErrorGraphQLField("code")
    user_id: "UpdateUsersRoleErrorGraphQLField" = UpdateUsersRoleErrorGraphQLField(
        "user_id"
    )

    def fields(
        self, *subfields: UpdateUsersRoleErrorGraphQLField
    ) -> "UpdateUsersRoleErrorFields":
        """Subfields should come from the UpdateUsersRoleErrorFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UpdateUsersRoleErrorFields":
        self._alias = alias
        return self


class UpdateUsersRoleResultFields(GraphQLField):
    @classmethod
    def updated_users(cls) -> "UserFields":
        return UserFields("updated_users")

    @classmethod
    def errors(cls) -> "UpdateUsersRoleErrorFields":
        return UpdateUsersRoleErrorFields("errors")

    def fields(
        self,
        *subfields: Union[
            UpdateUsersRoleResultGraphQLField,
            "UpdateUsersRoleErrorFields",
            "UserFields",
        ]
    ) -> "UpdateUsersRoleResultFields":
        """Subfields should come from the UpdateUsersRoleResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UpdateUsersRoleResultFields":
        self._alias = alias
        return self


class UserFields(GraphQLField):
    id: "UserGraphQLField" = UserGraphQLField("id")

    @classmethod
    def account(cls) -> "AccountFields":
        return AccountFields("account")

    @classmethod
    def account_products(cls) -> "AccountProductFields":
        return AccountProductFields("account_products")

    birthday: "UserGraphQLField" = UserGraphQLField("birthday")
    country_code: "UserGraphQLField" = UserGraphQLField("country_code")
    created_at: "UserGraphQLField" = UserGraphQLField("created_at")
    current_language: "UserGraphQLField" = UserGraphQLField("current_language")

    @classmethod
    def custom_field_metas(cls) -> "CustomFieldMetasFields":
        return CustomFieldMetasFields("custom_field_metas")

    @classmethod
    def custom_field_values(cls) -> "CustomFieldValueFields":
        return CustomFieldValueFields("custom_field_values")

    email: "UserGraphQLField" = UserGraphQLField("email")
    enabled: "UserGraphQLField" = UserGraphQLField("enabled")
    encrypt_api_token: "UserGraphQLField" = UserGraphQLField("encrypt_api_token")
    is_admin: "UserGraphQLField" = UserGraphQLField("is_admin")
    is_guest: "UserGraphQLField" = UserGraphQLField("is_guest")
    is_pending: "UserGraphQLField" = UserGraphQLField("is_pending")
    is_verified: "UserGraphQLField" = UserGraphQLField("is_verified")
    is_view_only: "UserGraphQLField" = UserGraphQLField("is_view_only")
    join_date: "UserGraphQLField" = UserGraphQLField("join_date")
    last_activity: "UserGraphQLField" = UserGraphQLField("last_activity")
    location: "UserGraphQLField" = UserGraphQLField("location")
    mobile_phone: "UserGraphQLField" = UserGraphQLField("mobile_phone")
    name: "UserGraphQLField" = UserGraphQLField("name")

    @classmethod
    def out_of_office(cls) -> "OutOfOfficeFields":
        return OutOfOfficeFields("out_of_office")

    phone: "UserGraphQLField" = UserGraphQLField("phone")
    photo_original: "UserGraphQLField" = UserGraphQLField("photo_original")
    photo_small: "UserGraphQLField" = UserGraphQLField("photo_small")
    photo_thumb: "UserGraphQLField" = UserGraphQLField("photo_thumb")
    photo_thumb_small: "UserGraphQLField" = UserGraphQLField("photo_thumb_small")
    photo_tiny: "UserGraphQLField" = UserGraphQLField("photo_tiny")
    sign_up_product_kind: "UserGraphQLField" = UserGraphQLField("sign_up_product_kind")

    @classmethod
    def teams(cls, *, ids: Optional[str] = None) -> "TeamFields":
        arguments: Dict[str, Dict[str, Any]] = {"ids": {"type": "ID", "value": ids}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields("teams", arguments=cleared_arguments)

    time_zone_identifier: "UserGraphQLField" = UserGraphQLField("time_zone_identifier")
    title: "UserGraphQLField" = UserGraphQLField("title")
    url: "UserGraphQLField" = UserGraphQLField("url")
    utc_hours_diff: "UserGraphQLField" = UserGraphQLField("utc_hours_diff")

    def fields(
        self,
        *subfields: Union[
            UserGraphQLField,
            "AccountFields",
            "AccountProductFields",
            "CustomFieldMetasFields",
            "CustomFieldValueFields",
            "OutOfOfficeFields",
            "TeamFields",
        ]
    ) -> "UserFields":
        """Subfields should come from the UserFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserFields":
        self._alias = alias
        return self


class VersionFields(GraphQLField):
    display_name: "VersionGraphQLField" = VersionGraphQLField("display_name")
    kind: "VersionGraphQLField" = VersionGraphQLField("kind")
    value: "VersionGraphQLField" = VersionGraphQLField("value")

    def fields(self, *subfields: VersionGraphQLField) -> "VersionFields":
        """Subfields should come from the VersionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "VersionFields":
        self._alias = alias
        return self


class WatcherFields(GraphQLField):
    user_id: "WatcherGraphQLField" = WatcherGraphQLField("user_id")
    medium: "WatcherGraphQLField" = WatcherGraphQLField("medium")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    def fields(
        self, *subfields: Union[WatcherGraphQLField, "UserFields"]
    ) -> "WatcherFields":
        """Subfields should come from the WatcherFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WatcherFields":
        self._alias = alias
        return self


class WebhookFields(GraphQLField):
    board_id: "WebhookGraphQLField" = WebhookGraphQLField("board_id")
    config: "WebhookGraphQLField" = WebhookGraphQLField("config")
    event: "WebhookGraphQLField" = WebhookGraphQLField("event")
    id: "WebhookGraphQLField" = WebhookGraphQLField("id")

    def fields(self, *subfields: WebhookGraphQLField) -> "WebhookFields":
        """Subfields should come from the WebhookFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WebhookFields":
        self._alias = alias
        return self


class WorkspaceFields(GraphQLField):
    @classmethod
    def account_product(cls) -> "AccountProductFields":
        return AccountProductFields("account_product")

    created_at: "WorkspaceGraphQLField" = WorkspaceGraphQLField("created_at")
    description: "WorkspaceGraphQLField" = WorkspaceGraphQLField("description")
    id: "WorkspaceGraphQLField" = WorkspaceGraphQLField("id")
    is_default_workspace: "WorkspaceGraphQLField" = WorkspaceGraphQLField(
        "is_default_workspace"
    )
    kind: "WorkspaceGraphQLField" = WorkspaceGraphQLField("kind")
    name: "WorkspaceGraphQLField" = WorkspaceGraphQLField("name")

    @classmethod
    def owners_subscribers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "UserFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields("owners_subscribers", arguments=cleared_arguments)

    @classmethod
    def settings(cls) -> "WorkspaceSettingsFields":
        return WorkspaceSettingsFields("settings")

    state: "WorkspaceGraphQLField" = WorkspaceGraphQLField("state")

    @classmethod
    def team_owners_subscribers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "TeamFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields("team_owners_subscribers", arguments=cleared_arguments)

    @classmethod
    def teams_subscribers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "TeamFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields("teams_subscribers", arguments=cleared_arguments)

    @classmethod
    def users_subscribers(
        cls, *, limit: Optional[int] = None, page: Optional[int] = None
    ) -> "UserFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "limit": {"type": "Int", "value": limit},
            "page": {"type": "Int", "value": page},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields("users_subscribers", arguments=cleared_arguments)

    def fields(
        self,
        *subfields: Union[
            WorkspaceGraphQLField,
            "AccountProductFields",
            "TeamFields",
            "UserFields",
            "WorkspaceSettingsFields",
        ]
    ) -> "WorkspaceFields":
        """Subfields should come from the WorkspaceFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkspaceFields":
        self._alias = alias
        return self


class WorkspaceIconFields(GraphQLField):
    color: "WorkspaceIconGraphQLField" = WorkspaceIconGraphQLField("color")
    image: "WorkspaceIconGraphQLField" = WorkspaceIconGraphQLField("image")

    def fields(self, *subfields: WorkspaceIconGraphQLField) -> "WorkspaceIconFields":
        """Subfields should come from the WorkspaceIconFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkspaceIconFields":
        self._alias = alias
        return self


class WorkspaceSettingsFields(GraphQLField):
    @classmethod
    def icon(cls) -> "WorkspaceIconFields":
        return WorkspaceIconFields("icon")

    def fields(
        self, *subfields: Union[WorkspaceSettingsGraphQLField, "WorkspaceIconFields"]
    ) -> "WorkspaceSettingsFields":
        """Subfields should come from the WorkspaceSettingsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkspaceSettingsFields":
        self._alias = alias
        return self
