import '../../../base/day.dart';
import '../../utils/input_loader.dart';

class Day25 extends Day {
  Day25() : super(2015, 25);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  @override
  List<int> parser(dynamic rawInput) {
    final text = rawInput is List ? rawInput.join(' ') : rawInput.toString();
    final regex = RegExp(r'\d+');
    final matches = regex.allMatches(text).map((m) => int.parse(m.group(0)!)).toList();
    return matches;
  }

  @override
  Object? part1(covariant List<int> input) {
    final row = input[0];
    final col = input[1];

    final seq = col*(col+1)~/2 + ((row-1)*(2*col+(row-1)-1))~/2;

    int n = 20151125;
    for (int i=1; i<seq; i++) {
      n = (n*252533)%33554393;
    }
    return n;
  }

  @override
  Object? part2(covariant List<int> input) {
    return 0;
  }
}
