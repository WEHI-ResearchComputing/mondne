from typing import Any, List, Optional

from .base_model import BaseModel
from .enums import (
    BoardKind,
    DiscountPeriod,
    ItemsOrderByDirection,
    ItemsQueryOperator,
    ItemsQueryRuleOperator,
    WorkspaceKind,
)


class TimelineItemTimeRange(BaseModel):
    start_timestamp: Any
    end_timestamp: Any


class GrantMarketplaceAppDiscountData(BaseModel):
    days_valid: int
    discount: int
    is_recurring: bool
    period: Optional[DiscountPeriod] = None
    app_plan_ids: List[str]


class ColumnMappingInput(BaseModel):
    source: str
    target: Optional[str] = None


class CreateDocBoardInput(BaseModel):
    column_id: str
    item_id: str


class CreateDocInput(BaseModel):
    board: Optional["CreateDocBoardInput"] = None
    workspace: Optional["CreateDocWorkspaceInput"] = None


class CreateDocWorkspaceInput(BaseModel):
    kind: Optional[BoardKind] = None
    name: str
    workspace_id: str


class ItemsPageByColumnValuesQuery(BaseModel):
    column_id: str
    column_values: List[str]


class ItemsQuery(BaseModel):
    groups: Optional[List["ItemsQueryGroup"]] = None
    ids: Optional[List[str]] = None
    operator: Optional[ItemsQueryOperator] = None
    order_by: Optional[List["ItemsQueryOrderBy"]] = None
    rules: Optional[List["ItemsQueryRule"]] = None


class ItemsQueryGroup(BaseModel):
    groups: Optional[List["ItemsQueryGroup"]] = None
    operator: Optional[ItemsQueryOperator] = None
    rules: Optional[List["ItemsQueryRule"]] = None


class ItemsQueryOrderBy(BaseModel):
    column_id: str
    direction: Optional[ItemsOrderByDirection] = None


class ItemsQueryRule(BaseModel):
    column_id: str
    compare_attribute: Optional[str] = None
    compare_value: Any
    operator: Optional[ItemsQueryRuleOperator] = None


class UpdateWorkspaceAttributesInput(BaseModel):
    description: Optional[str] = None
    kind: Optional[WorkspaceKind] = None
    name: Optional[str] = None


class CreateTeamAttributesInput(BaseModel):
    name: str
    is_guest_team: Optional[bool] = None
    parent_team_id: Optional[str] = None
    subscriber_ids: Optional[List[str]] = None


class CreateTeamOptionsInput(BaseModel):
    allow_empty_team: Optional[bool] = None


class UpdateEmailDomainAttributesInput(BaseModel):
    user_ids: List[str]
    new_domain: str


CreateDocInput.model_rebuild()
ItemsQuery.model_rebuild()
ItemsQueryGroup.model_rebuild()
