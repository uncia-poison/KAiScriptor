"""Tests for lexicon components."""

import pytest
from kaiscriptor.lexicon import (
    Separator,
    WatcherType,
    Watcher,
    TEMPORAL_WATCHERS,
    EMOTIONAL_WATCHERS,
    SPATIAL_WATCHERS,
    ALL_WATCHERS,
    get_watchers_by_type
)


class TestSeparator:
    """Test the Separator enum."""

    def test_separator_values(self):
        """Test that separator enum has expected values."""
        assert Separator.SLASH == "/"
        assert Separator.PIPE == "|"
        assert Separator.SEMICOLON == ";"
        assert Separator.BRACE_OPEN == "{"
        assert Separator.BRACE_CLOSE == "}"
        assert Separator.PAREN_OPEN == "("
        assert Separator.PAREN_CLOSE == ")"

    def test_separator_is_string(self):
        """Test that separators can be used as strings."""
        sep = Separator.SLASH
        assert isinstance(sep.value, str)
        assert sep.value in "test/path"


class TestWatcherType:
    """Test the WatcherType enum."""

    def test_watcher_type_values(self):
        """Test that watcher types have expected values."""
        assert WatcherType.TEMPORAL == "temporal"
        assert WatcherType.EMOTIONAL == "emotional"
        assert WatcherType.SPATIAL == "spatial"

    def test_watcher_type_count(self):
        """Test that there are exactly 3 watcher types."""
        assert len(list(WatcherType)) == 3


class TestWatchers:
    """Test watcher tokens."""

    def test_temporal_watchers_exist(self):
        """Test that temporal watchers are defined."""
        assert len(TEMPORAL_WATCHERS) > 0
        for w in TEMPORAL_WATCHERS:
            assert w.watcher_type == WatcherType.TEMPORAL

    def test_emotional_watchers_exist(self):
        """Test that emotional watchers are defined."""
        assert len(EMOTIONAL_WATCHERS) > 0
        for w in EMOTIONAL_WATCHERS:
            assert w.watcher_type == WatcherType.EMOTIONAL

    def test_spatial_watchers_exist(self):
        """Test that spatial watchers are defined."""
        assert len(SPATIAL_WATCHERS) > 0
        for w in SPATIAL_WATCHERS:
            assert w.watcher_type == WatcherType.SPATIAL

    def test_all_watchers_comprehensive(self):
        """Test that ALL_WATCHERS contains all watcher categories."""
        expected_count = (
            len(TEMPORAL_WATCHERS) +
            len(EMOTIONAL_WATCHERS) +
            len(SPATIAL_WATCHERS)
        )
        assert len(ALL_WATCHERS) == expected_count

    def test_watcher_structure(self):
        """Test that watchers have the expected structure."""
        for w in ALL_WATCHERS:
            assert isinstance(w, Watcher)
            assert isinstance(w.symbol, str)
            assert len(w.symbol) > 0
            assert isinstance(w.watcher_type, WatcherType)
            assert isinstance(w.description, str)
            assert len(w.description) > 0

    def test_watcher_symbols_unique(self):
        """Test that all watcher symbols are unique."""
        symbols = [w.symbol for w in ALL_WATCHERS]
        assert len(symbols) == len(set(symbols))


class TestWatcherLookup:
    """Test watcher lookup functions."""

    def test_get_watchers_by_type_temporal(self):
        """Test getting temporal watchers."""
        result = get_watchers_by_type(WatcherType.TEMPORAL)
        assert len(result) == len(TEMPORAL_WATCHERS)
        assert all(w.watcher_type == WatcherType.TEMPORAL for w in result)

    def test_get_watchers_by_type_emotional(self):
        """Test getting emotional watchers."""
        result = get_watchers_by_type(WatcherType.EMOTIONAL)
        assert len(result) == len(EMOTIONAL_WATCHERS)
        assert all(w.watcher_type == WatcherType.EMOTIONAL for w in result)

    def test_get_watchers_by_type_spatial(self):
        """Test getting spatial watchers."""
        result = get_watchers_by_type(WatcherType.SPATIAL)
        assert len(result) == len(SPATIAL_WATCHERS)
        assert all(w.watcher_type == WatcherType.SPATIAL for w in result)

    def test_get_watchers_by_type_all_categories(self):
        """Test that each watcher type returns the correct watchers."""
        for watcher_type in WatcherType:
            result = get_watchers_by_type(watcher_type)
            assert len(result) > 0
            assert all(w.watcher_type == watcher_type for w in result)


class TestWatcherType:
    """Test the Watcher NamedTuple type."""

    def test_watcher_is_namedtuple(self):
        """Test that Watcher is a NamedTuple."""
        w = TEMPORAL_WATCHERS[0]
        assert hasattr(w, '_fields')
        assert w._fields == ('symbol', 'watcher_type', 'description')

    def test_watcher_immutable(self):
        """Test that watchers are immutable."""
        w = TEMPORAL_WATCHERS[0]
        with pytest.raises(AttributeError):
            w.symbol = "X"
