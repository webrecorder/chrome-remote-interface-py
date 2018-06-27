from collections import namedtuple
from cripy.gevent.protocol.runtime.types import *

__all__ = [
    "ConsoleAPICalledEvent",
    "ExceptionRevokedEvent",
    "ExceptionThrownEvent",
    "ExecutionContextCreatedEvent",
    "ExecutionContextDestroyedEvent",
    "ExecutionContextsClearedEvent",
    "InspectRequestedEvent",
    "RUNTIME_EVENTS_TO_CLASS",
    "RUNTIME_EVENTS_NS"
]


class ConsoleAPICalledEvent(object):
    """
    Issued when console API was called.
    """

    __slots__ = ["type", "args", "executionContextId", "timestamp", "stackTrace", "context"]

    def __init__(self, type, args, executionContextId, timestamp, stackTrace=None, context=None):
        """
        Create a new instance of ConsoleAPICalledEvent

        :param type: Type of the call.
        :type type: str
        :param args: Call arguments.
        :type args: List[dict]
        :param executionContextId: Identifier of the context where the call was made.
        :type executionContextId: int
        :param timestamp: Call timestamp.
        :type timestamp: float
        :param stackTrace: Stack trace captured when the call was made.
        :type stackTrace: Optional[dict]
        :param context: Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context.
        :type context: Optional[str]
        """
        super(ConsoleAPICalledEvent, self).__init__()
        self.type = type
        self.args = RemoteObject.safe_create_from_list(args)
        self.executionContextId = executionContextId
        self.timestamp = timestamp
        self.stackTrace = StackTrace.safe_create(stackTrace)
        self.context = context

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.args is not None:
            repr_args.append("args={!r}".format(self.args))
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.stackTrace is not None:
            repr_args.append("stackTrace={!r}".format(self.stackTrace))
        if self.context is not None:
            repr_args.append("context={!r}".format(self.context))
        return "ConsoleAPICalledEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ConsoleAPICalledEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ConsoleAPICalledEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ConsoleAPICalledEvent if creation did not fail
        :rtype: Optional[Union[dict, ConsoleAPICalledEvent]]
        """
        if init is not None:
            try:
                ourselves = ConsoleAPICalledEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ConsoleAPICalledEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ConsoleAPICalledEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ConsoleAPICalledEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ConsoleAPICalledEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleAPICalledEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExceptionRevokedEvent(object):
    """
    Issued when unhandled exception was revoked.
    """

    __slots__ = ["reason", "exceptionId"]

    def __init__(self, reason, exceptionId):
        """
        Create a new instance of ExceptionRevokedEvent

        :param reason: Reason describing why exception was revoked.
        :type reason: str
        :param exceptionId: The id of revoked exception, as reported in `exceptionThrown`.
        :type exceptionId: int
        """
        super(ExceptionRevokedEvent, self).__init__()
        self.reason = reason
        self.exceptionId = exceptionId

    def __repr__(self):
        repr_args = []
        if self.reason is not None:
            repr_args.append("reason={!r}".format(self.reason))
        if self.exceptionId is not None:
            repr_args.append("exceptionId={!r}".format(self.exceptionId))
        return "ExceptionRevokedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ExceptionRevokedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ExceptionRevokedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ExceptionRevokedEvent if creation did not fail
        :rtype: Optional[Union[dict, ExceptionRevokedEvent]]
        """
        if init is not None:
            try:
                ourselves = ExceptionRevokedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ExceptionRevokedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ExceptionRevokedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ExceptionRevokedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ExceptionRevokedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionRevokedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExceptionThrownEvent(object):
    """
    Issued when exception was thrown and unhandled.
    """

    __slots__ = ["timestamp", "exceptionDetails"]

    def __init__(self, timestamp, exceptionDetails):
        """
        Create a new instance of ExceptionThrownEvent

        :param timestamp: Timestamp of the exception.
        :type timestamp: float
        :param exceptionDetails: The exceptionDetails
        :type exceptionDetails: dict
        """
        super(ExceptionThrownEvent, self).__init__()
        self.timestamp = timestamp
        self.exceptionDetails = ExceptionDetails.safe_create(exceptionDetails)

    def __repr__(self):
        repr_args = []
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.exceptionDetails is not None:
            repr_args.append("exceptionDetails={!r}".format(self.exceptionDetails))
        return "ExceptionThrownEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ExceptionThrownEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ExceptionThrownEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ExceptionThrownEvent if creation did not fail
        :rtype: Optional[Union[dict, ExceptionThrownEvent]]
        """
        if init is not None:
            try:
                ourselves = ExceptionThrownEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ExceptionThrownEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ExceptionThrownEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ExceptionThrownEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ExceptionThrownEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionThrownEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextCreatedEvent(object):
    """
    Issued when new execution context is created.
    """

    __slots__ = ["context"]

    def __init__(self, context):
        """
        Create a new instance of ExecutionContextCreatedEvent

        :param context: A newly created execution context.
        :type context: dict
        """
        super(ExecutionContextCreatedEvent, self).__init__()
        self.context = ExecutionContextDescription.safe_create(context)

    def __repr__(self):
        repr_args = []
        if self.context is not None:
            repr_args.append("context={!r}".format(self.context))
        return "ExecutionContextCreatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ExecutionContextCreatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ExecutionContextCreatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ExecutionContextCreatedEvent if creation did not fail
        :rtype: Optional[Union[dict, ExecutionContextCreatedEvent]]
        """
        if init is not None:
            try:
                ourselves = ExecutionContextCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ExecutionContextCreatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ExecutionContextCreatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ExecutionContextCreatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ExecutionContextCreatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextCreatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextDestroyedEvent(object):
    """
    Issued when execution context is destroyed.
    """

    __slots__ = ["executionContextId"]

    def __init__(self, executionContextId):
        """
        Create a new instance of ExecutionContextDestroyedEvent

        :param executionContextId: Id of the destroyed context
        :type executionContextId: int
        """
        super(ExecutionContextDestroyedEvent, self).__init__()
        self.executionContextId = executionContextId

    def __repr__(self):
        repr_args = []
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        return "ExecutionContextDestroyedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ExecutionContextDestroyedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ExecutionContextDestroyedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ExecutionContextDestroyedEvent if creation did not fail
        :rtype: Optional[Union[dict, ExecutionContextDestroyedEvent]]
        """
        if init is not None:
            try:
                ourselves = ExecutionContextDestroyedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ExecutionContextDestroyedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ExecutionContextDestroyedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ExecutionContextDestroyedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ExecutionContextDestroyedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextDestroyedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextsClearedEvent(dict):
    """
    Issued when all executionContexts were cleared in browser
    """

    def __repr__(self):
        return "ExecutionContextsClearedEvent(dict)"

    @staticmethod
    def safe_create(init):
        """
        Safely create ExecutionContextsClearedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ExecutionContextsClearedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ExecutionContextsClearedEvent if creation did not fail
        :rtype: Optional[Union[dict, ExecutionContextsClearedEvent]]
        """
        if init is not None:
            try:
                ourselves = ExecutionContextsClearedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ExecutionContextsClearedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ExecutionContextsClearedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ExecutionContextsClearedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ExecutionContextsClearedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextsClearedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class InspectRequestedEvent(object):
    """
    Issued when object should be inspected (for example, as a result of inspect() command line API call).
    """

    __slots__ = ["object", "hints"]

    def __init__(self, object, hints):
        """
        Create a new instance of InspectRequestedEvent

        :param object: The object
        :type object: dict
        :param hints: The hints
        :type hints: dict
        """
        super(InspectRequestedEvent, self).__init__()
        self.object = RemoteObject.safe_create(object)
        self.hints = hints

    def __repr__(self):
        repr_args = []
        if self.object is not None:
            repr_args.append("object={!r}".format(self.object))
        if self.hints is not None:
            repr_args.append("hints={!r}".format(self.hints))
        return "InspectRequestedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create InspectRequestedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of InspectRequestedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of InspectRequestedEvent if creation did not fail
        :rtype: Optional[Union[dict, InspectRequestedEvent]]
        """
        if init is not None:
            try:
                ourselves = InspectRequestedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list InspectRequestedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list InspectRequestedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of InspectRequestedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, InspectRequestedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InspectRequestedEvent.safe_create(it))
            return list_of_self
        else:
            return init


