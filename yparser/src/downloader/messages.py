from dataclasses import dataclass


@dataclass
class Message:
    url: str
    timestamp: int
    len_queue: int


@dataclass
class CorrectSaveMessage(Message):
    save_path: str


@dataclass
class IncorrectSaveMessage(Message):
    error: BaseException
