def find_anagrams(word, candidates):
    normalized = word.casefold()
    signature = sorted(normalized)
    matches = []
    for candidate in candidates:
        candidate_folded = candidate.casefold()
        if candidate_folded == normalized:
            continue
        if sorted(candidate_folded) == signature:
            matches.append(candidate)
    return matches
