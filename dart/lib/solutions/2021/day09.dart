import '../../../base/day.dart';
import '../../utils/geometry.dart';
import '../../utils/search_algo.dart';

class Day09 extends Day {
  Day09() : super(2021, 9);

  @override
  Map<Point, int> parser(dynamic rawInput) {
    Map<Point, int> heights = {};
    for (final (y, line) in rawInput.indexed) {
      for (int x=0; x<line.length; x++) {
        heights[Point(x, y)] = line[x];
      }
    }
    return heights;
  }

  @override
  Object? part1(covariant Map<Point, int> input) {
    int riskFactor = 0;
    List<Point> minima = [];
    for (final MapEntry(:key, :value) in input.entries) {
      bool isMin = directions.every((d) {
        final neighborKey = key + d;
        return !input.containsKey(neighborKey) || input[neighborKey]! >= value;
      });
      if (isMin) {
        riskFactor += value+1;
        minima.add(key);
      }
    }
    part1Result = minima;
    return riskFactor;
  }

  @override
  Object? part2(covariant Map<Point, int> input) {
    List<int> basinSize = [];
    final floodFill = FloodFill(input);

    for (final start in part1Result as List<Point>) {
      basinSize.add(floodFill.getBasinSize(start, (neighbor) => input[neighbor] != 9));
    }

    basinSize.sort((a, b) => b.compareTo(a));
    return basinSize[0] * basinSize[1] * basinSize[2];
  }
}
