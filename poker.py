# -*- coding: utf-8 -*-
from collections import namedtuple, Counter
import random


def construct_deck():
    card = namedtuple("Card", 'rank rankname suit suitsymbol')
    ranks = [str(x) for x in range(2, 15)]
    rank_names = list(map(str, ranks[:-4])) + ['J', 'Q', 'K', 'A']
    suits = ('hearts', "♥"), ('spades', '♠'), \
            ('clubs', '♣'), ('diamonds', '♦')

    return [card(x[0], x[1], y[0], y[1])
            for x in zip(ranks, rank_names) for y in suits]


def shuffle(deck):
    temp = deck[:]
    random.shuffle(temp)
    return temp


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


def is_pair_or_higher(hand, community=None):
    """Technically it is possibly to have 3 pair in hold em,
       with 2 pocket cards and 5 community.
       However, only the highest 2 will be counted.
       Returns list of tuples.
    """
    cards_counted = Counter([x.rank for x in hand]).most_common(3)
    print(cards_counted)

    pairs = filter((lambda x: x[1] > 1), [x for x in cards_counted])

    return pairs if len(pairs) > 0 else False


def is_three_of_a_kind(hand, community=None):
    if community is None:
        return False


def read_cards(hand, community=None):
    """Find player's highest possible hand.
    """
    pass


def print_state(players, community=None):
    player = players[0]
    print("Your hand: "),
    for card in player.hand:
        print(card.rankname + card.suitsymbol),

    if community is not None:
        print("community cards: "),
        for x in [(x.rankname, x.suitsymbol) for x in community]:
            print(x[0] + x[1]),
        # stuff = [template.format(r=x.rankname, s=x.suit) for x in community]
        # print(stuff)


def prompt_player(fn):
    args = {('call', '1'): fn, ('check', '2'): fn,
            ('fold', '3'): lambda x: None}

    arg = input("Call, Check, Fold? ").lower()

    try:
        return next(v for k, v in args.items() if arg in k)
    except:
        print("invalid choice")
        return prompt_player(fn)


def controller():
    deck = shuffle(construct_deck())
    deck_after_deal, players = deal(deck)
    print_state(players)
    thing = prompt_player(flop)
    deck, community_cards = thing(deck)
    # print(community_cards)
    print_state(players, community_cards)
    prompt_player(turn_and_river)

    # deck_after_turn, turn = turn_and_river(deck)
    # deck_after_river, river = turn_and_river(deck)
    # print(len(deck_after_river))

    # print_state(players, [x for x in flop] + [river, turn])
