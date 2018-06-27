from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.page import types as Page
from cripy.asyncio.protocol.runtime import types as Runtime
from cripy.asyncio.protocol.dom import types as DOM
from cripy.asyncio.protocol.overlay import events as Events
from cripy.asyncio.protocol.overlay import types as Types

__all__ = ["Overlay"]


class Overlay(object):
    """
    This domain provides various functionality related to drawing atop the inspected page.
    """

    dependencies = ['DOM', 'Page', 'Runtime']

    events = Events.OVERLAY_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Overlay object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        """
        Disables domain notifications.
        """
        res = await self.chrome.send('Overlay.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables domain notifications.
        """
        res = await self.chrome.send('Overlay.enable')
        return res

    async def getHighlightObjectForTest(self, nodeId: int) -> Optional[dict]:
        """
        For testing.

        :param nodeId: Id of the node to get highlight object for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('Overlay.getHighlightObjectForTest', msg_dict)
        return res

    async def hideHighlight(self) -> Optional[dict]:
        """
        Hides any highlight.
        """
        res = await self.chrome.send('Overlay.hideHighlight')
        return res

    async def highlightFrame(self, frameId: str, contentColor: Optional[dict] = None, contentOutlineColor: Optional[dict] = None) -> Optional[dict]:
        """
        Highlights owner element of the frame with given id.

        :param frameId: Identifier of the frame to highlight.
        :type frameId: str
        :param contentColor: The content box highlight fill color (default: transparent).
        :type contentColor: Optional[dict]
        :param contentOutlineColor: The content box highlight outline color (default: transparent).
        :type contentOutlineColor: Optional[dict]
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        if contentColor is not None:
            msg_dict['contentColor'] = contentColor
        if contentOutlineColor is not None:
            msg_dict['contentOutlineColor'] = contentOutlineColor
        res = await self.chrome.send('Overlay.highlightFrame', msg_dict)
        return res

    async def highlightNode(self, highlightConfig: dict, nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectId: Optional[str] = None) -> Optional[dict]:
        """
        Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
objectId must be specified.

        :param highlightConfig: A descriptor for the highlight appearance.
        :type highlightConfig: dict
        :param nodeId: Identifier of the node to highlight.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node to highlight.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node to be highlighted.
        :type objectId: Optional[str]
        """
        msg_dict = dict()
        if highlightConfig is not None:
            msg_dict['highlightConfig'] = highlightConfig
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        res = await self.chrome.send('Overlay.highlightNode', msg_dict)
        return res

    async def highlightQuad(self, quad: list, color: Optional[dict] = None, outlineColor: Optional[dict] = None) -> Optional[dict]:
        """
        Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

        :param quad: Quad to highlight
        :type quad: Any
        :param color: The highlight fill color (default: transparent).
        :type color: Optional[dict]
        :param outlineColor: The highlight outline color (default: transparent).
        :type outlineColor: Optional[dict]
        """
        msg_dict = dict()
        if quad is not None:
            msg_dict['quad'] = quad
        if color is not None:
            msg_dict['color'] = color
        if outlineColor is not None:
            msg_dict['outlineColor'] = outlineColor
        res = await self.chrome.send('Overlay.highlightQuad', msg_dict)
        return res

    async def highlightRect(self, x: int, y: int, width: int, height: int, color: Optional[dict] = None, outlineColor: Optional[dict] = None) -> Optional[dict]:
        """
        Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

        :param x: X coordinate
        :type x: int
        :param y: Y coordinate
        :type y: int
        :param width: Rectangle width
        :type width: int
        :param height: Rectangle height
        :type height: int
        :param color: The highlight fill color (default: transparent).
        :type color: Optional[dict]
        :param outlineColor: The highlight outline color (default: transparent).
        :type outlineColor: Optional[dict]
        """
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if width is not None:
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        if color is not None:
            msg_dict['color'] = color
        if outlineColor is not None:
            msg_dict['outlineColor'] = outlineColor
        res = await self.chrome.send('Overlay.highlightRect', msg_dict)
        return res

    async def setInspectMode(self, mode: str, highlightConfig: Optional[dict] = None) -> Optional[dict]:
        """
        Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
Backend then generates 'inspectNodeRequested' event upon element selection.

        :param mode: Set an inspection mode.
        :type mode: str
        :param highlightConfig: A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled == false`.
        :type highlightConfig: Optional[dict]
        """
        msg_dict = dict()
        if mode is not None:
            msg_dict['mode'] = mode
        if highlightConfig is not None:
            msg_dict['highlightConfig'] = highlightConfig
        res = await self.chrome.send('Overlay.setInspectMode', msg_dict)
        return res

    async def setPausedInDebuggerMessage(self, message: Optional[str] = None) -> Optional[dict]:
        """
        :param message: The message to display, also triggers resume and step over controls.
        :type message: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict['message'] = message
        res = await self.chrome.send('Overlay.setPausedInDebuggerMessage', msg_dict)
        return res

    async def setShowDebugBorders(self, show: bool) -> Optional[dict]:
        """
        Requests that backend shows debug borders on layers

        :param show: True for showing debug borders
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        res = await self.chrome.send('Overlay.setShowDebugBorders', msg_dict)
        return res

    async def setShowFPSCounter(self, show: bool) -> Optional[dict]:
        """
        Requests that backend shows the FPS counter

        :param show: True for showing the FPS counter
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        res = await self.chrome.send('Overlay.setShowFPSCounter', msg_dict)
        return res

    async def setShowPaintRects(self, result: bool) -> Optional[dict]:
        """
        Requests that backend shows paint rectangles

        :param result: True for showing paint rectangles
        :type result: bool
        """
        msg_dict = dict()
        if result is not None:
            msg_dict['result'] = result
        res = await self.chrome.send('Overlay.setShowPaintRects', msg_dict)
        return res

    async def setShowScrollBottleneckRects(self, show: bool) -> Optional[dict]:
        """
        Requests that backend shows scroll bottleneck rects

        :param show: True for showing scroll bottleneck rects
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        res = await self.chrome.send('Overlay.setShowScrollBottleneckRects', msg_dict)
        return res

    async def setShowViewportSizeOnResize(self, show: bool) -> Optional[dict]:
        """
        Paints viewport size upon main frame resize.

        :param show: Whether to paint size or not.
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        res = await self.chrome.send('Overlay.setShowViewportSizeOnResize', msg_dict)
        return res

    async def setSuspended(self, suspended: bool) -> Optional[dict]:
        """
        :param suspended: Whether overlay should be suspended and not consume any resources until resumed.
        :type suspended: bool
        """
        msg_dict = dict()
        if suspended is not None:
            msg_dict['suspended'] = suspended
        res = await self.chrome.send('Overlay.setSuspended', msg_dict)
        return res

    def inspectNodeRequested(self, fn, once=False):
        if once:
            self.chrome.once("Overlay.inspectNodeRequested", fn)
        else:
            self.chrome.on("Overlay.inspectNodeRequested", fn)

    def nodeHighlightRequested(self, fn, once=False):
        if once:
            self.chrome.once("Overlay.nodeHighlightRequested", fn)
        else:
            self.chrome.on("Overlay.nodeHighlightRequested", fn)

    def screenshotRequested(self, fn, once=False):
        if once:
            self.chrome.once("Overlay.screenshotRequested", fn)
        else:
            self.chrome.on("Overlay.screenshotRequested", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.OVERLAY_EVENTS_TO_CLASS

