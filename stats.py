def count_words(text):
    wordslist = text.split()
    return len(wordslist)

def count_characters(text):
    text = text.lower()
    characters_dict = {}
    for character in text:
        if character in characters_dict:
            characters_dict[character] += 1
        else: characters_dict[character] = 1
    return characters_dict

def sort_by_num(characters):
    return characters["num"]

def sort_characters(characters_dict):
    characters_list = []
    for char, num in characters_dict.items():
        character_temp = {"char": char, "num": num}
        characters_list.append(character_temp)
    characters_list.sort(reverse=True, key=sort_by_num)
    return characters_list