from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class Message:
    key: str
    value: Any
    timestamp: int = None

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Message':
        return cls(**data)
