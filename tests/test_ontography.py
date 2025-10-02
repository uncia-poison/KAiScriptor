"""Tests for ontographic operators."""

import pytest
from kaiscriptor.ontography import (
    ALPHA, OMEGA, PSI, THETA, DELTA, XI, NABLA,
    ALL_OPERATORS,
    get_operator_by_symbol,
    get_operator_by_name,
    OntographicOperator
)


class TestOntographicOperators:
    """Test the ontographic operator constants."""

    def test_alpha_operator(self):
        """Test the ALPHA operator properties."""
        assert ALPHA.symbol == "α"
        assert ALPHA.name == "Alpha"
        assert "morphological" in ALPHA.purpose.lower()

    def test_omega_operator(self):
        """Test the OMEGA operator properties."""
        assert OMEGA.symbol == "Ω"
        assert OMEGA.name == "Omega"
        assert "composition" in OMEGA.purpose.lower() or "union" in OMEGA.purpose.lower()

    def test_psi_operator(self):
        """Test the PSI operator properties."""
        assert PSI.symbol == "Ψ"
        assert PSI.name == "Psi"
        assert "connection" in PSI.purpose.lower() or "relation" in PSI.purpose.lower()

    def test_theta_operator(self):
        """Test the THETA operator properties."""
        assert THETA.symbol == "Θ"
        assert THETA.name == "Theta"
        assert "fractal" in THETA.purpose.lower() or "nested" in THETA.purpose.lower()

    def test_delta_operator(self):
        """Test the DELTA operator properties."""
        assert DELTA.symbol == "Δ"
        assert DELTA.name == "Delta"
        assert "commentary" in DELTA.purpose.lower() or "meta" in DELTA.purpose.lower()

    def test_xi_operator(self):
        """Test the XI operator properties."""
        assert XI.symbol == "Ξ"
        assert XI.name == "Xi"
        assert "network" in XI.purpose.lower()

    def test_nabla_operator(self):
        """Test the NABLA operator properties."""
        assert NABLA.symbol == "∇"
        assert NABLA.name == "Nabla"
        assert "negation" in NABLA.purpose.lower() or "difference" in NABLA.purpose.lower()

    def test_all_operators_count(self):
        """Test that ALL_OPERATORS contains exactly 7 operators."""
        assert len(ALL_OPERATORS) == 7

    def test_all_operators_unique_symbols(self):
        """Test that all operators have unique symbols."""
        symbols = [op.symbol for op in ALL_OPERATORS]
        assert len(symbols) == len(set(symbols))

    def test_all_operators_unique_names(self):
        """Test that all operators have unique names."""
        names = [op.name for op in ALL_OPERATORS]
        assert len(names) == len(set(names))


class TestOperatorLookup:
    """Test the operator lookup functions."""

    def test_get_operator_by_symbol_valid(self):
        """Test lookup by valid symbol."""
        result = get_operator_by_symbol("α")
        assert result is not None
        assert result.name == "Alpha"

    def test_get_operator_by_symbol_all(self):
        """Test that all operators can be found by their symbols."""
        for op in ALL_OPERATORS:
            result = get_operator_by_symbol(op.symbol)
            assert result is not None
            assert result.name == op.name

    def test_get_operator_by_symbol_invalid(self):
        """Test lookup by invalid symbol returns None."""
        result = get_operator_by_symbol("X")
        assert result is None

    def test_get_operator_by_name_valid(self):
        """Test lookup by valid name."""
        result = get_operator_by_name("Alpha")
        assert result is not None
        assert result.symbol == "α"

    def test_get_operator_by_name_case_insensitive(self):
        """Test that name lookup is case-insensitive."""
        result1 = get_operator_by_name("alpha")
        result2 = get_operator_by_name("ALPHA")
        result3 = get_operator_by_name("Alpha")

        assert result1 is not None
        assert result1 == result2 == result3

    def test_get_operator_by_name_all(self):
        """Test that all operators can be found by their names."""
        for op in ALL_OPERATORS:
            result = get_operator_by_name(op.name)
            assert result is not None
            assert result.symbol == op.symbol

    def test_get_operator_by_name_invalid(self):
        """Test lookup by invalid name returns None."""
        result = get_operator_by_name("InvalidOperator")
        assert result is None


class TestOntographicOperatorType:
    """Test the OntographicOperator type."""

    def test_operator_is_namedtuple(self):
        """Test that OntographicOperator is a NamedTuple."""
        assert hasattr(ALPHA, '_fields')
        assert ALPHA._fields == ('symbol', 'name', 'purpose')

    def test_operator_immutable(self):
        """Test that operators are immutable."""
        with pytest.raises(AttributeError):
            ALPHA.symbol = "β"
