from dataclasses import dataclass, field
from model import Achievement


@dataclass
class Game:
    name: str = ""
    appid: str = ""
    achievements: dict[str, Achievement] = field(default_factory=dict)
    has_protected: bool = False
    protected_count: int = 0
    achievement_count: int = 0
