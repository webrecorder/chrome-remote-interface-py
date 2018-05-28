from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class ConsoleProfileFinishedEvent(BaseEvent):

    event: str = "Profiler.consoleProfileFinished"

    def __init__(self) -> None:
        """
        :param str id: The id
        :param Debugger.Location location: Location of console.profileEnd().
        :param Profile profile: The profile
        :param str title: Profile title passed as an argument to console.profile().
        """
        super().__init__()


class ConsoleProfileStartedEvent(BaseEvent):
    """Sent when new profile recording is started using console.profile() call."""

    event: str = "Profiler.consoleProfileStarted"

    def __init__(self) -> None:
        """
        :param str id: The id
        :param Debugger.Location location: Location of console.profile().
        :param str title: Profile title passed as an argument to console.profile().
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Profiler.consoleProfileFinished": ConsoleProfileFinishedEvent,
   "Profiler.consoleProfileStarted": ConsoleProfileStartedEvent,
}

