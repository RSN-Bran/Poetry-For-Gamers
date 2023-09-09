import os
import json
import random


tdir = os.getcwd()

class Card:
    def __init__(self, category, subcategories):
        self.category=category
        self.subcategories=subcategories
    def choose_subcategory(self):
        index = random.randint(0, len(self.subcategories)-1)
        return self.subcategories[index]

def parse_cards():
    data_file = open(tdir+os.sep+"data.json")          
    json_cards = json.load(data_file)
    cards = []
    for card in json_cards:
        cards.append(Card(card["category"], card["subcategories"]))
    print(f"{len(cards)} cards loaded")
    return cards

def main():
    print("Loading Game...")
    cards = parse_cards()
    used_indexes = []
    print("Ready to go?")
    input()
    while True:
        if len(used_indexes) == len(cards):
            print("All cards used. Game is over")
            break
        card_index = -1
        while True:
            card_index = random.randint(0, len(cards)-1)
            if card_index not in used_indexes:
                used_indexes.append(card_index)
                break;
        
        current_card = cards[card_index]
        print(f"Current Card:\n{current_card.category} - 1 Point\n{current_card.choose_subcategory()} - 3 Points")
        input()



main()