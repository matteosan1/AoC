import '../../../base/day.dart';

class Day24 extends Day {
  Day24() : super(2015, 24);

  @override
  List<int> parser(dynamic rawInput) {
    return rawInput.map<int>(int.parse).toList()..sort((int a, int b) => b.compareTo(a));
  }

  int? solveForGroups(List<int> packages, int targetWeight) {
    for (int size = 1; size <= packages.length; size++) {
      int? minQE;

      void findCombinations(int startIndex, int currentCount, int currentSum, int currentQE) {
        if (currentSum > targetWeight || currentCount > size) return;
        
        if (currentCount == size && currentSum == targetWeight) {
          if (minQE == null || currentQE < minQE!) {
            minQE = currentQE;
          }
          return;
        }

        for (int i = startIndex; i < packages.length; i++) {
          if (currentSum + packages[i] > targetWeight) continue;          
          findCombinations(i + 1, currentCount + 1, currentSum + packages[i], currentQE * packages[i]);
        }
      }

      findCombinations(0, 0, 0, 1);
      if (minQE != null) {
        return minQE;
      }
    }
    return null;
  }
    
  @override
  Object? part1(covariant List<int> input) {
    part1Result = input.reduce((a, b) => a + b);
    final targetWeight = (part1Result as int)  ~/ 3;
    return solveForGroups(input, targetWeight);
  }

  @override
  Object? part2(covariant List<int> input) {
    final targetWeight = (part1Result as int)  ~/ 4;
    return solveForGroups(input, targetWeight);
  }
}
