import 'dart:collection';
import '../../../base/day.dart';

typedef LoadResult = ({List<List<bool>> indicators, List<List<List<int>>> buttons, List<List<int>> joltages});

class Day10 extends Day {
  Day10() : super(2025, 10);

  @override
  LoadResult parser(dynamic rawInput) {
    List<String> lines = rawInput;
    List<List<bool>> indicators = [];
    List<List<List<int>>> buttons = [];
    List<List<int>> joltages = [];

    for (var line in lines) {
      if (line.trim().isEmpty) continue;
      var parts = line.trim().split(RegExp(r'\s+'));
      
      var indicatorStr = parts.first;
      var joltageStr = parts.last;
      var buttonStrs = parts.sublist(1, parts.length - 1);

      var indList = indicatorStr
          .substring(1, indicatorStr.length - 1)
          .split('')
          .map((ch) => ch == '#')
          .toList();
      indicators.add(indList);

      List<List<int>> lineButtons = [];
      for (var bStr in buttonStrs) {
        var inner = bStr.substring(1, bStr.length - 1);
        if (inner.isNotEmpty) {
          var bIndices = inner.split(',').map((s) => int.parse(s.trim())).toList();
          lineButtons.add(bIndices);
        } else {
          lineButtons.add([]);
        }
      }
      buttons.add(lineButtons);

      // 3. Parsing joltages: "[10,20,30]" -> [10, 20, 30]
      var jolList = joltageStr
          .substring(1, joltageStr.length - 1)
          .split(',')
          .map((s) => int.parse(s.trim()))
          .toList();
      joltages.add(jolList);
    }

    return (indicators: indicators, buttons: buttons, joltages: joltages);
  }

//   IndicatorState toBoolState(List<int> indicator) {
//     return indicator.map((e) => e == 1).toList();
//   }

  int _solvePart1(List<bool> indicator, List<List<int>> buttons) {
    // int num = indicator.length;
    // int targetMask = 0;
    // for (int i = 0; i < num; i++) {
    //   if (indicator[i]) targetMask |= (1 << i);
    // }

    // int startMask = 0;
    // if (startMask == targetMask) return 0;

    // var visited = <int, int>{startMask: 0};
    // var queue = Queue<int>();
    // queue.add(startMask);

    // // Precalcola le maschere dei bottoni per massima efficienza
    // List<int> buttonMasks = [];
    // for (var btn in buttons) {
    //   int m = 0;
    //   for (int idx in btn) {
    //     m |= (1 << idx);
    //   }
    //   buttonMasks.add(m);
    // }

    // while (queue.isNotEmpty) {
    //   int curr = queue.removeFirst();
    //   int times = visited[curr]! + 1;

    //   for (int bMask in buttonMasks) {
    //     int nextCurr = curr ^ bMask;
    //     if (!visited.containsKey(nextCurr)) {
    //       if (nextCurr == targetMask) {
    //         return times;
    //       }
    //       visited[nextCurr] = times;
    //       queue.add(nextCurr);
    //     }
    //   }
    // }
    return 0;
  }

  /// Risolve la Parte 2 tramite Branch-and-Bound ricorsivo con pruning
  int _solvePart2(List<int> joltage, List<List<int>> buttons) {
    // int numButtons = buttons.length;
    // int numRows = joltage.length;
    // int bestCost = 999999999;

    // void search(int btnIdx, List<int> currentJoltage, int currentCost) {
    //   if (currentCost >= bestCost) return;

    //   // Pruning: controlla se ci sono joltages rimasti che nessun bottone rimanente può coprire
    //   for (int r = 0; r < numRows; r++) {
    //     if (currentJoltage[r] > 0) {
    //       bool canCover = false;
    //       for (int b = btnIdx; b < numButtons; b++) {
    //         if (buttons[b].contains(r)) {
    //           canCover = true;
    //           break;
    //         }
    //       }
    //       if (!canCover) return;
    //     }
    //   }

    //   if (btnIdx == numButtons) {
    //     if (currentJoltage.every((v) => v == 0)) {
    //       if (currentCost < bestCost) {
    //         bestCost = currentCost;
    //       }
    //     }
    //     return;
    //   }

    //   // Determina il numero massimo di pressioni possibili per il bottone corrente
    //   int maxPress = 999999;
    //   for (int row in buttons[btnIdx]) {
    //     if (currentJoltage[row] < maxPress) {
    //       maxPress = currentJoltage[row];
    //     }
    //   }

    //   // Prova tutte le combinazioni di pressioni partendo dalla massima (ottimizzazione euristica)
    //   for (int presses = maxPress; presses >= 0; presses--) {
    //     if (currentCost + presses >= bestCost) continue;

    //     List<int> nextJoltage = List.from(currentJoltage);
    //     for (int row in buttons[btnIdx]) {
    //       nextJoltage[row] -= presses;
    //     }

    //     search(btnIdx + 1, nextJoltage, currentCost + presses);
    //   }
    // }

    // search(0, List.from(joltage), 0);
    //return bestCost;
    return 0;
  }

  @override
  Object? part1(covariant LoadResult input) {
    int grandTotal = 0;
    for (int i = 0; i < input.indicators.length; i++) {
      grandTotal += _solvePart1(input.indicators[i], input.buttons[i]);
    }
    return grandTotal;
  }

  @override
  Object? part2(covariant LoadResult input) {
    int grandTotal = 0;
    for (int i = 0; i < input.joltages.length; i++) {
      grandTotal += _solvePart2(input.joltages[i], input.buttons[i]);
    }
    return grandTotal;
  }
}
