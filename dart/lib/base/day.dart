import '../utils/input_loader.dart';

abstract class Day {
  final int year;
  final int dayNumber;

  Day(this.year, this.dayNumber);

  String get inputFilePath => '$year/day${dayNumber.toString().padLeft(2, '0')}.txt';

  dynamic loadInputData() {
    return loadMultiLines(inputFilePath, (lines) => lines);
  }

  dynamic parser(dynamic rawInput) {
    return rawInput;
  }

  dynamic parserPart1(dynamic rawInput) {
    return parser(rawInput);
  }

  dynamic parserPart2(dynamic rawInput) {
    return parser(rawInput);
  }

  Object? part1(dynamic input);
  Object? part2(dynamic input);

  void solve() {
    print('========================================');
    print('🎄 Advent of Code $year - Day ${dayNumber.toString().padLeft(2, '0')} 🎄');
    print('========================================');

    try {
      final rawData = loadInputData();

      final input1 = parserPart1(rawData);
      final sw1 = Stopwatch()..start();
      final result1 = part1(input1);
      sw1.stop();
      print('🎄Part 1: $result1  (⏱️ ${sw1.elapsedMicroseconds / 1000000} s)');

      final input2 = parserPart2(rawData);
      final sw2 = Stopwatch()..start();
      final result2 = part2(input2);
      sw2.stop();
      print('🎄🎅Part 2: $result2  (⏱️ ${sw2.elapsedMicroseconds / 1000000} s)');
    } catch (e) {
      print('❌ Errore durante l\'esecuzione: $e');
    }
    print('----------------------------------------\n');
  }
}