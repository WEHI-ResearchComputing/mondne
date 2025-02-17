from enum import Enum


class CustomActivityColor(str, Enum):
    VIVID_CERULEAN = "VIVID_CERULEAN"
    GO_GREEN = "GO_GREEN"
    PHILIPPINE_GREEN = "PHILIPPINE_GREEN"
    YANKEES_BLUE = "YANKEES_BLUE"
    CELTIC_BLUE = "CELTIC_BLUE"
    MEDIUM_TURQUOISE = "MEDIUM_TURQUOISE"
    CORNFLOWER_BLUE = "CORNFLOWER_BLUE"
    MAYA_BLUE = "MAYA_BLUE"
    SLATE_BLUE = "SLATE_BLUE"
    GRAY = "GRAY"
    YELLOW_GREEN = "YELLOW_GREEN"
    DINGY_DUNGEON = "DINGY_DUNGEON"
    PARADISE_PINK = "PARADISE_PINK"
    BRINK_PINK = "BRINK_PINK"
    YELLOW_ORANGE = "YELLOW_ORANGE"
    LIGHT_DEEP_PINK = "LIGHT_DEEP_PINK"
    LIGHT_HOT_PINK = "LIGHT_HOT_PINK"
    PHILIPPINE_YELLOW = "PHILIPPINE_YELLOW"


class CustomActivityIcon(str, Enum):
    ASCENDING = "ASCENDING"
    CAMERA = "CAMERA"
    CONFERENCE = "CONFERENCE"
    FLAG = "FLAG"
    GIFT = "GIFT"
    HEADPHONES = "HEADPHONES"
    HOMEKEYS = "HOMEKEYS"
    LOCATION = "LOCATION"
    PAPERPLANE = "PAPERPLANE"
    PLANE = "PLANE"
    NOTEBOOK = "NOTEBOOK"
    PLIERS = "PLIERS"
    TRIPOD = "TRIPOD"
    TWOFLAGS = "TWOFLAGS"
    UTENCILS = "UTENCILS"


class DiscountPeriod(str, Enum):
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class SubscriptionDiscountModelType(str, Enum):
    percent = "percent"
    nominal = "nominal"


class SubscriptionDiscountType(str, Enum):
    recurring = "recurring"
    one_time = "one_time"


class SubscriptionPeriodType(str, Enum):
    monthly = "monthly"
    yearly = "yearly"


class SubscriptionStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class AssetsSource(str, Enum):
    all = "all"
    columns = "columns"
    gallery = "gallery"


class BoardAttributes(str, Enum):
    communication = "communication"
    description = "description"
    name = "name"


class BoardKind(str, Enum):
    private = "private"
    public = "public"
    share = "share"


class BoardObjectType(str, Enum):
    board = "board"
    custom_object = "custom_object"
    document = "document"
    sub_items_board = "sub_items_board"


class BoardsOrderBy(str, Enum):
    created_at = "created_at"
    used_at = "used_at"


class BoardSubscriberKind(str, Enum):
    owner = "owner"
    subscriber = "subscriber"


class ColumnProperty(str, Enum):
    description = "description"
    title = "title"


class ColumnType(str, Enum):
    auto_number = "auto_number"
    board_relation = "board_relation"
    button = "button"
    checkbox = "checkbox"
    color_picker = "color_picker"
    country = "country"
    creation_log = "creation_log"
    date = "date"
    dependency = "dependency"
    doc = "doc"
    dropdown = "dropdown"
    email = "email"
    file = "file"
    formula = "formula"
    group = "group"
    hour = "hour"
    integration = "integration"
    item_assignees = "item_assignees"
    item_id = "item_id"
    last_updated = "last_updated"
    link = "link"
    location = "location"
    long_text = "long_text"
    mirror = "mirror"
    name = "name"
    numbers = "numbers"
    people = "people"
    person = "person"
    phone = "phone"
    progress = "progress"
    rating = "rating"
    status = "status"
    subtasks = "subtasks"
    tags = "tags"
    team = "team"
    text = "text"
    time_tracking = "time_tracking"
    timeline = "timeline"
    unsupported = "unsupported"
    vote = "vote"
    week = "week"
    world_clock = "world_clock"


