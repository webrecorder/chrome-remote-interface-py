from typing import Any, List, Optional, Union
from cripy.async.protocol.storage import events as Events
from cripy.async.protocol.storage import types as Types


class Storage(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def clearDataForOrigin(
        self, origin: str, storageTypes: str
    ) -> Optional[dict]:
        """
        :param origin: Security origin.
        :type origin: str
        :param storageTypes: Comma separated origin names.
        :type storageTypes: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        if storageTypes is not None:
            msg_dict["storageTypes"] = storageTypes
        mayberes = await self.chrome.send("Storage.clearDataForOrigin", msg_dict)
        return mayberes

    async def getUsageAndQuota(self, origin: str) -> Optional[dict]:
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        mayberes = await self.chrome.send("Storage.getUsageAndQuota", msg_dict)
        res = await mayberes
        res["usageBreakdown"] = Types.UsageForType.safe_create_from_list(
            res["usageBreakdown"]
        )
        return res

    async def trackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        mayberes = await self.chrome.send(
            "Storage.trackCacheStorageForOrigin", msg_dict
        )
        return mayberes

    async def trackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        mayberes = await self.chrome.send("Storage.trackIndexedDBForOrigin", msg_dict)
        return mayberes

    async def untrackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        mayberes = await self.chrome.send(
            "Storage.untrackCacheStorageForOrigin", msg_dict
        )
        return mayberes

    async def untrackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        mayberes = await self.chrome.send("Storage.untrackIndexedDBForOrigin", msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS