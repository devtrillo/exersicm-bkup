
export class Matrix {
  private _rows: number[][];
  private _columns: number[][];

  constructor(matrix: string) {
    // Parse rows
    this._rows = matrix
      .split('\n')
      .map(row => row.trim().split(/\s+/).map(Number));

    // Parse columns
    const numCols = this._rows[0]?.length || 0;
    this._columns = Array.from({ length: numCols }, (_, colIdx) =>
      this._rows.map(row => row[colIdx])
    );
  }

  get rows(): number[][] {
    return this._rows;
  }

  get columns(): number[][] {
    return this._columns;
  }
}
