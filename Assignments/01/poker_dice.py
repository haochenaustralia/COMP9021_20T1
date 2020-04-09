from random import randint
from collections import defaultdict


def card_hands(random_card_numbers):
    hand = ''.join(str(i) for i in random_card_numbers)

    types = ["1112", "122", "113", "14", "5", "23"]
    print_types = ["One pair", "Two pair", "Three of a kind"
        , "Four of a kind", "Five of a kind", "Full house"]

    hand_type = "Bust"
    if hand == '01234' or hand == '12345':
        hand_type = "Straight"
    else:
        counter = defaultdict(int)
        for number in random_card_numbers:
            counter[number] = counter[number] + 1

        values = list(counter.values())
        values.sort()
        str_values = "".join(str(x) for x in values)
        if str_values in types:
            hand_type = print_types[types.index(str_values)]

    return hand_type


def check_input_cards_not_exist(input_cards, random_cards):
    for card in input_cards:
        if card not in random_cards:
            return True

    return False


def check_input_cards_counter(input_cards, random_cards):
    for card in input_cards:
        if input_cards.count(card) > random_cards.count(card):
            return True

    return False


def play():
    # REPLACE PASS ABOVE WITH YOUR CODE
    card_orders = ["Ace", "King", "Queen", "Jack", "10", "9"]
    random_card_numbers = [randint(0, 5) for _ in range(5)]
    random_card_numbers.sort()

    random_cards = [card_orders[index] for index in random_card_numbers]
    print(f"The roll is: {' '.join(random_cards)}")
    print(f"It is a {card_hands(random_card_numbers)}")

    number = 2
    while (True):
        if number == 2:
            input_value = input("Which dice do you want to keep for the second roll? ")
        else:
            input_value = input("Which dice do you want to keep for the third roll? ")

        if input_value.lower() in ["all"]:
            print("Ok, done.")
            break

        input_cards = input_value.split()
        if check_input_cards_not_exist(input_cards, random_cards) \
                and check_input_cards_counter(input_cards, random_cards):
            print("That is not possible, try again!")
            continue

        # 如果输入的都保留
        input_cards_numbers = [card_orders.index(card) for card in input_cards]
        input_cards_numbers.sort()
        if input_cards_numbers == random_card_numbers:
            print("Ok, done.")
            break

        re_random_card_numbers = [randint(0, 5) for _ in range(5 - len(input_cards))]
        re_random_card_numbers.sort()
        re_random_cards = [card_orders[index] for index in re_random_card_numbers]

        random_cards = input_cards + re_random_cards

        random_card_numbers = [card_orders.index(card) for card in random_cards]
        random_card_numbers.sort()
        random_cards = [card_orders[index] for index in random_card_numbers]
        print(f"The roll is: {' '.join(random_cards)}")
        print(f"It is a {card_hands(random_card_numbers)}")
        number +=1

def simulate(n):
    # REPLACE PASS ABOVE WITH YOUR CODE
    print_types = ["Five of a kind",
                   "Four of a kind",
                   "Full house",
                   "Straight",
                   "Three of a kind",
                   "Two pair",
                   "One pair"]

    result = defaultdict(int)
    for _ in range(n):
        random_card_numbers = [randint(0, 5) for _ in range(5)]
        random_card_numbers.sort()
        hand_type = card_hands(random_card_numbers)
        result[hand_type] =result[hand_type]  + 1

    for key in print_types:
        print(f"{key:15} : {result[key]/n:2.2%}")


# DEFINE OTHER FUNCTIONS
if __name__ == "__main__":
    from random import seed

    seed(0)
    simulate(10)
    simulate(100)

