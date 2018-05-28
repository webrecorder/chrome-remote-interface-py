from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase


class Domain(ChromeTypeBase):
    """Description of the protocol domain."""
    def __init__(self, name: str, version: str) -> None:
        """
        :param name: Domain name.
        :type name: str
        :param version: Domain version.
        :type version: str
        """
        super().__init__()
        self.name: str = name
        self.version: str = version


