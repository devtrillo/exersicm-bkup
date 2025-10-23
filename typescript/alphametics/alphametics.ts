export function solve(puzzle: string): Record<string, number> | undefined {
	// Parse the puzzle
	const [left, right] = puzzle.split("==").map((side) => side.trim());
	const leftWords = left.split("+").map((w) => w.trim());
	const rightWord = right;

	// Get all unique letters
	const allWords = [...leftWords, rightWord];
	const lettersSet = new Set<string>();
	allWords.forEach((word) => {
		for (const c of word) lettersSet.add(c);
	});
	const letters = Array.from(lettersSet);
	if (letters.length > 10) return undefined; // Not enough digits

	// Identify leading letters (cannot be zero)
	const leading = new Set<string>();
	allWords.forEach((word) => leading.add(word[0]));

	// Precompute word to letter indices
	function wordValue(word: string, mapping: Record<string, number>): number {
		let value = 0;
		for (const c of word) {
			value = value * 10 + mapping[c];
		}
		return value;
	}

	// Backtracking
	function search(
		idx: number,
		used: boolean[],
		mapping: Record<string, number>,
	): Record<string, number> | undefined {
		if (idx === letters.length) {
			// All letters assigned, check if valid
			// No leading zeros
			for (const l of leading) {
				if (mapping[l] === 0) return undefined;
			}
			const leftSum = leftWords.reduce(
				(sum, w) => sum + wordValue(w, mapping),
				0,
			);
			const rightVal = wordValue(rightWord, mapping);
			if (leftSum === rightVal) {
				return { ...mapping };
			}
			return undefined;
		}
		const letter = letters[idx];
		for (let d = 0; d <= 9; d++) {
			if (!used[d]) {
				if (d === 0 && leading.has(letter)) continue;
				mapping[letter] = d;
				used[d] = true;
				const result = search(idx + 1, used, mapping);
				if (result) return result;
				used[d] = false;
				delete mapping[letter];
			}
		}
		return undefined;
	}

	return search(0, Array(10).fill(false), {});
}
