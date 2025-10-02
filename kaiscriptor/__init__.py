"""
KAiScriptor: Semantic Role Framing Toolkit for LLMs

A semantic compression system for encoding identity, roles, and relationships
in transformer-based Large Language Models using a lexicon of 150+ symbols.
"""

__version__ = "0.1.0"

from .ontography import (
    ALPHA,
    OMEGA,
    PSI,
    THETA,
    DELTA,
    XI,
    NABLA,
    OntographicOperator,
)

from .lexicon import (
    Separator,
    Watcher,
    WatcherType,
    get_watchers_by_type,
)

__all__ = [
    "ALPHA",
    "OMEGA",
    "PSI",
    "THETA",
    "DELTA",
    "XI",
    "NABLA",
    "OntographicOperator",
    "Separator",
    "Watcher",
    "WatcherType",
    "get_watchers_by_type",
]
