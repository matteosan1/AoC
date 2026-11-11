import '../../../base/day.dart';
import '../../utils/geometry.dart';

class Day04 extends Day {
  Day04() : super(2025, 4);

  @override
  Map<Point, int> parser(dynamic rawInput) {
    Map<Point, int> rolls = {};
    List<String> lines = rawInput;

    for (int y=0; y<lines.length; y++) {
        String line = lines[y];
        for (int x=0; x<line.length; x++) {
            if (line[x] == "@") {
                rolls[Point(x, y)] = 1;
            }
        }
    }
    return rolls;
  }

  bool accessibleRoll(Point roll, Map<Point, int> rolls, int threshold) {
    int neighborSum = allDirections.values.fold(0, (sum, dir) {
        return sum + (rolls.containsKey(roll + dir) ? rolls[roll + dir]! : 0);
    });
  
    return neighborSum < threshold;
  }

  @override
  Object? part1(covariant Map<Point, int> input) {
    int accessibles = 0;
  
    for (Point roll in input.keys) {
      if (accessibleRoll(roll, input, 4)) {
        accessibles += 1;
      }
    }

    return accessibles;  
  }

  @override
  Object? part2(covariant Map<Point, int> input) {
    int removed = 0;
    
    while (true) {
      List<Point> toRemove = [];
    
      for (Point roll in input.keys.toList()) {
        if (accessibleRoll(roll, input, 4)) {
          removed += 1;
          toRemove.add(roll);
        }
      }

      if (toRemove.isEmpty) {
        break;
      }

      for (Point r in toRemove) {
        input.remove(r);
      }
    }

    return removed;
  }
}
