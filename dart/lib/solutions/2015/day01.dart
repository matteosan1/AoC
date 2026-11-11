import '../../../base/day.dart';
import '../../utils/input_loader.dart';

class Day01 extends Day {
  Day01() : super(2015, 1);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  @override
  Object? part1(covariant String input) {
    int floor = 0;
    for (var char in input.split('')) {
      if (char == '(') {
        floor += 1;
      } else {
        floor -= 1;
      }
    }
    return floor;
  }

  @override
  Object? part2(covariant String input) {
    int floor = 0;
    int pos = 1;

    for (var char in input.split('')) {
      if (char == '(') {
        floor += 1;
      } else {
        floor -= 1;
        if (floor == -1) {
          break;
        }
      }
      pos += 1;
    }
    return pos;
  }
}
