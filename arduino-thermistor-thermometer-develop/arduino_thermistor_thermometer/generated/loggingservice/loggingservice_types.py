# Generated by sila2.code_generator; sila2.__version__: 0.12.2
from __future__ import annotations

from typing import Any, List, NamedTuple


class GetLogFile_Responses(NamedTuple):

    LogFile: str
    """
    Log File as text
    """


class SetLogLevel_Responses(NamedTuple):

    pass


class ListenToLoggingStream_Responses(NamedTuple):

    pass


class ListenToAllLogEntries_Responses(NamedTuple):

    pass


class ListenToLoggingStream_IntermediateResponses(NamedTuple):

    IntermediateLoggingText: str
    """
    The current logging text of a certain logging stream as it is created by the server
    """


class ListenToAllLogEntries_IntermediateResponses(NamedTuple):

    IntermediateLoggingEntry: List[LogEntry]
    """
    Intermediate Log Entries as they are created by the server
    """


Severity = str

LogEntry = Any