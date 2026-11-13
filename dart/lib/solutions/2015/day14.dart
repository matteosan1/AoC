import '../../../base/day.dart';

const int seconds = 2503;

class Reindeer {
    final String name;
    final int speed;
    final int movement;
    final int rest;
    
    int dist = 0;
    int score = 0;
    int timeMoving = 0;
    int timeResting = 0;
    bool isResting = false;

    Reindeer({
      required this.name,
      required this.speed,
      required this.movement,
      required this.rest,
    });

    void tick() {
      if (isResting) {
        timeResting++;
        if (timeResting == rest) {
          isResting = false;
          timeResting = 0;
        }
      } else {
        timeMoving++;
        dist += speed;
        if (timeMoving == movement) {
          isResting = true;
          timeMoving = 0;
        }
      }
    }
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
    for (int i=0; i<seconds; i++) {
      for (final reindeer in input) {
        reindeer.tick();
      }
    }
    
    final winner = input.reduce((curr, next) => next.dist > curr.dist ? next : curr);
    return winner.dist;
  }

  void awardPointsToLeaders(List<Reindeer> list) {
    if (list.isEmpty) return;

    list.reduce((curr, next) => next.dist > curr.dist ? next : curr);
    int maxDist = list.first.dist;
    // for (int i = 1; i < list.length; i++) {
    //   if (list[i].dist > maxDist) {
    //     maxDist = list[i].dist;
    //   }
    // }

    for (final r in list) {
      if (r.dist == maxDist) {
        r.score++;
      }
    }
  }

  @override
  Object? part2(covariant List<Reindeer> input) {
    for (int i=0; i<seconds; i++) {
      for (final reindeer in input) {
        reindeer.tick();
      }
      awardPointsToLeaders(input);
    }
    
    final winner = input.reduce((curr, next) => next.score > curr.score ? next : curr);
    return winner.score;
  }
}
