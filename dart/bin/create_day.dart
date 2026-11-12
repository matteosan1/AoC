import 'dart:io';
import 'package:path/path.dart' as p;
import 'package:args/args.dart';

void main(List<String> arguments) {
  final parser = ArgParser()
    ..addOption('year', abbr: 'y', help: 'Anno di Advent of Code (es. 2025)')
    ..addOption('day', abbr: 'd', help: 'Giorno da creare (es. 7)');

  try {
    final argResults = parser.parse(arguments);
    final yearStr = argResults['year'];
    final dayStr = argResults['day'];

    if (yearStr == null || dayStr == null) {
      print('❌ Uso corretto: dart run bin/create_day.dart --year <anno> --day <giorno>');
      print('Esempio: dart run bin/create_day.dart -y 2025 -d 7');
      return;
    }

    final year = int.parse(yearStr);
    final day = int.parse(dayStr);
    final dayPadded = day.toString().padLeft(2, '0');

    final dirPath = p.join('lib', 'solutions', '$year');
    final filePath = p.join(dirPath, 'day$dayPadded.dart');

    final dir = Directory(dirPath);
    if (!dir.existsSync()) {
      dir.createSync(recursive: true);
      print('📁 Cartella creata: $dirPath');
    }

    final file = File(filePath);
    if (file.existsSync()) {
      print('⚠️ Il file esiste già: $filePath');      
    } else {
      final className = 'Day$dayPadded';
      final skeletonContent = '''
import '../../../base/day.dart';

class $className extends Day {
  $className() : super($year, $day);

  @override
  Object? part1(covariant List<String> input) {
    // TODO: Implementare la parte 1
    return 0;
  }

  @override
  Object? part2(covariant List<String> input) {
    // TODO: Implementare la parte 2
    return 0;
  }
}
''';

      file.writeAsStringSync('${skeletonContent.trim()}\n');      
      print('✨ File di soluzione generato con successo: $filePath');
    }

    final registryPath = p.join(dirPath, 'registry.dart');
    final registryFile = File(registryPath);
    final importLine = "import 'day$dayPadded.dart';";
    final mapEntry = '  $day: () => Day$dayPadded(),';

    if (!registryFile.existsSync()) {
      final newRegistryContent = '''
import '../../base/day.dart';
import 'day$dayPadded.dart';

final Map<int, Day Function()> solutions$year = {
  $day: () => Day$dayPadded(),
};
''';
      registryFile.writeAsStringSync("${newRegistryContent.trim()}\n");
      print('📝 File registry.dart creato: $registryPath');
    } else {
      var content = registryFile.readAsStringSync();
      bool modified = false;
      
      if (!content.contains(importLine)) {
        // Rimuoviamo \s* dalla regex per fermarci esattamente al punto e virgola
        final importRegex = RegExp(r"import\s+[^;]+;");
        final matches = importRegex.allMatches(content).toList();
        
        if (matches.isNotEmpty) {
          final lastMatch = matches.last;
          final insertIndex = lastMatch.end;

          content = "${content.substring(0, insertIndex)}\n$importLine${content.substring(insertIndex)}";          
          modified = true;
        } else {
          content = "$importLine\n$content";
          modified = true;
        }
      }

      if (!content.contains('$day: () => Day$dayPadded()')) {
        final mapRegex = RegExp(r'(solutions\d*\s*=\s*\{[^}]*)(\})', multiLine: true, dotAll: true);
        if (mapRegex.hasMatch(content)) {
          content = content.replaceFirstMapped(mapRegex, (match) {
            final existingEntries = match.group(1)!;
            final trimmed = existingEntries.trimRight();
            final needsComma = !trimmed.endsWith(',');
            return '$trimmed${needsComma ? ',' : ''}\n$mapEntry\n}';
          });
          modified = true;
        } else {
          print('⚠️ Impossibile trovare la mappa dei giorni in registry.dart. Aggiungi manualmente: $mapEntry');
        }
      }
      
      if (modified) {
        registryFile.writeAsStringSync(content);
        print('🔄 File registry.dart aggiornato con successo.');
      } else {
        print('ℹ️ Il registry.dart contiene già l\'import e l\'entry per questo giorno.');
      }
    }

    final sharedInputPath = r'lib\inputs';
    final inputDirPath = p.join(sharedInputPath, year.toString());
    final inputFilePath = p.join(inputDirPath, 'day$dayPadded.txt');

    final inputDir = Directory(inputDirPath);
    if (!inputDir.existsSync()) {
      try {
        inputDir.createSync(recursive: true);
      } catch (_) {}
    }

    final inputFile = File(inputFilePath);
    if (!inputFile.existsSync()) {
      try {
        inputFile.writeAsStringSync('');
        print('📄 File di input vuoto creato in: $inputFilePath');
      } catch (e) {
        print('⚠️ Impossibile creare il file di input condiviso (controlla i permessi o il path): $e');
      }
    } else {
      print('ℹ️ Il file di input esiste già nella cartella condivisa.');
    }

  } catch (e) {
    print('❌ Errore negli argomenti: $e');
    print(parser.usage);
  }
}