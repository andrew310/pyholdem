# -*- coding: utf-8 -*-


    # ('hearts', "♥"), ('spades', '♠'), \
    #         ('clubs', '♣'), ('diamonds', '♦')


def print_state(players, community=None):
    player = players[0]
    print("Your hand: "),
    for card in player.hand:
        print(card.rankname + card.suit),

    if community is not None:
        print("community cards: "),
        for x in [(x.rankname, x.suit) for x in community]:
            print(x[0] + x[1]),
        # stuff = [template.format(r=x.rankname, s=x.suit) for x in community]
        # print(stuff)


def controller():
    deck = construct_deck()
    print(deck)
    # deck_after_deal, players = deal(deck)
    # print_state(players)
    # thing = prompt_player(flop)
    # deck, community_cards = thing(deck)
    # # print(community_cards)
    # print_state(players, community_cards)
    # prompt_player(turn_and_river)

    # deck_after_turn, turn = turn_and_river(deck)
    # deck_after_river, river = turn_and_river(deck)
    # print(len(deck_after_river))

    # print_state(players, [x for x in flop] + [river, turn])

controller()


def prompt_player(fn):
    args = {('call', '1'): fn, ('check', '2'): fn,
            ('fold', '3'): lambda x: None}

    arg = input("Call, Check, Fold? ").lower()

    try:
        return next(v for k, v in args.items() if arg in k)
    except:
        print("invalid choice")
        return prompt_player(fn)
