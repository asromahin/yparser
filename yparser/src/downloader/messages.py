from dataclasses import dataclass
import time


class Message:
    def __init__(self):
        self.timestamp = int(time.time())


@dataclass
class CorrectSaveMessage(Message):
    url: str
    save_path: str


@dataclass
class IncorrectSaveMessage(Message):
    url: str
    error: BaseException
