import 'package:aoc/utils/utils.dart';

import '../../../base/day.dart';

typedef People = List<String>;
typedef Happiness = Map<(String, String), int>;
typedef LoadResult = ({Happiness happiness, People people});

class Day13 extends Day {
  Day13() : super(2015, 13);

  @override
  LoadResult parserPart1(dynamic rawInput) {
    Happiness happiness = {};
    Set<String> people = {};
    for (var line in rawInput) {
      final parts = line.split(" ");
      if (line.contains("lose")) {
        happiness[(parts.first, parts.last.substring(0, parts.last.length - 1))] = -int.parse(parts[3]);
      } else {
        happiness[(parts.first, parts.last.substring(0, parts.last.length - 1))] = int.parse(parts[3]);
      }
      people.add(parts.first);
    }

    return (happiness: happiness, people: people.toList());
  }

  @override
  LoadResult parserPart2(dynamic rawInput) {
    LoadResult res = parserPart1(rawInput);
    for (var p in res.people) {
        res.happiness[(p, "Matteo")] = 0;
        res.happiness[("Matteo", p)] = 0;
    }
    res.people.insert(0, "Matteo");

    return res;
  }

  @override
  Object? part1(covariant LoadResult input) {
    int worst = -2^53;
    for (final start in input.people) {
      var remaining = input.people.where((item) => item != start).toList();
        for (var perm in remaining.permutations()) {
        final table = [start, ...perm];
        int total = 0;
    
        for (int i = 0; i < table.length; i++) {
          final current = table[i];
          final neighbor = table[(i + 1) % table.length];
          total += input.happiness[(current, neighbor)]!;
          total += input.happiness[(neighbor, current)]!;
        }    
        if (total > worst) worst = total;
      }
    }
    return worst;
  }

  @override
  Object? part2(covariant LoadResult input) {
    int worst = -2^53;
    for (final start in input.people) {
      var remaining = input.people.where((item) => item != start).toList();
        for (var perm in remaining.permutations()) {
        final table = [start, ...perm];
        int total = 0;
    
        for (int i = 0; i < table.length; i++) {
          final current = table[i];
          final neighbor = table[(i + 1) % table.length];
          total += input.happiness[(current, neighbor)]!;
          total += input.happiness[(neighbor, current)]!;
        }    
        if (total > worst) worst = total;
      }
    }
    return worst;
  }
}
