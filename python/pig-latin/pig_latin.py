def translate(text):
    def translate_word(word):
        vowels = ("a", "e", "i", "o", "u")
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        index = 0
        while index < len(word):
            char = word[index]
            if char in vowels:
                break
            if char == "y" and index != 0:
                break
            if char == "q" and index + 1 < len(word) and word[index + 1] == "u":
                index += 2
                continue
            index += 1

        return word[index:] + word[:index] + "ay"

    return " ".join(translate_word(word) for word in text.split())
