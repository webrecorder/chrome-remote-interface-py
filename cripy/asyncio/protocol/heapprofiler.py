from typing import Any, List, Optional, Union


__all__ = ["HeapProfiler"]


class HeapProfiler(object):
    dependencies = ['Runtime']


    def __init__(self, chrome):
        """
        Construct a new HeapProfiler object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def addInspectedHeapObject(self, heapObjectId: str) -> Optional[dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :type heapObjectId: str
        """
        msg_dict = dict()
        if heapObjectId is not None:
            msg_dict['heapObjectId'] = heapObjectId
        res = await self.chrome.send('HeapProfiler.addInspectedHeapObject', msg_dict)
        return res

    async def collectGarbage(self) -> Optional[dict]:
        res = await self.chrome.send('HeapProfiler.collectGarbage')
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('HeapProfiler.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('HeapProfiler.enable')
        return res

    async def getHeapObjectId(self, objectId: str) -> Optional[dict]:
        """
        :param objectId: Identifier of the object to get heap object id for.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        res = await self.chrome.send('HeapProfiler.getHeapObjectId', msg_dict)
        return res

    async def getObjectByHeapObjectId(self, objectId: str, objectGroup: Optional[str] = None) -> Optional[dict]:
        """
        :param objectId: The objectId
        :type objectId: str
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        res = await self.chrome.send('HeapProfiler.getObjectByHeapObjectId', msg_dict)
        return res

    async def getSamplingProfile(self) -> Optional[dict]:
        res = await self.chrome.send('HeapProfiler.getSamplingProfile')
        return res

    async def startSampling(self, samplingInterval: Optional[float] = None) -> Optional[dict]:
        """
        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        :type samplingInterval: Optional[float]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict['samplingInterval'] = samplingInterval
        res = await self.chrome.send('HeapProfiler.startSampling', msg_dict)
        return res

    async def startTrackingHeapObjects(self, trackAllocations: Optional[bool] = None) -> Optional[dict]:
        """
        :param trackAllocations: The trackAllocations
        :type trackAllocations: Optional[bool]
        """
        msg_dict = dict()
        if trackAllocations is not None:
            msg_dict['trackAllocations'] = trackAllocations
        res = await self.chrome.send('HeapProfiler.startTrackingHeapObjects', msg_dict)
        return res

    async def stopSampling(self) -> Optional[dict]:
        res = await self.chrome.send('HeapProfiler.stopSampling')
        return res

    async def stopTrackingHeapObjects(self, reportProgress: Optional[bool] = None) -> Optional[dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict['reportProgress'] = reportProgress
        res = await self.chrome.send('HeapProfiler.stopTrackingHeapObjects', msg_dict)
        return res

    async def takeHeapSnapshot(self, reportProgress: Optional[bool] = None) -> Optional[dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict['reportProgress'] = reportProgress
        res = await self.chrome.send('HeapProfiler.takeHeapSnapshot', msg_dict)
        return res

    def addHeapSnapshotChunk(self, fn, once=False) -> None:
        if once:
            self.chrome.once("HeapProfiler.addHeapSnapshotChunk", fn)
        else:
            self.chrome.on("HeapProfiler.addHeapSnapshotChunk", fn)

    def heapStatsUpdate(self, fn, once=False) -> None:
        """
        If heap objects tracking has been started then backend may send update for one or more fragments
        """
        if once:
            self.chrome.once("HeapProfiler.heapStatsUpdate", fn)
        else:
            self.chrome.on("HeapProfiler.heapStatsUpdate", fn)

    def lastSeenObjectId(self, fn, once=False) -> None:
        """
        If heap objects tracking has been started then backend regularly sends a current value for last
        seen object id and corresponding timestamp. If the were changes in the heap since last event
        then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.
        """
        if once:
            self.chrome.once("HeapProfiler.lastSeenObjectId", fn)
        else:
            self.chrome.on("HeapProfiler.lastSeenObjectId", fn)

    def reportHeapSnapshotProgress(self, fn, once=False) -> None:
        if once:
            self.chrome.once("HeapProfiler.reportHeapSnapshotProgress", fn)
        else:
            self.chrome.on("HeapProfiler.reportHeapSnapshotProgress", fn)

    def resetProfiles(self, fn, once=False) -> None:
        if once:
            self.chrome.once("HeapProfiler.resetProfiles", fn)
        else:
            self.chrome.on("HeapProfiler.resetProfiles", fn)


