import '../../../base/day.dart';
import '../../utils/geometry.dart';
import '../../utils/search_algo.dart';

typedef HeatMap = ({Map<Point, int> grid, Point start, Point end, List<Point> lowers});

class Day12 extends Day {
  Day12() : super(2022, 12);

  @override
  HeatMap parser(dynamic rawInput) {
    Map<Point, int> grid = {};
    late Point start;
    late Point end;
    List<Point> lowers = [];

    for (final (y, line) in rawInput.indexed) {
      for (int x=0; x<line.length; x++) {
        if (line[x] == 'S' || line[x] == 'a') {
          grid[Point(x, y)] = 'a'.codeUnitAt(0);
          lowers.add(Point(x, y));
          if (line[x] == 'S') start = Point(x, y);
        } else if (line[x] == 'E') {
          grid[Point(x, y)] = 'z'.codeUnitAt(0);
          end = Point(x, y);        
        } else {
          grid[Point(x, y)] = line.codeUnitAt(x);
        }        
      }
    }
    return (grid: grid, start: start, end: end, lowers: lowers);
  }

  @override
  Object? part1(covariant HeatMap input) {
    final path = PathFindingBFS.findPath(input.start, input.end, 
      (current, neighbor) {
        if (!input.grid.containsKey(neighbor)) return false;
        final currentHeight = input.grid[current]!;
        final neighborHeight = input.grid[neighbor]!;
        return neighborHeight <= currentHeight + 1;
      },
    );

    return path?.length;
  }

  @override
  Object? part2(covariant HeatMap input) {
    int minLength = 100000000;
    for (final start in input.lowers) {
      final path = PathFindingBFS.findPath(start, input.end, 
        (current, neighbor) {
          if (!input.grid.containsKey(neighbor)) return false;
          final currentHeight = input.grid[current]!;
          final neighborHeight = input.grid[neighbor]!;
          return neighborHeight <= currentHeight + 1;
        },
      );

      if (path != null && path.length < minLength) {
        minLength = path.length;
      }
    }

    return minLength;
  }
}



Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
