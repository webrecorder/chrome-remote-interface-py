from cripy.gevent.protocol.input import types as Types

__all__ = ["Input"]


class Input(object):
    def __init__(self, chrome):
        """
        Construct a new Input object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def dispatchKeyEvent(self, type, modifiers=None, timestamp=None, text=None, unmodifiedText=None, keyIdentifier=None, code=None, key=None, windowsVirtualKeyCode=None, nativeVirtualKeyCode=None, autoRepeat=None, isKeypad=None, isSystemKey=None, location=None):
        """
        Dispatches a key event to the page.

        :param type: Type of the key event.
        :type type: str
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: Optional[int]
        :param timestamp: Time at which the event occurred.
        :type timestamp: Optional[float]
        :param text: Text as generated by processing a virtual key code with a keyboard layout. Not needed for for `keyUp` and `rawKeyDown` events (default: "")
        :type text: Optional[str]
        :param unmodifiedText: Text that would have been generated by the keyboard if no modifiers were pressed (except for shift). Useful for shortcut (accelerator) key handling (default: "").
        :type unmodifiedText: Optional[str]
        :param keyIdentifier: Unique key identifier (e.g., 'U+0041') (default: "").
        :type keyIdentifier: Optional[str]
        :param code: Unique DOM defined string value for each physical key (e.g., 'KeyA') (default: "").
        :type code: Optional[str]
        :param key: Unique DOM defined string value describing the meaning of the key in the context of active modifiers, keyboard layout, etc (e.g., 'AltGr') (default: "").
        :type key: Optional[str]
        :param windowsVirtualKeyCode: Windows virtual key code (default: 0).
        :type windowsVirtualKeyCode: Optional[int]
        :param nativeVirtualKeyCode: Native virtual key code (default: 0).
        :type nativeVirtualKeyCode: Optional[int]
        :param autoRepeat: Whether the event was generated from auto repeat (default: false).
        :type autoRepeat: Optional[bool]
        :param isKeypad: Whether the event was generated from the keypad (default: false).
        :type isKeypad: Optional[bool]
        :param isSystemKey: Whether the event was a system key event (default: false).
        :type isSystemKey: Optional[bool]
        :param location: Whether the event was from the left or right side of the keyboard. 1=Left, 2=Right (default: 0).
        :type location: Optional[int]
        """
        msg_dict = dict()
        if type is not None:
            msg_dict['type'] = type
        if modifiers is not None:
            msg_dict['modifiers'] = modifiers
        if timestamp is not None:
            msg_dict['timestamp'] = timestamp
        if text is not None:
            msg_dict['text'] = text
        if unmodifiedText is not None:
            msg_dict['unmodifiedText'] = unmodifiedText
        if keyIdentifier is not None:
            msg_dict['keyIdentifier'] = keyIdentifier
        if code is not None:
            msg_dict['code'] = code
        if key is not None:
            msg_dict['key'] = key
        if windowsVirtualKeyCode is not None:
            msg_dict['windowsVirtualKeyCode'] = windowsVirtualKeyCode
        if nativeVirtualKeyCode is not None:
            msg_dict['nativeVirtualKeyCode'] = nativeVirtualKeyCode
        if autoRepeat is not None:
            msg_dict['autoRepeat'] = autoRepeat
        if isKeypad is not None:
            msg_dict['isKeypad'] = isKeypad
        if isSystemKey is not None:
            msg_dict['isSystemKey'] = isSystemKey
        if location is not None:
            msg_dict['location'] = location
        wres = self.chrome.send('Input.dispatchKeyEvent', msg_dict)
        return wres.get()

    def dispatchMouseEvent(self, type, x, y, modifiers=None, timestamp=None, button=None, clickCount=None, deltaX=None, deltaY=None):
        """
        Dispatches a mouse event to the page.

        :param type: Type of the mouse event.
        :type type: str
        :param x: X coordinate of the event relative to the main frame's viewport in CSS pixels.
        :type x: float
        :param y: Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
        :type y: float
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: Optional[int]
        :param timestamp: Time at which the event occurred.
        :type timestamp: Optional[float]
        :param button: Mouse button (default: "none").
        :type button: Optional[str]
        :param clickCount: Number of times the mouse button was clicked (default: 0).
        :type clickCount: Optional[int]
        :param deltaX: X delta in CSS pixels for mouse wheel event (default: 0).
        :type deltaX: Optional[float]
        :param deltaY: Y delta in CSS pixels for mouse wheel event (default: 0).
        :type deltaY: Optional[float]
        """
        msg_dict = dict()
        if type is not None:
            msg_dict['type'] = type
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if modifiers is not None:
            msg_dict['modifiers'] = modifiers
        if timestamp is not None:
            msg_dict['timestamp'] = timestamp
        if button is not None:
            msg_dict['button'] = button
        if clickCount is not None:
            msg_dict['clickCount'] = clickCount
        if deltaX is not None:
            msg_dict['deltaX'] = deltaX
        if deltaY is not None:
            msg_dict['deltaY'] = deltaY
        wres = self.chrome.send('Input.dispatchMouseEvent', msg_dict)
        return wres.get()

    def dispatchTouchEvent(self, type, touchPoints, modifiers=None, timestamp=None):
        """
        Dispatches a touch event to the page.

        :param type: Type of the touch event. TouchEnd and TouchCancel must not contain any touch points, while TouchStart and TouchMove must contains at least one.
        :type type: str
        :param touchPoints: Active touch points on the touch device. One event per any changed point (compared to previous touch event in a sequence) is generated, emulating pressing/moving/releasing points one by one.
        :type touchPoints: List[dict]
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: Optional[int]
        :param timestamp: Time at which the event occurred.
        :type timestamp: Optional[float]
        """
        msg_dict = dict()
        if type is not None:
            msg_dict['type'] = type
        if touchPoints is not None:
            msg_dict['touchPoints'] = touchPoints
        if modifiers is not None:
            msg_dict['modifiers'] = modifiers
        if timestamp is not None:
            msg_dict['timestamp'] = timestamp
        wres = self.chrome.send('Input.dispatchTouchEvent', msg_dict)
        return wres.get()

    def emulateTouchFromMouseEvent(self, type, x, y, button, timestamp=None, deltaX=None, deltaY=None, modifiers=None, clickCount=None):
        """
        Emulates touch event from the mouse event parameters.

        :param type: Type of the mouse event.
        :type type: str
        :param x: X coordinate of the mouse pointer in DIP.
        :type x: int
        :param y: Y coordinate of the mouse pointer in DIP.
        :type y: int
        :param button: Mouse button.
        :type button: str
        :param timestamp: Time at which the event occurred (default: current time).
        :type timestamp: Optional[float]
        :param deltaX: X delta in DIP for mouse wheel event (default: 0).
        :type deltaX: Optional[float]
        :param deltaY: Y delta in DIP for mouse wheel event (default: 0).
        :type deltaY: Optional[float]
        :param modifiers: Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
        :type modifiers: Optional[int]
        :param clickCount: Number of times the mouse button was clicked (default: 0).
        :type clickCount: Optional[int]
        """
        msg_dict = dict()
        if type is not None:
            msg_dict['type'] = type
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if button is not None:
            msg_dict['button'] = button
        if timestamp is not None:
            msg_dict['timestamp'] = timestamp
        if deltaX is not None:
            msg_dict['deltaX'] = deltaX
        if deltaY is not None:
            msg_dict['deltaY'] = deltaY
        if modifiers is not None:
            msg_dict['modifiers'] = modifiers
        if clickCount is not None:
            msg_dict['clickCount'] = clickCount
        wres = self.chrome.send('Input.emulateTouchFromMouseEvent', msg_dict)
        return wres.get()

    def setIgnoreInputEvents(self, ignore):
        """
        Ignores input events (useful while auditing page).

        :param ignore: Ignores input events processing when set to true.
        :type ignore: bool
        """
        msg_dict = dict()
        if ignore is not None:
            msg_dict['ignore'] = ignore
        wres = self.chrome.send('Input.setIgnoreInputEvents', msg_dict)
        return wres.get()

    def synthesizePinchGesture(self, x, y, scaleFactor, relativeSpeed=None, gestureSourceType=None):
        """
        Synthesizes a pinch gesture over a time period by issuing appropriate touch events.

        :param x: X coordinate of the start of the gesture in CSS pixels.
        :type x: float
        :param y: Y coordinate of the start of the gesture in CSS pixels.
        :type y: float
        :param scaleFactor: Relative scale factor after zooming (>1.0 zooms in, <1.0 zooms out).
        :type scaleFactor: float
        :param relativeSpeed: Relative pointer speed in pixels per second (default: 800).
        :type relativeSpeed: Optional[int]
        :param gestureSourceType: Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
        :type gestureSourceType: Optional[str]
        """
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if scaleFactor is not None:
            msg_dict['scaleFactor'] = scaleFactor
        if relativeSpeed is not None:
            msg_dict['relativeSpeed'] = relativeSpeed
        if gestureSourceType is not None:
            msg_dict['gestureSourceType'] = gestureSourceType
        wres = self.chrome.send('Input.synthesizePinchGesture', msg_dict)
        return wres.get()

    def synthesizeScrollGesture(self, x, y, xDistance=None, yDistance=None, xOverscroll=None, yOverscroll=None, preventFling=None, speed=None, gestureSourceType=None, repeatCount=None, repeatDelayMs=None, interactionMarkerName=None):
        """
        Synthesizes a scroll gesture over a time period by issuing appropriate touch events.

        :param x: X coordinate of the start of the gesture in CSS pixels.
        :type x: float
        :param y: Y coordinate of the start of the gesture in CSS pixels.
        :type y: float
        :param xDistance: The distance to scroll along the X axis (positive to scroll left).
        :type xDistance: Optional[float]
        :param yDistance: The distance to scroll along the Y axis (positive to scroll up).
        :type yDistance: Optional[float]
        :param xOverscroll: The number of additional pixels to scroll back along the X axis, in addition to the given distance.
        :type xOverscroll: Optional[float]
        :param yOverscroll: The number of additional pixels to scroll back along the Y axis, in addition to the given distance.
        :type yOverscroll: Optional[float]
        :param preventFling: Prevent fling (default: true).
        :type preventFling: Optional[bool]
        :param speed: Swipe speed in pixels per second (default: 800).
        :type speed: Optional[int]
        :param gestureSourceType: Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
        :type gestureSourceType: Optional[str]
        :param repeatCount: The number of times to repeat the gesture (default: 0).
        :type repeatCount: Optional[int]
        :param repeatDelayMs: The number of milliseconds delay between each repeat. (default: 250).
        :type repeatDelayMs: Optional[int]
        :param interactionMarkerName: The name of the interaction markers to generate, if not empty (default: "").
        :type interactionMarkerName: Optional[str]
        """
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if xDistance is not None:
            msg_dict['xDistance'] = xDistance
        if yDistance is not None:
            msg_dict['yDistance'] = yDistance
        if xOverscroll is not None:
            msg_dict['xOverscroll'] = xOverscroll
        if yOverscroll is not None:
            msg_dict['yOverscroll'] = yOverscroll
        if preventFling is not None:
            msg_dict['preventFling'] = preventFling
        if speed is not None:
            msg_dict['speed'] = speed
        if gestureSourceType is not None:
            msg_dict['gestureSourceType'] = gestureSourceType
        if repeatCount is not None:
            msg_dict['repeatCount'] = repeatCount
        if repeatDelayMs is not None:
            msg_dict['repeatDelayMs'] = repeatDelayMs
        if interactionMarkerName is not None:
            msg_dict['interactionMarkerName'] = interactionMarkerName
        wres = self.chrome.send('Input.synthesizeScrollGesture', msg_dict)
        return wres.get()

    def synthesizeTapGesture(self, x, y, duration=None, tapCount=None, gestureSourceType=None):
        """
        Synthesizes a tap gesture over a time period by issuing appropriate touch events.

        :param x: X coordinate of the start of the gesture in CSS pixels.
        :type x: float
        :param y: Y coordinate of the start of the gesture in CSS pixels.
        :type y: float
        :param duration: Duration between touchdown and touchup events in ms (default: 50).
        :type duration: Optional[int]
        :param tapCount: Number of times to perform the tap (e.g. 2 for double tap, default: 1).
        :type tapCount: Optional[int]
        :param gestureSourceType: Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
        :type gestureSourceType: Optional[str]
        """
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if duration is not None:
            msg_dict['duration'] = duration
        if tapCount is not None:
            msg_dict['tapCount'] = tapCount
        if gestureSourceType is not None:
            msg_dict['gestureSourceType'] = gestureSourceType
        wres = self.chrome.send('Input.synthesizeTapGesture', msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None
