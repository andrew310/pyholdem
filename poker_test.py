import pytest
from holdem import construct_deck, deal, is_pair_or_higher, is_three_of_a_kind


def test_construct_deck():
    deck = construct_deck()
    assert len(deck) == 52
    assert deck[0].__class__.__name__ == 'Card'
    for i in range(0, 4):
        assert deck[i].rank == 2
        assert deck[i].rankname == '2'

    for i in range(48, 52):
        assert deck[i].rank == 14
        assert deck[i].rankname == 'A'


def test_deal():
    deck, hands = deal(construct_deck())
    assert len(deck) == 48
    assert len(hands) == 2
    assert len(hands[0]) == 2
    assert hands[0].__class__.__name__ == 'Player'
    assert hands[0].__dict__.keys() == ['name', 'hand']


def test_pair_or_higher():
    deck = construct_deck()
    assert is_pair_or_higher([deck[0], deck[1]]) == [(2, 2)]
    assert is_pair_or_higher([deck[0], deck[3]]) == [(2, 2)]
    assert is_pair_or_higher([deck[0], deck[1]],
                             [deck[2], deck[11], deck[20]]) == [(2, 3)]
    assert is_pair_or_higher([deck[0], deck[1]],
                             [deck[2], deck[3], deck[4]]) == [(2, 4)]

    # Wrong Card Amounts

    with pytest.raises(NameError):
        # Too many pocket cards.
        assert is_pair_or_higher([deck[0], deck[1], deck[2]])

    with pytest.raises(NameError):
        # Only one card in pocket.
        assert is_pair_or_higher([deck[0]])

    with pytest.raises(NameError):
        # Too few community cards.
        assert is_pair_or_higher([deck[0], deck[0]],
                                 [deck[0]])

    with pytest.raises(NameError):
        # Too many community cards.
        assert is_pair_or_higher([deck[0], deck[0]],
                                 [deck[0], deck[0], deck[0], deck[0], deck[0],
                                  deck[0]])


def test_is_three_of_a_kind():
    deck = construct_deck()
    # Three of a kind with 2s.
    assert is_three_of_a_kind([deck[0], deck[1]],
                              [deck[2], deck[4], deck[5]]) == 2

    assert is_three_of_a_kind([deck[0], deck[1]],
                              [deck[4], deck[7], deck[10]]) == False

    # 2 possible sets, 2s and 3s
    assert is_three_of_a_kind([deck[0], deck[1]],
                              [deck[2], deck[4], deck[5], deck[6]]) == 3
