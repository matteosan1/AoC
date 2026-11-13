import 'dart:typed_data';
import '../../../base/day.dart';

class Grid {
  final int rows;
  final int cols;
  final Int8List _data;

  Grid(this.rows, this.cols) : _data = Int8List(rows * cols);

  factory Grid.fromLines(List<String> lines) {
    final rows = lines.length;
    final cols = lines[0].length;
    final grid = Grid(rows, cols);
    
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        grid.set(r, c, lines[r][c] == '#' ? 1 : 0);
      }
    }
    return grid;
  }

  int get(int r, int c) => _data[r * cols + c];
  void set(int r, int c, int val) => _data[r * cols + c] = val;

  bool inBounds(int r, int c) => r >= 0 && r < rows && c >= 0 && c < cols;

  int countActiveNeighbors(int r, int c) {
    int count = 0;
    for (int dr = -1; dr <= 1; dr++) {
      for (int dc = -1; dc <= 1; dc++) {
        if (dr == 0 && dc == 0) continue;
        final nr = r + dr;
        final nc = c + dc;
        if (inBounds(nr, nc) && get(nr, nc) == 1) {
          count++;
        }
      }
    }
    return count;
  }

  Grid clone() {
    final copy = Grid(rows, cols);    
    copy._data.setAll(0, _data);
    return copy;
  }

  int get totalActive {
    int sum = 0;
    for (int i = 0; i < _data.length; i++) {
      sum += _data[i];
    }
    return sum;
  }
}

class Day18 extends Day {
  Day18() : super(2015, 18);

  @override
  Grid parser(dynamic rawInput) {
    return Grid.fromLines(rawInput);
  }

  void evolve(Grid current) {
    Grid newGrid = current.clone();
    for (int row=0; row<current.rows; row++) {
      for (int col=0; col<current.cols; col++) {
        final cell = current.get(row, col);
        final neighs = current.countActiveNeighbors(row, col);
        if (cell == 1) {
          if (neighs != 2 && neighs != 3) {
            newGrid.set(row, col, 0);  
          }
        } else {
          if (neighs == 3) {
            newGrid.set(row, col, 1);
          } 
        }
      }
    }
    current = newGrid.clone();
  }

  @override
  Object? part1(covariant Grid input) {
    Grid current = input.clone();
    for (int step=0; step<100; step++) {
      evolve(current);
    }

    return current.totalActive;
  }

  void fourCornersOn(Grid current) {
    current.set(0, 0, 1);
    current.set(0, current.cols-1, 1);
    current.set(current.rows-1, 0, 1);
    current.set(current.rows-1, current.cols-1, 1);
  }

  @override
  Object? part2(covariant Grid input) {
    Grid current = input.clone();
    fourCornersOn(current);
    for (int step=0; step<100; step++) {
      evolve(current);
      fourCornersOn(current);
    }

    return current.totalActive;
  }
}
