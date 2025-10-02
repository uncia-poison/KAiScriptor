"""
Extended lexicon components for KAiScriptor.

Defines separators, watchers, and other token classes used in
semantic anchor assembly.
"""

from enum import Enum
from typing import NamedTuple


class Separator(str, Enum):
    """Separators and punctuation used in KAiScriptor anchors."""
    SLASH = "/"
    PIPE = "|"
    SEMICOLON = ";"
    BRACE_OPEN = "{"
    BRACE_CLOSE = "}"
    PAREN_OPEN = "("
    PAREN_CLOSE = ")"


class WatcherType(str, Enum):
    """Categories of watcher tokens that aid memory and retrieval."""
    TEMPORAL = "temporal"
    EMOTIONAL = "emotional"
    SPATIAL = "spatial"


class Watcher(NamedTuple):
    """Represents a watcher token with its type and symbol."""
    symbol: str
    watcher_type: WatcherType
    description: str


TEMPORAL_WATCHERS = [
    Watcher("🕒", WatcherType.TEMPORAL, "Generic time marker"),
    Watcher("⏰", WatcherType.TEMPORAL, "Alarm/deadline"),
    Watcher("📅", WatcherType.TEMPORAL, "Calendar/date"),
    Watcher("⌛", WatcherType.TEMPORAL, "Time passing"),
]

EMOTIONAL_WATCHERS = [
    Watcher("❤️", WatcherType.EMOTIONAL, "Love/affection"),
    Watcher("🔥", WatcherType.EMOTIONAL, "Passion/intensity"),
    Watcher("😊", WatcherType.EMOTIONAL, "Joy/happiness"),
    Watcher("😢", WatcherType.EMOTIONAL, "Sadness"),
    Watcher("😠", WatcherType.EMOTIONAL, "Anger"),
    Watcher("💡", WatcherType.EMOTIONAL, "Insight/realization"),
]

SPATIAL_WATCHERS = [
    Watcher("🌍", WatcherType.SPATIAL, "Earth/global"),
    Watcher("🏡", WatcherType.SPATIAL, "Home"),
    Watcher("🏢", WatcherType.SPATIAL, "Office/workplace"),
    Watcher("✈️", WatcherType.SPATIAL, "Travel"),
    Watcher("🌊", WatcherType.SPATIAL, "Ocean/water"),
    Watcher("🏔️", WatcherType.SPATIAL, "Mountains"),
]

ALL_WATCHERS = TEMPORAL_WATCHERS + EMOTIONAL_WATCHERS + SPATIAL_WATCHERS


def get_watchers_by_type(watcher_type: WatcherType) -> list[Watcher]:
    """Return all watchers of a specific type."""
    return [w for w in ALL_WATCHERS if w.watcher_type == watcher_type]
