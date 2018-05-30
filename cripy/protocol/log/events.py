from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.log.types import (
    LogEntry,
)


class EntryAddedEvent(BaseEvent):
    """
    Issued when new message was logged.
    """

    event = "Log.entryAdded"

    def __init__(self, entry: Union[LogEntry, dict]) -> None:
        """
        :param entry: The entry.
        :type entry: dict
        """
        super().__init__()
        self.entry = LogEntry.safe_create(entry)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['EntryAddedEvent']:
        if init is not None:
            return EntryAddedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['EntryAddedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EntryAddedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Log.entryAdded": EntryAddedEvent,
}
