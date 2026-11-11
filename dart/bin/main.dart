import 'package:args/args.dart';
import 'package:aoc/base/day.dart';

// dart run bin/main.dart --year 2023 --day 1
import 'package:aoc/solutions/2025/day01.dart';
import 'package:aoc/solutions/2025/day02.dart';
import 'package:aoc/solutions/2025/day03.dart';
import 'package:aoc/solutions/2025/day04.dart';
import 'package:aoc/solutions/2025/day05.dart';
import 'package:aoc/solutions/2025/day06.dart';
// import 'package:aoc/solutions/2025/day07.dart';
// import 'package:aoc/solutions/2025/day08.dart';
import 'package:aoc/solutions/2025/day09.dart';
import 'package:aoc/solutions/2025/day10.dart';
import 'package:aoc/solutions/2025/day11.dart';
import 'package:aoc/solutions/2025/day12.dart';

final Map<int, Map<int, Day Function()>> registry = {
  2025: {
    1: () => Day01(),
    2: () => Day02(),
    3: () => Day03(),
    4: () => Day04(),
    5: () => Day05(),
    6: () => Day06(),
    // 7: () => Day07(),
    // 8: () => Day08(),
    9: () => Day09(),
    10: () => Day10(),
    11: () => Day11(),
    12: () => Day12(),
  },

};

void main(List<String> arguments) {
  final parser = ArgParser()
    ..addOption('year', abbr: 'y', help: 'Anno di Advent of Code')
    ..addOption('day', abbr: 'd', help: 'Giorno da eseguire')
    ..addFlag('all', abbr: 'a', negatable: false, help: 'Esegui tutti i giorni registrati');

  try {
    final argResults = parser.parse(arguments);

    if (argResults['all'] == true) {
      runAll();
      return;
    }

    final yearStr = argResults['year'];
    final dayStr = argResults['day'];

    if (yearStr == null || dayStr == null) {
      print('Uso corretto: dart run bin/main.dart --year <anno> --day <giorno>');
      print('Oppure: dart run bin/main.dart --all');
      return;
    }

    final year = int.parse(yearStr);
    final day = int.parse(dayStr);

    runDay(year, day);
  } catch (e) {
    print('Errore negli argomenti: $e');
    print(parser.usage);
  }
}

void runDay(int year, int dayNumber) {
  final yearMap = registry[year];
  if (yearMap == null) {
    print('Nessuna soluzione trovata per l\'anno $year.');
    return;
  }

  final dayFactory = yearMap[dayNumber];
  if (dayFactory == null) {
    print('Il giorno $dayNumber per l\'anno $year non è stato ancora implementato.');
    return;
  }

  final puzzle = dayFactory();
  puzzle.solve();
}

void runAll() {
  final sortedYears = registry.keys.toList()..sort();
  for (var year in sortedYears) {
    final sortedDays = registry[year]!.keys.toList()..sort();
    for (var day in sortedDays) {
      // registry[year]![day]().solve();
      registry[year]?[day]?.call().solve();
    }
  }
}