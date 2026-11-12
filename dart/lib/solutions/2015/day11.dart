import '../../../base/day.dart';
import '../../utils/input_loader.dart';
import '../../utils/utils.dart';

class Day11 extends Day {
  Day11() : super(2015, 11);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  bool hasAtLeastTwoPairs(List<int> units) {
    int pairCount = 0;
    int i = 0;

    while (i < units.length - 1) {
      if (units[i] == units[i + 1]) {
        pairCount++;
        if (pairCount >= 2) return true;        
        i += 2;
      } else {
        i++;
      }
    }

    return false;
  }

  bool check(List<int> units) {
    if (units.contains(111) || units.contains(108) || units.contains(105)) return false;    
    final differences = units.adjacentPairs.map((p) => p.$2 - p.$1).toList();
    if (differences.where((d) => d == 1).length < 3) return false;
    if (!hasAtLeastTwoPairs(units)) return false;

    return true;
  }

  String evolve(String start) {
    var units = start.codeUnits;

      while (true) {      
        for (int i=units.length-1; i>=0; i--) {
          units[i] += 1;
          if (units[i] == 123) {
            units[i] = 97;
            if (i == 0) {
              units.insert(0, 97);
            }
          } else {
            break;
          }
        }

        if (check(units)) {
          break;
        }      
      }
      
      return String.fromCharCodes(units);
  }

  @override
  Object? part1(covariant String input) {
    final pwd = evolve(input);
    return pwd;
  }

  @override
  Object? part2(covariant String input) {
    return evolve(part1Result as String);
  }
}
