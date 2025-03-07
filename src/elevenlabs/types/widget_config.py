# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .embed_variant import EmbedVariant
from .widget_expandable import WidgetExpandable
from .widget_config_avatar import WidgetConfigAvatar
from .widget_feedback_mode import WidgetFeedbackMode
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WidgetConfig(UncheckedBaseModel):
    variant: typing.Optional[EmbedVariant] = None
    expandable: typing.Optional[WidgetExpandable] = None
    avatar: typing.Optional[WidgetConfigAvatar] = None
    feedback_mode: typing.Optional[WidgetFeedbackMode] = None
    bg_color: typing.Optional[str] = None
    text_color: typing.Optional[str] = None
    btn_color: typing.Optional[str] = None
    btn_text_color: typing.Optional[str] = None
    border_color: typing.Optional[str] = None
    focus_color: typing.Optional[str] = None
    border_radius: typing.Optional[int] = None
    btn_radius: typing.Optional[int] = None
    action_text: typing.Optional[str] = None
    start_call_text: typing.Optional[str] = None
    end_call_text: typing.Optional[str] = None
    expand_text: typing.Optional[str] = None
    listening_text: typing.Optional[str] = None
    speaking_text: typing.Optional[str] = None
    shareable_page_text: typing.Optional[str] = None
    shareable_page_show_terms: typing.Optional[bool] = None
    terms_text: typing.Optional[str] = None
    terms_html: typing.Optional[str] = None
    terms_key: typing.Optional[str] = None
    show_avatar_when_collapsed: typing.Optional[bool] = None
    disable_banner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to disable the ConvAI widget banner
    """

    language_selector: typing.Optional[bool] = None
    custom_avatar_path: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