class DocBlockContentType(str, Enum):
    bulleted_list = "bulleted_list"
    check_list = "check_list"
    code = "code"
    divider = "divider"
    image = "image"
    large_title = "large_title"
    layout = "layout"
    medium_title = "medium_title"
    normal_text = "normal_text"
    notice_box = "notice_box"
    numbered_list = "numbered_list"
    page_break = "page_break"
    quote = "quote"
    small_title = "small_title"
    table = "table"
    video = "video"


class DocsOrderBy(str, Enum):
    created_at = "created_at"
    used_at = "used_at"


class DuplicateBoardType(str, Enum):
    duplicate_board_with_pulses = "duplicate_board_with_pulses"
    duplicate_board_with_pulses_and_updates = "duplicate_board_with_pulses_and_updates"
    duplicate_board_with_structure = "duplicate_board_with_structure"


class FileLinkValueKind(str, Enum):
    box = "box"
    dropbox = "dropbox"
    google_drive = "google_drive"
    link = "link"
    onedrive = "onedrive"


class FirstDayOfTheWeek(str, Enum):
    monday = "monday"
    sunday = "sunday"


class FolderColor(str, Enum):
    AQUAMARINE = "AQUAMARINE"
    BRIGHT_BLUE = "BRIGHT_BLUE"
    BRIGHT_GREEN = "BRIGHT_GREEN"
    CHILI_BLUE = "CHILI_BLUE"
    DARK_ORANGE = "DARK_ORANGE"
    DARK_PURPLE = "DARK_PURPLE"
    DARK_RED = "DARK_RED"
    DONE_GREEN = "DONE_GREEN"
    INDIGO = "INDIGO"
    LIPSTICK = "LIPSTICK"
    NULL = "NULL"
    PURPLE = "PURPLE"
    SOFIA_PINK = "SOFIA_PINK"
    STUCK_RED = "STUCK_RED"
    SUNSET = "SUNSET"
    WORKING_ORANGE = "WORKING_ORANGE"


class FolderCustomIcon(str, Enum):
    FOLDER = "FOLDER"
    MOREBELOW = "MOREBELOW"
    MOREBELOWFILLED = "MOREBELOWFILLED"
    NULL = "NULL"
    WORK = "WORK"


class FolderFontWeight(str, Enum):
    FONT_WEIGHT_BOLD = "FONT_WEIGHT_BOLD"
    FONT_WEIGHT_LIGHT = "FONT_WEIGHT_LIGHT"
    FONT_WEIGHT_NORMAL = "FONT_WEIGHT_NORMAL"
    FONT_WEIGHT_VERY_LIGHT = "FONT_WEIGHT_VERY_LIGHT"
    NULL = "NULL"


class GroupAttributes(str, Enum):
    color = "color"
    position = "position"
    relative_position_after = "relative_position_after"
    relative_position_before = "relative_position_before"
    title = "title"


class ItemsOrderByDirection(str, Enum):
    asc = "asc"
    desc = "desc"


class ItemsQueryOperator(str, Enum):
    and_ = "and"
    or_ = "or"


class ItemsQueryRuleOperator(str, Enum):
    any_of = "any_of"
    between = "between"
    contains_terms = "contains_terms"
    contains_text = "contains_text"
    ends_with = "ends_with"
    greater_than = "greater_than"
    greater_than_or_equals = "greater_than_or_equals"
    is_empty = "is_empty"
    is_not_empty = "is_not_empty"
    lower_than = "lower_than"
    lower_than_or_equal = "lower_than_or_equal"
    not_any_of = "not_any_of"
    not_contains_text = "not_contains_text"
    starts_with = "starts_with"
    within_the_last = "within_the_last"
    within_the_next = "within_the_next"


class Kind(str, Enum):
    person = "person"
    team = "team"


class NotificationTargetType(str, Enum):
    Post = "Post"
    Project = "Project"


class NumberValueUnitDirection(str, Enum):
    left = "left"
    right = "right"


class PositionRelative(str, Enum):
    after_at = "after_at"
    before_at = "before_at"


class State(str, Enum):
    active = "active"
    all = "all"
    archived = "archived"
    deleted = "deleted"


class UserKind(str, Enum):
    all = "all"
    guests = "guests"
    non_guests = "non_guests"
    non_pending = "non_pending"


