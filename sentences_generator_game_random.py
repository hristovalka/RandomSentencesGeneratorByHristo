import random


def get_random_word(words):
    return random.choice(words)


names = ["Hristo", "Janet", "Manuela", "Anton"]
places = ["Plovdiv", "Sofia", "Varna", "Burgas"]
verbs = ["eats", "holds", "goes", "takes", "sees", "brings", "holds"]
nouns = ["beans", "stones", "laptop", "bikes", "cake", "apple"]
adverbs = ["slowly", "warmly", "sadly", "rapidly", "sad", "diligently"]
details = ["near the river", "at home", "in the park", "in the sky"]


while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_details = get_random_word(details)
    print(f"{random_name} from {random_place} {random_verb} {random_noun}")
    input("Click [ENTER] to continue...")










