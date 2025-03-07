# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from .project_response_model_target_audience import ProjectResponseModelTargetAudience
from .project_state import ProjectState
from .project_response_model_access_level import ProjectResponseModelAccessLevel
from .project_response_model_fiction import ProjectResponseModelFiction
from .project_creation_meta_response_model import ProjectCreationMetaResponseModel
from .project_response_model_source_type import ProjectResponseModelSourceType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ProjectResponse(UncheckedBaseModel):
    project_id: str = pydantic.Field()
    """
    The ID of the project.
    """

    name: str = pydantic.Field()
    """
    The name of the project.
    """

    create_date_unix: int = pydantic.Field()
    """
    The creation date of the project.
    """

    default_title_voice_id: str = pydantic.Field()
    """
    The default title voice ID.
    """

    default_paragraph_voice_id: str = pydantic.Field()
    """
    The default paragraph voice ID.
    """

    default_model_id: str = pydantic.Field()
    """
    The default model ID.
    """

    last_conversion_date_unix: typing.Optional[int] = pydantic.Field(default=None)
    """
    The last conversion date of the project.
    """

    can_be_downloaded: bool = pydantic.Field()
    """
    Whether the project can be downloaded.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the project.
    """

    author: typing.Optional[str] = pydantic.Field(default=None)
    """
    The author of the project.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the project.
    """

    genres: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of genres of the project.
    """

    cover_image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cover image URL of the project.
    """

    target_audience: typing.Optional[ProjectResponseModelTargetAudience] = pydantic.Field(default=None)
    """
    The target audience of the project.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Two-letter language code (ISO 639-1) of the language of the project.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content type of the project, e.g. 'Novel' or 'Short Story'
    """

    original_publication_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original publication date of the project.
    """

    mature_content: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the project contains mature content.
    """

    isbn_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISBN number of the project.
    """

    volume_normalization: bool = pydantic.Field()
    """
    Whether the project uses volume normalization.
    """

    state: ProjectState = pydantic.Field()
    """
    The state of the project.
    """

    access_level: ProjectResponseModelAccessLevel = pydantic.Field()
    """
    The access level of the project.
    """

    fiction: typing.Optional[ProjectResponseModelFiction] = pydantic.Field(default=None)
    """
    Whether the project is fiction.
    """

    quality_check_on: bool = pydantic.Field()
    """
    Whether quality check is enabled for this project.
    """

    quality_check_on_when_bulk_convert: bool = pydantic.Field()
    """
    Whether quality check is enabled on the project when bulk converting.
    """

    creation_meta: typing.Optional[ProjectCreationMetaResponseModel] = pydantic.Field(default=None)
    """
    The creation meta of the project.
    """

    source_type: typing.Optional[ProjectResponseModelSourceType] = pydantic.Field(default=None)
    """
    The source type of the project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
