import random

card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
card_value = [i for i in range(1, 14)] * 4
deck = [item for item in zip(card_face, card_value)]
random.shuffle(deck)
player_cards = list()
player_cards.append(deck.pop())
print("Your cards:", player_cards)
answer = input("請問你要補牌嗎？")
while answer != "n" and answer != "N":
    import random
    print("以下是你的牌")
    card_face = ["Diamond"] * 13 + ["Spade"] * 13 + ["Heart"] * 13 + ["Club"] * 13
    card_value = [i for i in range(1, 14)]* 4
    deck = [item for item in zip(card_face, card_value)]
    random.shuffle(deck)
    player_cards = list()
    player_cards.append(deck.pop())
    print("Your cards:", player_cards)
    answer = input("請問你要補牌嗎？") 
    
    pass
print("以下是你的牌")
deck = zip(card_face, card_value)
player_cards.append(deck)
for deck in deck:
            print(deck)

print("你總共得到",(card_value))
    