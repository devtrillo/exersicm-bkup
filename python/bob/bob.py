def response(hey_bob):
    message = hey_bob.strip()
    if not message:
        return "Fine. Be that way!"

    is_question = message.endswith("?")
    letters = [char for char in message if char.isalpha()]
    is_shouting = bool(letters) and all(char.isupper() for char in letters)

    if is_question and is_shouting:
        return "Calm down, I know what I'm doing!"
    if is_shouting:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."
