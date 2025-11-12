
export function isPangram(sentence: string): boolean {
  const alphabet = new Set<string>()
  for (const char of sentence.toLowerCase()) {
    if (char >= 'a' && char <= 'z') {
      alphabet.add(char)
    }
  }
  return alphabet.size === 26
}
