import 'package:args/args.dart';
import 'package:aoc/base/day.dart';

// dart run bin/main.dart --year 2023 --day 1
import 'package:aoc/solutions/2015/registry.dart' as year2015;
import 'package:aoc/solutions/2025/registry.dart' as year2025;

final Map<int, Map<int, Day Function()>> masterRegistry = {
  2015: year2015.solutions2015,
  2025: year2025.solutions2025,
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
  final yearMap = masterRegistry[year];
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
  final sortedYears = masterRegistry.keys.toList()..sort();
  for (var year in sortedYears) {
    final sortedDays = masterRegistry[year]!.keys.toList()..sort();
    for (var day in sortedDays) {
      masterRegistry[year]?[day]?.call().solve();
    }
  }
}