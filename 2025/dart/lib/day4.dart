import 'dart:io';

import 'package:aoc_2025/aoc_2025.dart';

Map<Point, int> parser(List<String> contents) {
    Map<Point, int> rolls = {};

    for (int y=0; y<contents.length; y++) {
        String line = contents[y];
        for (int x=0; x<line.length; x++) {
            if (line[x] == "@") {
                rolls[Point(x, y)] = 1;
            }
        }
    }
    return rolls;
}

bool accessibleRoll(Point roll, Map<Point, int> rolls, int threshold) {
    int neighborSum = allDirections.values.fold(0, (sum, dir) {
        return sum + (rolls.containsKey(roll + dir) ? rolls[roll + dir]! : 0);
    });
  
    return neighborSum < threshold;
}

void part1(Map<Point, int> rolls) {
    int accessibles = 0;
  
    for (Point roll in rolls.keys) {
        if (accessibleRoll(roll, rolls, 4)) {
            accessibles += 1;
        }
    }

    stdout.write('🎄 Part 1: $accessibles');
}

void part2(Map<Point, int> rolls) {
    int removed = 0;
    
    while (true) {
        List<Point> toRemove = [];
    
        for (Point roll in rolls.keys.toList()) {
            if (accessibleRoll(roll, rolls, 4)) {
                removed += 1;
                toRemove.add(roll);
            }
        }

        if (toRemove.isEmpty) {
            break;
        }

        for (Point r in toRemove) {
            rolls.remove(r);
        }
    }

    stdout.write('🎄🎅 Part 2: $removed');
}

void day4() {
    const title = "Day 4: Printing Department";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_4.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
