from collections import namedtuple, Counter
from functools import wraps
import random


def construct_deck():
    card = namedtuple("Card", 'rank rankname suit')
    ranks = [x for x in range(2, 15)]
    rank_names = list(map(str, ranks[:-4])) + ['J', 'Q', 'K', 'A']
    suits = ['hearts', 'spades', 'clubs', 'diamonds']

    return [card(x[0], x[1], y)
            for x in zip(ranks, rank_names) for y in suits]


def shuffle(deck):
    temp = deck[:]
    random.shuffle(temp)
    return temp


def validate_cards(f):
    """Simply ensure no incorrect card amounts.
    """
    def wrapper(*args, **kwargs):
        if len(args[0]) != 2:
            raise NameError('WrongPlayerCardAmount')

        if len(args) > 1:
            if len(args[1]) < 3 or len(args[1]) > 5:
                raise NameError('WrongCommunityCardAmount')

        return f(*args, **kwargs)
    return wrapper


def deal(deck, player_count=2):
    """Returns named tuple of players hands
       and deck with remaining cards.
       Should only be called once at beginning of game.
    """
    player = namedtuple("Player", 'name hand')
    hands = [player(x, [deck.pop(), deck.pop()]) for x in range(player_count)]

    return deck, hands


def flop(deck):
    flop = [deck.pop() for x in range(0, 3)]
    return deck, flop


def turn_and_river(deck):
    card = deck.pop()
    return deck, card


@validate_cards
def is_pair_or_higher(hand, community=None):
    """Technically it is possibly to have 3 pair in hold em,
       with 2 pocket cards and 5 community.
       However, only the highest 2 will be counted.
       Returns format: (rank, count)
    """
    if community is not None:
        hand = hand + community

    cards_counted = Counter([x.rank for x in hand]).most_common(3)

    pairs = filter((lambda x: x[1] > 1), [x for x in cards_counted])

    return pairs if len(pairs) > 0 else False


def is_three_of_a_kind(hand, community=None):
    """Returns rank of top 3 of kind, else False"""
    res = [x[0] for x in is_pair_or_higher(hand, community) if x[1] == 3]
    return max(res) if res else False


def highest_hand(hand, community=None):
    """Find player's highest possible hand."""
    pass
    # high card
    # pair
    # two pair
    # three of a kind
    # straight
    # flush
    # full house
    # four of a kind
    # straight flush
    # royal flush