RUNTIME_EVENTS_TO_CLASS = {
   "Runtime.consoleAPICalled": ConsoleAPICalledEvent,
   "Runtime.exceptionRevoked": ExceptionRevokedEvent,
   "Runtime.exceptionThrown": ExceptionThrownEvent,
   "Runtime.executionContextCreated": ExecutionContextCreatedEvent,
   "Runtime.executionContextDestroyed": ExecutionContextDestroyedEvent,
   "Runtime.executionContextsCleared": ExecutionContextsClearedEvent,
   "Runtime.inspectRequested": InspectRequestedEvent,
}

RuntimeNS = namedtuple("RuntimeNS", ["ConsoleAPICalled", "ExceptionRevoked", "ExceptionThrown", "ExecutionContextCreated", "ExecutionContextDestroyed", "ExecutionContextsCleared", "InspectRequested"])

RUNTIME_EVENTS_NS = RuntimeNS(
  ConsoleAPICalled="Runtime.consoleAPICalled",
  ExceptionRevoked="Runtime.exceptionRevoked",
  ExceptionThrown="Runtime.exceptionThrown",
  ExecutionContextCreated="Runtime.executionContextCreated",
  ExecutionContextDestroyed="Runtime.executionContextDestroyed",
  ExecutionContextsCleared="Runtime.executionContextsCleared",
  InspectRequested="Runtime.inspectRequested",
)
