from dataclasses import dataclass


@dataclass
class Message:
    timestamp: int


@dataclass
class CorrectSaveMessage(Message):
    url: str
    save_path: str


@dataclass
class IncorrectSaveMessage(Message):
    url: str
    error: BaseException
