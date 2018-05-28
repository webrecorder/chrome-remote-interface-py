from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class FontsUpdatedEvent(BaseEvent):
    """Fires whenever a web font is updated.
	 A non-empty font parameter indicates a successfully loaded web font"""

    event: str = "CSS.fontsUpdated"

    def __init__(self) -> None:
        """
        :param FontFace font: The web font that has loaded.
        """
        super().__init__()


class MediaQueryResultChangedEvent(BaseEvent):
    """Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features."""

    event: str = "CSS.mediaQueryResultChanged"

    def __init__(self) -> None:
        super().__init__()


class StyleSheetAddedEvent(BaseEvent):
    """Fired whenever an active document stylesheet is added."""

    event: str = "CSS.styleSheetAdded"

    def __init__(self) -> None:
        """
        :param CSSStyleSheetHeader header: Added stylesheet metainfo.
        """
        super().__init__()


class StyleSheetChangedEvent(BaseEvent):
    """Fired whenever a stylesheet is changed as a result of the client operation."""

    event: str = "CSS.styleSheetChanged"

    def __init__(self) -> None:
        """
        :param StyleSheetId styleSheetId: The styleSheetId
        """
        super().__init__()


class StyleSheetRemovedEvent(BaseEvent):
    """Fired whenever an active document stylesheet is removed."""

    event: str = "CSS.styleSheetRemoved"

    def __init__(self) -> None:
        """
        :param StyleSheetId styleSheetId: Identifier of the removed stylesheet.
        """
        super().__init__()


EVENT_TO_CLASS = {
   "CSS.fontsUpdated": FontsUpdatedEvent,
   "CSS.mediaQueryResultChanged": MediaQueryResultChangedEvent,
   "CSS.styleSheetAdded": StyleSheetAddedEvent,
   "CSS.styleSheetChanged": StyleSheetChangedEvent,
   "CSS.styleSheetRemoved": StyleSheetRemovedEvent,
}

