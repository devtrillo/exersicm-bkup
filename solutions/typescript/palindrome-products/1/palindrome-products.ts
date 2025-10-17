interface Input {
  maxFactor: number;
  minFactor?: number;
}

interface SearchResult {
  value: number | null;
  factors: [number, number][];
}

interface Result {
  smallest: SearchResult;
  largest: SearchResult;
}

export function generate({ minFactor = 1, maxFactor }: Input): Result {
  if (minFactor > maxFactor) throw new Error("min must be <= max");

  const result: Result = {
    smallest: { value: null, factors: [] },
    largest: { value: null, factors: [] },
  };
  for (let i = minFactor; i <= maxFactor; i++) {
    for (let j = i; j <= maxFactor; j++) {
      const product = i * j;
      const isPalindrome = isPalindromeNumber(product);
      if (!isPalindrome) continue;
      if (result.smallest.value === null || product < result.smallest.value) {
        result.smallest = { value: product, factors: [[i, j]] };
      } else if (result.smallest.value === product) {
        result.smallest.factors.push([i, j]);
      }
      if (result.largest.value === null || product > result.largest.value) {
        result.largest = { value: product, factors: [[i, j]] };
      } else if (result.largest.value === product) {
        result.largest.factors.push([i, j]);
      }
    }
  }
  return result;
}

function isPalindromeNumber(input: number): boolean {
  const numberString = input.toString();
  const reversedStr = numberString.split("").reverse().join("");
  return numberString === reversedStr;
}
