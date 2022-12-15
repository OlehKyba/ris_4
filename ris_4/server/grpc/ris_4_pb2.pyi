from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DecreaseByOneLetterRequest(_message.Message):
    __slots__ = ["word"]
    WORD_FIELD_NUMBER: _ClassVar[int]
    word: str
    def __init__(self, word: _Optional[str] = ...) -> None: ...

class DecreaseByOneLetterResponse(_message.Message):
    __slots__ = ["is_decreased"]
    IS_DECREASED_FIELD_NUMBER: _ClassVar[int]
    is_decreased: bool
    def __init__(self, is_decreased: bool = ...) -> None: ...
