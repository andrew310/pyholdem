from .poker import construct_deck, deal


def test_construct_deck():
    deck = construct_deck()
    assert len(deck) == 52
    assert deck[0].__class__.__name__ == 'Card'


def test_deal():
    deck, hands = deal(construct_deck())
    assert len(deck) == 48
    assert len(hands) == 2
    assert len(hands[0]) == 2
    assert hands[0].__class__.__name__ == 'Player'
    assert hands[0].__dict__.keys() == ['name', 'hand']


def test_pair_or_higher():
    pass
