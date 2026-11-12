import '../../../base/day.dart';

class Reindeer {
    final String name;
    final int speed;
    final int movement;
    final int rest;
    
    int dist = 0;

    Reindeer({
      required this.name,
      required this.speed,
      required this.movement,
      required this.rest,
    });
}

class Day14 extends Day {
  Day14() : super(2015, 14);

  @override
  List<Reindeer> parser(dynamic rawInput) {
    List<Reindeer> reindeers = [];
    for (final line in rawInput) {
        final parts = line.split(" ");
        final r = Reindeer(name: parts[0], speed: int.parse(parts[3]), movement: int.parse(parts[6]), rest: int.parse(parts[13]));
        reindeers.add(r);
    }
    return reindeers;
  }

  @override
  Object? part1(covariant List<Reindeer> input) {
    for (int i=0; i<2503; i++) {
      for (final reindeer in input) {
        reindeer.dist += reindeer.speed;
      }
    }
  }

  @override
  Object? part2(covariant List<String> input) {
    // TODO: Implementare la parte 2
    return 0;
  }
}
