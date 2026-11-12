import '../../../base/day.dart';
import '../../utils/input_loader.dart';
import '../../utils/geometry.dart';

class Day03 extends Day {
  Day03() : super(2015, 3);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  Point move(Point point, int direction) {
    if (direction == 94) {
        return point + directions[0];
    } else if (direction == 118) {
        return point + directions[2];
    } else if (direction == 62) {
        return point + directions[1];
    } else if (direction == 60) {
        return point + directions[3];            
    }
    return point;
  }

  @override
  Object? part1(covariant String input) {
    Point currentPoint = Point(0,0);
    final Set<Point> houses = {currentPoint};

    for (var code in input.codeUnits) {
        currentPoint = move(currentPoint, code);
        houses.add(currentPoint);
    }

    return houses.length;
  }

  @override
  Object? part2(covariant String input) {
    Point santaPoint = Point(0,0);
    Point roboSantaPoint = Point(0,0);
    final Set<Point> houses = {santaPoint};

    final units = input.codeUnits;
  
    for (int i = 0; i < units.length; i += 2) {
      final int code1 = units[i];
      santaPoint = move(santaPoint, code1);
      final int code2 = units[i+1];
      roboSantaPoint = move(roboSantaPoint, code2);
      houses.add(santaPoint);
      houses.add(roboSantaPoint);
    }

    return houses.length;
  }
}
