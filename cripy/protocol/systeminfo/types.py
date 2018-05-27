from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class GPUDevice(ChromeTypeBase):
    """Describes a single graphics processor (GPU)."""

    def __init__(
        self, vendorId: float, deviceId: float, vendorString: str, deviceString: str
    ) -> None:
        """
        :param vendorId: PCI ID of the GPU vendor, if available; 0 otherwise.
        :param deviceId: PCI ID of the GPU device, if available; 0 otherwise.
        :param vendorString: String description of the GPU vendor, if the PCI ID is not available.
        :param deviceString: String description of the GPU device, if the PCI ID is not available.
        """
        super().__init__()
        self.vendorId: float = vendorId
        self.deviceId: float = deviceId
        self.vendorString: str = vendorString
        self.deviceString: str = deviceString


class GPUInfo(ChromeTypeBase):
    """Provides information about the GPU(s) on the system."""

    def __init__(
        self,
        devices: List["GPUDevice"],
        driverBugWorkarounds: List["str"],
        auxAttributes: Optional[dict] = None,
        featureStatus: Optional[dict] = None,
    ) -> None:
        """
        :param devices: The graphics devices on the system. Element 0 is the primary GPU.
        :param auxAttributes: An optional dictionary of additional GPU related attributes.
        :param featureStatus: An optional dictionary of graphics features and their status.
        :param driverBugWorkarounds: An optional array of GPU driver bug workarounds.
        """
        super().__init__()
        self.devices: List[GPUDevice] = devices
        self.auxAttributes: Optional[dict] = auxAttributes
        self.featureStatus: Optional[dict] = featureStatus
        self.driverBugWorkarounds: List[str] = driverBugWorkarounds