export function annotate(field: string[]): string[] {
  if (!Array.isArray(field) || field.length === 0) return [];
  const numRows = field.length;
  const numCols = field[0].length;
  if (numCols === 0) return field;

  function countFlowersAround(row: number, col: number): number {
    let count = 0;
    for (let dr = -1; dr <= 1; dr++) {
      for (let dc = -1; dc <= 1; dc++) {
        if (dr === 0 && dc === 0) continue;
        const newRow = row + dr;
        const newCol = col + dc;
        if (
          newRow >= 0 && newRow < numRows &&
          newCol >= 0 && newCol < numCols &&
          field[newRow][newCol] === '*'
        ) {
          count++;
        }
      }
    }
    return count;
  }

  const result: string[] = [];
  for (let row = 0; row < numRows; row++) {
    let annotatedRow = '';
    for (let col = 0; col < numCols; col++) {
      if (field[row][col] === '*') {
        annotatedRow += '*';
      } else {
        const flowerCount = countFlowersAround(row, col);
        annotatedRow += flowerCount === 0 ? ' ' : String(flowerCount);
      }
    }
    result.push(annotatedRow);
  }
  return result;
}
