# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .. import core
from ..types.output_format import OutputFormat
from ..core.request_options import RequestOptions
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SpeechToSpeechClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        audio: core.File,
        enable_logging: typing.Optional[bool] = None,
        optimize_streaming_latency: typing.Optional[int] = None,
        output_format: typing.Optional[OutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        remove_background_noise: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Transform audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        audio : core.File
            See core.File for more documentation

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormat]
            The output format of the generated audio.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.Iterator[bytes]
            The generated audio file

        Examples
        --------
        from elevenlabs import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.speech_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            output_format="mp3_44100_128",
            model_id="eleven_multilingual_sts_v2",
        )
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/speech-to-speech/{jsonable_encoder(voice_id)}",
            method="POST",
            params={
                "enable_logging": enable_logging,
                "optimize_streaming_latency": optimize_streaming_latency,
                "output_format": output_format,
            },
            data={
                "model_id": model_id,
                "voice_settings": voice_settings,
                "seed": seed,
                "remove_background_noise": remove_background_noise,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    for _chunk in _response.iter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                _response.read()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def convert_as_stream(
        self,
        voice_id: str,
        *,
        audio: core.File,
        enable_logging: typing.Optional[bool] = None,
        optimize_streaming_latency: typing.Optional[int] = None,
        output_format: typing.Optional[OutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        remove_background_noise: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Stream audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        audio : core.File
            See core.File for more documentation

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormat]
            The output format of the generated audio.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.Iterator[bytes]
            Streaming audio data

        Examples
        --------
        from elevenlabs import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.speech_to_speech.convert_as_stream(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            output_format="mp3_44100_128",
            model_id="eleven_multilingual_sts_v2",
        )
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/speech-to-speech/{jsonable_encoder(voice_id)}/stream",
            method="POST",
            params={
                "enable_logging": enable_logging,
                "optimize_streaming_latency": optimize_streaming_latency,
                "output_format": output_format,
            },
            data={
                "model_id": model_id,
                "voice_settings": voice_settings,
                "seed": seed,
                "remove_background_noise": remove_background_noise,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    for _chunk in _response.iter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                _response.read()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSpeechToSpeechClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def convert(
        self,
        voice_id: str,
        *,
        audio: core.File,
        enable_logging: typing.Optional[bool] = None,
        optimize_streaming_latency: typing.Optional[int] = None,
        output_format: typing.Optional[OutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        remove_background_noise: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Transform audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        audio : core.File
            See core.File for more documentation

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormat]
            The output format of the generated audio.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.AsyncIterator[bytes]
            The generated audio file

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.speech_to_speech.convert(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                output_format="mp3_44100_128",
                model_id="eleven_multilingual_sts_v2",
            )


        asyncio.run(main())
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/speech-to-speech/{jsonable_encoder(voice_id)}",
            method="POST",
            params={
                "enable_logging": enable_logging,
                "optimize_streaming_latency": optimize_streaming_latency,
                "output_format": output_format,
            },
            data={
                "model_id": model_id,
                "voice_settings": voice_settings,
                "seed": seed,
                "remove_background_noise": remove_background_noise,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                await _response.aread()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def convert_as_stream(
        self,
        voice_id: str,
        *,
        audio: core.File,
        enable_logging: typing.Optional[bool] = None,
        optimize_streaming_latency: typing.Optional[int] = None,
        output_format: typing.Optional[OutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        remove_background_noise: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Stream audio from one voice to another. Maintain full control over emotion, timing and delivery.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        audio : core.File
            See core.File for more documentation

        enable_logging : typing.Optional[bool]
            When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

        optimize_streaming_latency : typing.Optional[int]
            You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
            0 - default mode (no latency optimizations)
            1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
            2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
            3 - max latency optimizations
            4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

            Defaults to None.

        output_format : typing.Optional[OutputFormat]
            The output format of the generated audio.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

        voice_settings : typing.Optional[str]
            Voice settings overriding stored settings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        remove_background_noise : typing.Optional[bool]
            If set, will remove the background noise from your audio input using our audio isolation model. Only applies to Voice Changer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.AsyncIterator[bytes]
            Streaming audio data

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.speech_to_speech.convert_as_stream(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                output_format="mp3_44100_128",
                model_id="eleven_multilingual_sts_v2",
            )


        asyncio.run(main())
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/speech-to-speech/{jsonable_encoder(voice_id)}/stream",
            method="POST",
            params={
                "enable_logging": enable_logging,
                "optimize_streaming_latency": optimize_streaming_latency,
                "output_format": output_format,
            },
            data={
                "model_id": model_id,
                "voice_settings": voice_settings,
                "seed": seed,
                "remove_background_noise": remove_background_noise,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                await _response.aread()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)
