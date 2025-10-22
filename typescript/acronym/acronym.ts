export function parse(phrase: string): string {
   return (phrase.match(/[A-Z]+[a-z]*|[a-z]+/g))?.map((word) => word[0].toUpperCase()).join('')||"";
}
