import 'dart:typed_data';
import '../../../base/day.dart';
import '../../utils/input_loader.dart';

class Day10 extends Day {
  Day10() : super(2015, 10);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  @override
  Uint8List parser(covariant String rawInput) {
    return Uint8List.fromList(rawInput.codeUnits.map((c) => c - 0x30).toList(),);
  }

  Uint8List lookAndSayStep(Uint8List current) {
    final next = Uint8List(current.length * 2);
    int writeIdx = 0;

    int i = 0;
    final n = current.length;

    while (i < n) {
      final digit = current[i];
      int count = 1;

      while (i + count < n && current[i + count] == digit) {
        count++;
      }

      next[writeIdx++] = count;
      next[writeIdx++] = digit;
      i += count;
    }
    return Uint8List.sublistView(next, 0, writeIdx);
  }

  Uint8List evolve(Uint8List start, int steps) {
    var seq = start;
    for (int s = 0; s < steps; s++) {
      seq = lookAndSayStep(seq);
    }
    return seq;
  }

  @override
  Object? part1(covariant Uint8List input) {
    final seq40 = evolve(input, 40);
    part1Result = seq40;
    return seq40.length;
  }

  @override
  Object? part2(covariant Uint8List input) {
      final seq40 = part1Result as Uint8List;
      return evolve(seq40, 10).length;
  }
}
