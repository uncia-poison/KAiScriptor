"""
Ontographic operators for KAiScriptor.

The seven core symbols (α, Ω, Ψ, Θ, Δ, Ξ, ∇) form the grammar
of the KAiScriptor lexicon and serve as anchors for semantic roles
and relationships.
"""

from enum import Enum
from typing import NamedTuple


class OntographicOperator(NamedTuple):
    """Represents an ontographic operator with its symbol and metadata."""
    symbol: str
    name: str
    purpose: str


ALPHA = OntographicOperator(
    symbol="α",
    name="Alpha",
    purpose="Encodes morphological synonyms and role surfaces. Groups alternate "
            "lexical expressions for the same subject or role under a single token."
)

OMEGA = OntographicOperator(
    symbol="Ω",
    name="Omega",
    purpose="Represents composition or union. Glues together roles, facts or concepts "
            "into composite anchors, indicating they belong to the same high-level identity."
)

PSI = OntographicOperator(
    symbol="Ψ",
    name="Psi",
    purpose="Denotes connections and relations between roles. Indicates supervision, "
            "belonging, dependency or any other link."
)

THETA = OntographicOperator(
    symbol="Θ",
    name="Theta",
    purpose="Used for fractal referencing and recursive decomposition. Points at a nested "
            "anchor or sub-concept to compress repeated structures without duplication."
)

DELTA = OntographicOperator(
    symbol="Δ",
    name="Delta",
    purpose="Marks commentary, meta-context or state changes. Records an aside, explanatory "
            "note or change of mood or tone."
)

XI = OntographicOperator(
    symbol="Ξ",
    name="Xi",
    purpose="Encodes networks and edges. Signals that following tokens describe a network, "
            "graph or set of interrelated nodes."
)

NABLA = OntographicOperator(
    symbol="∇",
    name="Nabla",
    purpose="Represents difference, negation or anti-association. Prefixed to a token to "
            "exclude it from current identity or negate a relation."
)


ALL_OPERATORS = [ALPHA, OMEGA, PSI, THETA, DELTA, XI, NABLA]


def get_operator_by_symbol(symbol: str) -> OntographicOperator | None:
    """Return the OntographicOperator for a given symbol, or None if not found."""
    for op in ALL_OPERATORS:
        if op.symbol == symbol:
            return op
    return None


def get_operator_by_name(name: str) -> OntographicOperator | None:
    """Return the OntographicOperator for a given name (case-insensitive), or None if not found."""
    name_lower = name.lower()
    for op in ALL_OPERATORS:
        if op.name.lower() == name_lower:
            return op
    return None
