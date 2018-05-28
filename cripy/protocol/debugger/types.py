from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase
from cripy.protocol.runtime import types as Runtime

CallFrameId = TypeVar("CallFrameId", str, str)
"""Call frame identifier."""

BreakpointId = TypeVar("BreakpointId", str, str)
"""Breakpoint identifier."""


class SearchMatch(ChromeTypeBase):
    """Search match for resource."""
    def __init__(self, lineNumber: float, lineContent: str) -> None:
        """
        :param lineNumber: Line number in resource content.
        :type lineNumber: float
        :param lineContent: Line with match content.
        :type lineContent: str
        """
        super().__init__()
        self.lineNumber: float = lineNumber
        self.lineContent: str = lineContent


class ScriptPosition(ChromeTypeBase):
    """Location in the source code."""
    def __init__(self, lineNumber: int, columnNumber: int) -> None:
        """
        :param lineNumber: The lineNumber
        :type lineNumber: int
        :param columnNumber: The columnNumber
        :type columnNumber: int
        """
        super().__init__()
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


class Scope(ChromeTypeBase):
    """Scope description."""
    def __init__(self, type: str, object: 'Runtime.RemoteObject', name: Optional[str] = None, startLocation: Optional['Location'] = None, endLocation: Optional['Location'] = None) -> None:
        """
        :param type: Scope type.
        :type type: str
        :param object: Object representing the scope. For `global` and `with` scopes it represents the actual object; for the rest of the scopes, it is artificial transient object enumerating scope variables as its properties.
        :type object: Runtime.RemoteObject
        :param name: The name
        :type name: str
        :param startLocation: Location in the source code where scope starts
        :type startLocation: Location
        :param endLocation: Location in the source code where scope ends
        :type endLocation: Location
        """
        super().__init__()
        self.type: str = type
        self.object: Runtime.RemoteObject = object
        self.name: Optional[str] = name
        self.startLocation: Optional[Location] = startLocation
        self.endLocation: Optional[Location] = endLocation


class Location(ChromeTypeBase):
    """Location in the source code."""
    def __init__(self, scriptId: 'Runtime.ScriptId', lineNumber: int, columnNumber: Optional[int] = None) -> None:
        """
        :param scriptId: Script identifier as reported in the `Debugger.scriptParsed`.
        :type scriptId: Runtime.ScriptId
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: int
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: Optional[int] = columnNumber


class CallFrame(ChromeTypeBase):
    """JavaScript call frame. Array of call frames form the call stack."""
    def __init__(self, callFrameId: 'CallFrameId', functionName: str, location: 'Location', url: str, scopeChain: List['Scope'], this: 'Runtime.RemoteObject', functionLocation: Optional['Location'] = None, returnValue: Optional['Runtime.RemoteObject'] = None) -> None:
        """
        :param callFrameId: Call frame identifier. This identifier is only valid while the virtual machine is paused.
        :type callFrameId: CallFrameId
        :param functionName: Name of the JavaScript function called on this call frame.
        :type functionName: str
        :param functionLocation: Location in the source code.
        :type functionLocation: Location
        :param location: Location in the source code.
        :type location: Location
        :param url: JavaScript script name or url.
        :type url: str
        :param scopeChain: Scope chain for this call frame.
        :type scopeChain: array
        :param this: `this` object for this call frame.
        :type this: Runtime.RemoteObject
        :param returnValue: The value being returned, if the function is at return point.
        :type returnValue: Runtime.RemoteObject
        """
        super().__init__()
        self.callFrameId: CallFrameId = callFrameId
        self.functionName: str = functionName
        self.functionLocation: Optional[Location] = functionLocation
        self.location: Location = location
        self.url: str = url
        self.scopeChain: List[Scope] = scopeChain
        self.this: Runtime.RemoteObject = this
        self.returnValue: Optional[Runtime.RemoteObject] = returnValue


class BreakLocation(ChromeTypeBase):
    def __init__(self, scriptId: 'Runtime.ScriptId', lineNumber: int, columnNumber: Optional[int] = None, type: Optional[str] = None) -> None:
        """
        :param scriptId: Script identifier as reported in the `Debugger.scriptParsed`.
        :type scriptId: Runtime.ScriptId
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: int
        :param type: The type
        :type type: str
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: Optional[int] = columnNumber
        self.type: Optional[str] = type


