from collections import namedtuple
from cripy.gevent.protocol.target.types import *

__all__ = [
    "AttachedToTargetEvent",
    "DetachedFromTargetEvent",
    "ReceivedMessageFromTargetEvent",
    "TargetCreatedEvent",
    "TargetDestroyedEvent",
    "TargetInfoChangedEvent",
    "TARGET_EVENTS_TO_CLASS",
    "TARGET_EVENTS_NS"
]


class AttachedToTargetEvent(object):
    """
    Issued when attached to target because of auto-attach or `attachToTarget` command.
    """

    __slots__ = ["sessionId", "targetInfo", "waitingForDebugger"]

    def __init__(self, sessionId, targetInfo, waitingForDebugger):
        """
        Create a new instance of AttachedToTargetEvent

        :param sessionId: Identifier assigned to the session used to send/receive messages.
        :type sessionId: str
        :param targetInfo: The targetInfo
        :type targetInfo: dict
        :param waitingForDebugger: The waitingForDebugger
        :type waitingForDebugger: bool
        """
        super(AttachedToTargetEvent, self).__init__()
        self.sessionId = sessionId
        self.targetInfo = TargetInfo.safe_create(targetInfo)
        self.waitingForDebugger = waitingForDebugger

    def __repr__(self):
        repr_args = []
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        if self.targetInfo is not None:
            repr_args.append("targetInfo={!r}".format(self.targetInfo))
        if self.waitingForDebugger is not None:
            repr_args.append("waitingForDebugger={!r}".format(self.waitingForDebugger))
        return "AttachedToTargetEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AttachedToTargetEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AttachedToTargetEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AttachedToTargetEvent if creation did not fail
        :rtype: Optional[Union[dict, AttachedToTargetEvent]]
        """
        if init is not None:
            try:
                ourselves = AttachedToTargetEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list AttachedToTargetEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AttachedToTargetEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AttachedToTargetEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AttachedToTargetEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttachedToTargetEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DetachedFromTargetEvent(object):
    """
    Issued when detached from target for any reason (including `detachFromTarget` command).
	Can be issued multiple times per target if multiple sessions have been attached to it.
    """

    __slots__ = ["sessionId", "targetId"]

    def __init__(self, sessionId, targetId=None):
        """
        Create a new instance of DetachedFromTargetEvent

        :param sessionId: Detached session identifier.
        :type sessionId: str
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        super(DetachedFromTargetEvent, self).__init__()
        self.sessionId = sessionId
        self.targetId = targetId

    def __repr__(self):
        repr_args = []
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "DetachedFromTargetEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create DetachedFromTargetEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DetachedFromTargetEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DetachedFromTargetEvent if creation did not fail
        :rtype: Optional[Union[dict, DetachedFromTargetEvent]]
        """
        if init is not None:
            try:
                ourselves = DetachedFromTargetEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list DetachedFromTargetEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DetachedFromTargetEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DetachedFromTargetEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DetachedFromTargetEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DetachedFromTargetEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ReceivedMessageFromTargetEvent(object):
    """
    Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event).
    """

    __slots__ = ["sessionId", "message", "targetId"]

    def __init__(self, sessionId, message, targetId=None):
        """
        Create a new instance of ReceivedMessageFromTargetEvent

        :param sessionId: Identifier of a session which sends a message.
        :type sessionId: str
        :param message: The message
        :type message: str
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        super(ReceivedMessageFromTargetEvent, self).__init__()
        self.sessionId = sessionId
        self.message = message
        self.targetId = targetId

    def __repr__(self):
        repr_args = []
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "ReceivedMessageFromTargetEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ReceivedMessageFromTargetEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ReceivedMessageFromTargetEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ReceivedMessageFromTargetEvent if creation did not fail
        :rtype: Optional[Union[dict, ReceivedMessageFromTargetEvent]]
        """
        if init is not None:
            try:
                ourselves = ReceivedMessageFromTargetEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ReceivedMessageFromTargetEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ReceivedMessageFromTargetEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ReceivedMessageFromTargetEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ReceivedMessageFromTargetEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ReceivedMessageFromTargetEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetCreatedEvent(object):
    """
    Issued when a possible inspection target is created.
    """

    __slots__ = ["targetInfo"]

    def __init__(self, targetInfo):
        """
        Create a new instance of TargetCreatedEvent

        :param targetInfo: The targetInfo
        :type targetInfo: dict
        """
        super(TargetCreatedEvent, self).__init__()
        self.targetInfo = TargetInfo.safe_create(targetInfo)

    def __repr__(self):
        repr_args = []
        if self.targetInfo is not None:
            repr_args.append("targetInfo={!r}".format(self.targetInfo))
        return "TargetCreatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TargetCreatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TargetCreatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TargetCreatedEvent if creation did not fail
        :rtype: Optional[Union[dict, TargetCreatedEvent]]
        """
        if init is not None:
            try:
                ourselves = TargetCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list TargetCreatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TargetCreatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TargetCreatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, TargetCreatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetCreatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetDestroyedEvent(object):
    """
    Issued when a target is destroyed.
    """

    __slots__ = ["targetId"]

    def __init__(self, targetId):
        """
        Create a new instance of TargetDestroyedEvent

        :param targetId: The targetId
        :type targetId: str
        """
        super(TargetDestroyedEvent, self).__init__()
        self.targetId = targetId

    def __repr__(self):
        repr_args = []
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "TargetDestroyedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TargetDestroyedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TargetDestroyedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TargetDestroyedEvent if creation did not fail
        :rtype: Optional[Union[dict, TargetDestroyedEvent]]
        """
        if init is not None:
            try:
                ourselves = TargetDestroyedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list TargetDestroyedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TargetDestroyedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TargetDestroyedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, TargetDestroyedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetDestroyedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetInfoChangedEvent(object):
    """
    Issued when some information about a target has changed.
	This only happens between `targetCreated` and `targetDestroyed`.
    """

    __slots__ = ["targetInfo"]

    def __init__(self, targetInfo):
        """
        Create a new instance of TargetInfoChangedEvent

        :param targetInfo: The targetInfo
        :type targetInfo: dict
        """
        super(TargetInfoChangedEvent, self).__init__()
        self.targetInfo = TargetInfo.safe_create(targetInfo)

    def __repr__(self):
        repr_args = []
        if self.targetInfo is not None:
            repr_args.append("targetInfo={!r}".format(self.targetInfo))
        return "TargetInfoChangedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TargetInfoChangedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TargetInfoChangedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TargetInfoChangedEvent if creation did not fail
        :rtype: Optional[Union[dict, TargetInfoChangedEvent]]
        """
        if init is not None:
            try:
                ourselves = TargetInfoChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list TargetInfoChangedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TargetInfoChangedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TargetInfoChangedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, TargetInfoChangedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetInfoChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


TARGET_EVENTS_TO_CLASS = {
   "Target.attachedToTarget": AttachedToTargetEvent,
   "Target.detachedFromTarget": DetachedFromTargetEvent,
   "Target.receivedMessageFromTarget": ReceivedMessageFromTargetEvent,
   "Target.targetCreated": TargetCreatedEvent,
   "Target.targetDestroyed": TargetDestroyedEvent,
   "Target.targetInfoChanged": TargetInfoChangedEvent,
}

TargetNS = namedtuple("TargetNS", ["AttachedToTarget", "DetachedFromTarget", "ReceivedMessageFromTarget", "TargetCreated", "TargetDestroyed", "TargetInfoChanged"])

TARGET_EVENTS_NS = TargetNS(
  AttachedToTarget="Target.attachedToTarget",
  DetachedFromTarget="Target.detachedFromTarget",
  ReceivedMessageFromTarget="Target.receivedMessageFromTarget",
  TargetCreated="Target.targetCreated",
  TargetDestroyed="Target.targetDestroyed",
  TargetInfoChanged="Target.targetInfoChanged",
)
