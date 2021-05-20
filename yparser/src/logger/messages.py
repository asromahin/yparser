from dataclasses import dataclass
import numpy as np
from PIL import Image


@dataclass
class Message:
    url: str
    timestamp: int
    len_queue: int
    id: str


@dataclass
class DownloadsMessage(Message):
    ''


@dataclass
class ParseMessage(Message):
    ''


@dataclass
class CorrectSaveMessage(DownloadsMessage):
    save_path: str


@dataclass
class IncorrectSaveMessage(DownloadsMessage):
    error: BaseException


@dataclass
class CorrectParseMessage(ParseMessage):
    parsed: list


@dataclass
class IncorrectParseMessage(ParseMessage):
    error: BaseException


@dataclass
class CurrentStateScreenshotMessage(ParseMessage):
    screenshot: Image