class VersionKind(str, Enum):
    current = "current"
    deprecated = "deprecated"
    dev = "dev"
    maintenance = "maintenance"
    old__maintenance = "old__maintenance"
    old_previous_maintenance = "old_previous_maintenance"
    previous_maintenance = "previous_maintenance"
    release_candidate = "release_candidate"


class WebhookEventType(str, Enum):
    change_column_value = "change_column_value"
    change_name = "change_name"
    change_specific_column_value = "change_specific_column_value"
    change_status_column_value = "change_status_column_value"
    change_subitem_column_value = "change_subitem_column_value"
    change_subitem_name = "change_subitem_name"
    create_column = "create_column"
    create_item = "create_item"
    create_subitem = "create_subitem"
    create_subitem_update = "create_subitem_update"
    create_update = "create_update"
    delete_update = "delete_update"
    edit_update = "edit_update"
    item_archived = "item_archived"
    item_deleted = "item_deleted"
    item_moved_to_any_group = "item_moved_to_any_group"
    item_moved_to_specific_group = "item_moved_to_specific_group"
    item_restored = "item_restored"
    move_subitem = "move_subitem"
    subitem_archived = "subitem_archived"
    subitem_deleted = "subitem_deleted"


class WorkspaceKind(str, Enum):
    closed = "closed"
    open = "open"


class WorkspacesOrderBy(str, Enum):
    created_at = "created_at"


class WorkspaceSubscriberKind(str, Enum):
    owner = "owner"
    subscriber = "subscriber"


class ActivateUsersErrorCode(str, Enum):
    EXCEEDS_BATCH_LIMIT = "EXCEEDS_BATCH_LIMIT"
    INVALID_INPUT = "INVALID_INPUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    CANNOT_UPDATE_SELF = "CANNOT_UPDATE_SELF"
    FAILED = "FAILED"


class AssignTeamOwnersErrorCode(str, Enum):
    VIEWERS_OR_GUESTS = "VIEWERS_OR_GUESTS"
    USER_NOT_MEMBER_OF_TEAM = "USER_NOT_MEMBER_OF_TEAM"
    EXCEEDS_BATCH_LIMIT = "EXCEEDS_BATCH_LIMIT"
    INVALID_INPUT = "INVALID_INPUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    CANNOT_UPDATE_SELF = "CANNOT_UPDATE_SELF"
    FAILED = "FAILED"


class BaseRoleName(str, Enum):
    GUEST = "GUEST"
    VIEW_ONLY = "VIEW_ONLY"
    MEMBER = "MEMBER"
    ADMIN = "ADMIN"


class DeactivateUsersErrorCode(str, Enum):
    EXCEEDS_BATCH_LIMIT = "EXCEEDS_BATCH_LIMIT"
    INVALID_INPUT = "INVALID_INPUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    CANNOT_UPDATE_SELF = "CANNOT_UPDATE_SELF"
    FAILED = "FAILED"


class RemoveTeamOwnersErrorCode(str, Enum):
    VIEWERS_OR_GUESTS = "VIEWERS_OR_GUESTS"
    USER_NOT_MEMBER_OF_TEAM = "USER_NOT_MEMBER_OF_TEAM"
    EXCEEDS_BATCH_LIMIT = "EXCEEDS_BATCH_LIMIT"
    INVALID_INPUT = "INVALID_INPUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    CANNOT_UPDATE_SELF = "CANNOT_UPDATE_SELF"
    FAILED = "FAILED"


class UpdateEmailDomainErrorCode(str, Enum):
    UPDATE_EMAIL_DOMAIN_ERROR = "UPDATE_EMAIL_DOMAIN_ERROR"
    EXCEEDS_BATCH_LIMIT = "EXCEEDS_BATCH_LIMIT"
    INVALID_INPUT = "INVALID_INPUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    CANNOT_UPDATE_SELF = "CANNOT_UPDATE_SELF"
    FAILED = "FAILED"


class UpdateUsersRoleErrorCode(str, Enum):
    EXCEEDS_BATCH_LIMIT = "EXCEEDS_BATCH_LIMIT"
    INVALID_INPUT = "INVALID_INPUT"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    CANNOT_UPDATE_SELF = "CANNOT_UPDATE_SELF"
    FAILED = "FAILED"
