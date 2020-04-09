from random import seed, shuffle
from copy import deepcopy
from collections import defaultdict


def generate_dial_and_centre(for_seed):
    colours = 'CDHS'  # Clubs, Diamonds, Hearts, Spades
    #                                            jacks, queens, kings
    ranks = list(str(x) for x in range(1, 11)) + list('jqk')
    seed(for_seed)
    cards = [colour + rank for colour in colours for rank in ranks]
    shuffle(cards)
    dial = dict.fromkeys(range(1, 13))
    for i in range(12):
        dial[i + 1] = [cards[i + 13 * j] for j in range(4)]
    return dial, [cards[12 + 13 * j] for j in range(4)]


def get_print_card(card, fipped_cards = None):
    colours = 'CDHS'
    unicode_colours = "DCBA"
    generate_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
    unicode_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "D", "E"]
    unicode_base = "\\U0001F0"
    card_colour = card[0]
    # 在colours 里面去寻找这个index
    card_colour_index = colours.find(card_colour)
    unicode_colour = unicode_colours[card_colour_index]
    generate_card_number = card[1:]
    generate_card_index = generate_cards.index(generate_card_number)
    unicode_card = unicode_cards[generate_card_index]
    # 三部分相加
    current_unicode_card = unicode_base + unicode_colour + unicode_card
    current_unicode_card = bytes(current_unicode_card.encode('utf-8'))
    print_unicode_card = current_unicode_card.decode('unicode-escape')

    if fipped_cards and card in fipped_cards:
        return print_unicode_card

    return "hidden" + print_unicode_card

def initial_hour(hour, dial, fipped_cards = None):
    # REPLACE PASS ABOVE WITH YOUR CODE
    print(" ".join([get_print_card(card, fipped_cards) for card in dial[hour]]))


def flipping_cards(new_dial, current_hour, nb_of_steps,
                   flipped_cards_counter,flipped_cards,
                   check_king = 0):
    if nb_of_steps < 0:
        return
    # check 翻开的个数
    if flipped_cards_counter[current_hour] == 4:
        # 是否所有的牌都翻开了。
        for value in flipped_cards.values():
            if len(value) == 4:
                continue
            else:
                if check_king :
                    raise Exception("No success...")
                raise Exception("Could not play that far...")
        else:
            return

    generate_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
    flip_card = new_dial[current_hour].pop()
    generate_card_number = flip_card[1:]
    card_number = generate_cards.index(generate_card_number) + 1

    # 把翻开的牌插入进来
    new_dial[card_number].insert(0,flip_card)
    # 翻开的hour里面记述
    flipped_cards_counter[current_hour] += 1
    # 翻开后的牌，记录下来
    flipped_cards[card_number].append(flip_card)
    # 继续执行
    flipping_cards(new_dial,card_number,nb_of_steps - 1,
                   flipped_cards_counter, flipped_cards,
                   check_king)

def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial,
                                                  centre,
                                                  check_king = 0):
    # REPLACE PRINT() ABOVE WITH YOUR CODE
    new_dial =deepcopy(dial)
    new_dial[13] = deepcopy(centre)
    # 当前翻开牌计数器
    flipped_cards_counter = defaultdict(int)
    # 翻开的牌
    flipped_cards = defaultdict(list)
    try:
        flipping_cards(new_dial, 13, nb_of_steps, flipped_cards_counter,flipped_cards, check_king)
        initial_hour(hour, new_dial, flipped_cards[hour])
    except Exception as e:
        print(e)

def kings_at_end_of_game(dial, centre):
    hour_after_playing_from_beginning_for_at_most(13, 53, dial,centre, 1)
    # REPLACE PRINT() ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS
if __name__ == "__main__":
    dial, centre = generate_dial_and_centre(0)
    # initial_hour(7, dial)
    # hour_after_playing_from_beginning_for_at_most(12, 1, dial, centre)
    kings_at_end_of_game(dial, centre)
    dial, centre = generate_dial_and_centre(18)
    kings_at_end_of_game(dial, centre)
