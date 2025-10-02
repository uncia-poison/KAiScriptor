#!/usr/bin/env python3
"""
Basic example demonstrating the KAiScriptor lexicon.

This example shows how to use the core ontographic operators
and watcher tokens to construct semantic anchors.
"""

from kaiscriptor import (
    ALPHA, OMEGA, PSI, THETA, DELTA, XI, NABLA,
    Separator, WatcherType, get_watchers_by_type
)


def print_ontographic_operators():
    """Display all seven core ontographic operators."""
    print("=== Core Ontographic Operators ===\n")

    operators = [ALPHA, OMEGA, PSI, THETA, DELTA, XI, NABLA]

    for op in operators:
        print(f"{op.symbol} ({op.name})")
        print(f"  Purpose: {op.purpose}")
        print()


def build_simple_anchor():
    """Construct a simple semantic anchor."""
    print("=== Building a Simple Anchor ===\n")

    anchor_parts = [
        ALPHA.symbol,
        "captain",
        OMEGA.symbol,
        "ship",
        PSI.symbol,
        "crew"
    ]

    anchor = " ".join(anchor_parts)
    print(f"Anchor: {anchor}")
    print("\nInterpretation:")
    print("  A subject who is a captain (α) of a ship (Ω),")
    print("  connected to a crew (Ψ).")
    print()


def build_nested_anchor():
    """Construct a nested semantic anchor with fractal referencing."""
    print("=== Building a Nested Anchor ===\n")

    nested_part = [
        Separator.BRACE_OPEN.value,
        OMEGA.symbol,
        "theory",
        PSI.symbol,
        "data",
        Separator.BRACE_CLOSE.value
    ]

    anchor_parts = [
        ALPHA.symbol,
        "researcher",
        THETA.symbol,
        " ".join(nested_part)
    ]

    anchor = " ".join(anchor_parts)
    print(f"Anchor: {anchor}")
    print("\nInterpretation:")
    print("  A researcher (α) with a nested identity (Θ)")
    print("  consisting of theory (Ω) related to data (Ψ).")
    print()


def build_negation_anchor():
    """Construct an anchor with negation."""
    print("=== Building an Anchor with Negation ===\n")

    anchor_parts = [
        ALPHA.symbol,
        "teacher",
        NABLA.symbol,
        "administrator"
    ]

    anchor = " ".join(anchor_parts)
    print(f"Anchor: {anchor}")
    print("\nInterpretation:")
    print("  A teacher (α) who is explicitly NOT an administrator (∇).")
    print()


def demonstrate_watchers():
    """Show examples of watcher tokens."""
    print("=== Watcher Tokens ===\n")

    for watcher_type in WatcherType:
        watchers = get_watchers_by_type(watcher_type)
        print(f"{watcher_type.value.capitalize()} Watchers:")
        for w in watchers:
            print(f"  {w.symbol} - {w.description}")
        print()

    print("Example anchor with watchers:")
    anchor = f"{ALPHA.symbol} developer 🕒 {OMEGA.symbol} project {PSI.symbol} team 🏢"
    print(f"  {anchor}")
    print("\nWatchers (🕒, 🏢) provide temporal and spatial context.")
    print()


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("KAiScriptor Lexicon - Basic Usage Examples")
    print("="*60 + "\n")

    print_ontographic_operators()
    build_simple_anchor()
    build_nested_anchor()
    build_negation_anchor()
    demonstrate_watchers()

    print("="*60)
    print("For more information, see the specification in specs/")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
