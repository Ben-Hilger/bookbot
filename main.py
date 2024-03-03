
def sort_on(dict):
    return dict["count"]

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        words = len(file_contents.split())

        lowerCased = file_contents.lower()

        characterDictionary = {}

        for character in lowerCased:
            if not character.isalpha():
                continue
            if character in characterDictionary:
                characterDictionary[character] += 1
            else:
                characterDictionary[character] = 1

        convertedCharacterDictionary = []

        for character in characterDictionary:
            convertedCharacterDictionary.append({"character": character, "count": characterDictionary[character]})

        convertedCharacterDictionary.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {path_to_file} ---")
        
        print(f"{words} words found in the document\n")

        for character in convertedCharacterDictionary:
            print(f"The '{character["character"]}' was found {character["count"]} times")        

        print("--- End report ---")
main()
