from dataclasses import dataclass


@dataclass
class Achievement:
    name: str = ""
    protected: bool = False
