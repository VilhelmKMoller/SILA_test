# Generated by sila2.code_generator; sila2.__version__: 0.12.2
# -----
# This class does not do anything useful at runtime. Its only purpose is to provide type annotations.
# Since sphinx does not support .pyi files (yet?), this is a .py file.
# -----

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from typing import Iterable, List, Optional

    from loggingservice_types import (
        GetLogFile_Responses,
        ListenToAllLogEntries_IntermediateResponses,
        ListenToAllLogEntries_Responses,
        ListenToLoggingStream_IntermediateResponses,
        ListenToLoggingStream_Responses,
        SetLogLevel_Responses,
    )
    from sila2.client import (
        ClientMetadataInstance,
        ClientObservableCommandInstanceWithIntermediateResponses,
        ClientUnobservableProperty,
    )


class LoggingServiceClient:
    """
    Provides services for integration of SiLA server logging.
    The service is intended to be used by the server to provide logging information to the client.
    The client can use the service to listen for log entries from the server.
    It is possible to listen for all log entries or only for log entries from a specific Stream.
    Error handling: If the server is not able to provide the requested information, it shall return an error message.

    """

    LoggingStreamList: ClientUnobservableProperty[List[str]]
    """
    Provides a list of URLs of all logging streams that are currently available on the server.
    """

    LogFileList: ClientUnobservableProperty[List[str]]
    """
    Provides a list of URLs of all log files that are currently available on the server.
    """

    LogLevel: ClientUnobservableProperty[str]
    """
    The current log level of the server.
    """

    def GetLogFile(
        self, LogFileName: str, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None
    ) -> GetLogFile_Responses:
        """
        Gets the log file from the server.
        """
        ...

    def SetLogLevel(
        self, LogLevel: str, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None
    ) -> SetLogLevel_Responses:
        """
        Sets the log level of the server.
        """
        ...

    def ListenToLoggingStream(
        self, LoggingStreamName: str, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None
    ) -> ClientObservableCommandInstanceWithIntermediateResponses[
        ListenToLoggingStream_IntermediateResponses, ListenToLoggingStream_Responses
    ]:
        """
        Starts listening to a logging stream from the SiLA server
        """
        ...

    def ListenToAllLogEntries(
        self, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None
    ) -> ClientObservableCommandInstanceWithIntermediateResponses[
        ListenToAllLogEntries_IntermediateResponses, ListenToAllLogEntries_Responses
    ]:
        """
        Starts listening to a stream of all consecutive log entries from the SiLA server
        """
        ...
