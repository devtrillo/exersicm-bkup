def recite(start_verse, end_verse):
    parts = [
        ("the house that Jack built.", ""),
        ("the malt", "that lay in"),
        ("the rat", "that ate"),
        ("the cat", "that killed"),
        ("the dog", "that worried"),
        ("the cow with the crumpled horn", "that tossed"),
        ("the maiden all forlorn", "that milked"),
        ("the man all tattered and torn", "that kissed"),
        ("the priest all shaven and shorn", "that married"),
        ("the rooster that crowed in the morn", "that woke"),
        ("the farmer sowing his corn", "that kept"),
        ("the horse and the hound and the horn", "that belonged to"),
    ]

    verses = []
    for verse_index in range(start_verse, end_verse + 1):
        verse_parts = ["This is "]
        for part_index in range(verse_index - 1, 0, -1):
            subject, verb = parts[part_index]
            verse_parts.append(subject)
            verse_parts.append(" ")
            verse_parts.append(verb)
            verse_parts.append(" ")
        verse_parts.append(parts[0][0])
        verses.append("".join(verse_parts))

    return verses
