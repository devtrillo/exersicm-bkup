export function convert(
  digits: number[],
  inputBase: number,
  outputBase: number,
): number[] {
  if (inputBase <= 1) throw new Error("Wrong input base");

  if (
    digits.length == 0 ||
    (digits.length > 1 &&
      (digits[0] == 0 || digits.every((elt) => elt == 0))) ||
    digits.some((elt) => elt < 0 || elt >= inputBase)
  )
    throw new Error("Input has wrong format");

  if (outputBase <= 1 || outputBase % 1 != 0)
    throw new Error("Wrong output base");

  let nb = digits
    .reverse()
    .map((elt, i) => elt * Math.pow(inputBase, i))
    .reduce((elt, acc) => elt + acc, 0);

  const result = [];

  while (true) {
    if (nb < outputBase) {
      result.unshift(nb);
      break;
    }
    result.unshift(nb % outputBase);
    nb = Math.floor(nb / outputBase);
  }

  return result;
}
