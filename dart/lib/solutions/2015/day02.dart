import 'dart:math';
import '../../../base/day.dart';
import '../../utils/input_loader.dart';

typedef Sides = ({int l, int w, int h});

class Day02 extends Day {
  Day02() : super(2015, 2);

  @override
  List<Sides> parser(dynamic rawInput) {
    List<String> lines = rawInput;
    List<Sides> sides = [];

    for (var line in lines) {
      if (line.trim().isEmpty) continue;

      final parts = line.split('x');
      sides.add((
        l: int.parse(parts[0]), 
        w: int.parse(parts[1]), 
        h: int.parse(parts[2]),
      ));
    }
    return sides;
  }

  @override
  Object? part1(covariant List<Sides> input) {
    int paper = 0;
    for (var box in input) {
      final s1 = box.l*box.w;
      final s2 = box.w*box.h;
      final s3 = box.l*box.h;
      final extra = [s1, s2, s3].reduce(min);

      paper += extra + s1*2 + s2*2 + s3*2;
    }
    return paper;
  }

  @override
  Object? part2(covariant List<Sides> input) {
    int ribbon = 0;
    for (Sides box in input) {
      final volume = box.l*box.w*box.h;
      final maxSide = [box.l, box.w, box.h].reduce(max);

      ribbon += box.l*2 + box.w*2 + box.h*2 - maxSide*2 + volume;
    }
    return ribbon;
  }
}
