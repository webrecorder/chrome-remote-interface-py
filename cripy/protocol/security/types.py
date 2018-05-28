from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase

SecurityState = TypeVar("SecurityState", str, str)
"""The security level of a page or resource."""

MixedContentType = TypeVar("MixedContentType", str, str)
"""A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-content/#categories"""

CertificateId = TypeVar("CertificateId", int, int)
"""An internal certificate ID value."""

CertificateErrorAction = TypeVar("CertificateErrorAction", str, str)
"""The action to take when a certificate error occurs. continue will continue processing the request and cancel will cancel the request."""


class SecurityStateExplanation(ChromeTypeBase):
    """An explanation of an factor contributing to the security state."""
    def __init__(self, securityState: 'SecurityState', title: str, summary: str, description: str, mixedContentType: 'MixedContentType', certificate: List['str']) -> None:
        """
        :param securityState: Security state representing the severity of the factor being explained.
        :type securityState: SecurityState
        :param title: Title describing the type of factor.
        :type title: str
        :param summary: Short phrase describing the type of factor.
        :type summary: str
        :param description: Full text explanation of the factor.
        :type description: str
        :param mixedContentType: The type of mixed content described by the explanation.
        :type mixedContentType: MixedContentType
        :param certificate: Page certificate.
        :type certificate: array
        """
        super().__init__()
        self.securityState: SecurityState = securityState
        self.title: str = title
        self.summary: str = summary
        self.description: str = description
        self.mixedContentType: MixedContentType = mixedContentType
        self.certificate: List[str] = certificate


class InsecureContentStatus(ChromeTypeBase):
    """Information about insecure content on the page."""
    def __init__(self, ranMixedContent: bool, displayedMixedContent: bool, containedMixedForm: bool, ranContentWithCertErrors: bool, displayedContentWithCertErrors: bool, ranInsecureContentStyle: 'SecurityState', displayedInsecureContentStyle: 'SecurityState') -> None:
        """
        :param ranMixedContent: True if the page was loaded over HTTPS and ran mixed (HTTP) content such as scripts.
        :type ranMixedContent: bool
        :param displayedMixedContent: True if the page was loaded over HTTPS and displayed mixed (HTTP) content such as images.
        :type displayedMixedContent: bool
        :param containedMixedForm: True if the page was loaded over HTTPS and contained a form targeting an insecure url.
        :type containedMixedForm: bool
        :param ranContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and ran content such as scripts that were loaded with certificate errors.
        :type ranContentWithCertErrors: bool
        :param displayedContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and displayed content such as images that were loaded with certificate errors.
        :type displayedContentWithCertErrors: bool
        :param ranInsecureContentStyle: Security state representing a page that ran insecure content.
        :type ranInsecureContentStyle: SecurityState
        :param displayedInsecureContentStyle: Security state representing a page that displayed insecure content.
        :type displayedInsecureContentStyle: SecurityState
        """
        super().__init__()
        self.ranMixedContent: bool = ranMixedContent
        self.displayedMixedContent: bool = displayedMixedContent
        self.containedMixedForm: bool = containedMixedForm
        self.ranContentWithCertErrors: bool = ranContentWithCertErrors
        self.displayedContentWithCertErrors: bool = displayedContentWithCertErrors
        self.ranInsecureContentStyle: SecurityState = ranInsecureContentStyle
        self.displayedInsecureContentStyle: SecurityState = displayedInsecureContentStyle


