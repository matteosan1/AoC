import 'package:aoc/utils/utils.dart';

import '../../../base/day.dart';

typedef Cities = List<String>;
typedef Distances = Map<(String, String), int>;
typedef LoadResult = ({Cities cities, Distances distancies});

class Day09 extends Day {
  Day09() : super(2015, 9);

  @override
  LoadResult parser(dynamic rawInput) {
    Distances distancies = {};
    Set<String> cities = {};
      for (var line in rawInput) {      
      final [dests, distance] = line.split(" = ");
      final [start, end] = dests.split(" to ");
      distancies[(start, end)] = int.parse(distance);
      cities.add(start);
      cities.add(end);
    }

    return (cities: cities.toList(), distancies: distancies);
  }

  @override
  Object? part1(covariant LoadResult input) {
    int best = 1 << 62;
    int worst = 0;

    for (var path in input.cities.permutations()) {
      int total = 0;
    
      for (int i = 0; i < path.length - 1; i++) {
        total += input.distancies[(input.cities[i], input.cities[i+1])]!;
      }
      if (total < best) best = total;
      if (total > worst) worst = total;
    }

    part1Result = worst;
    return best;
  }

  @override
  Object? part2(covariant LoadResult input) {
      return part1Result as int;
  }
}
