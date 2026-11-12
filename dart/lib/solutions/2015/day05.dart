import '../../../base/day.dart';

class Day05 extends Day {
  Day05() : super(2015, 5);

  bool isNiceString(String s) {
  if (s.contains('ab') || s.contains('cd') || s.contains('pq') || s.contains('xy')) {
    return false;
  }

  int vowelCount = 0;
  bool hasDoubleLetter = false;

  for (int i = 0; i < s.length; i++) {
    var char = s[i];

    if (char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u') {
      vowelCount++;
    }

    if (i < s.length - 1 && s[i] == s[i + 1]) {
      hasDoubleLetter = true;
    }
  }

  return vowelCount >= 3 && hasDoubleLetter;
}

  @override
  Object? part1(covariant List<String> input) {
    int nice = 0;

    for (var line in input) {
        if (isNiceString(line)) nice += 1;
    }

    return nice;
  }

  bool isNiceStringPart2(String s) {
    bool hasNonOverlappingPair = false;
    Map<String, List<int>> pairIndices = {};

    for (int i = 0; i < s.length - 1; i++) {
      String pair = s.substring(i, i + 2);
      pairIndices.putIfAbsent(pair, () => []).add(i);
    }

    for (var indices in pairIndices.values) {
      if (indices.length >= 2) {
        for (int i = 0; i < indices.length; i++) {
          for (int j = i + 1; j < indices.length; j++) {
            if (indices[j] - indices[i] >= 2) {
              hasNonOverlappingPair = true;
              break;
            }
          }
          if (hasNonOverlappingPair) break;
        }
      }
      if (hasNonOverlappingPair) break;
    }

    if (!hasNonOverlappingPair) return false;

    bool hasRepeatedWithOneBetween = false;
    for (int i = 0; i < s.length - 2; i++) {
      if (s[i] == s[i + 2]) {
        hasRepeatedWithOneBetween = true;
        break;
      }
    }

    return hasRepeatedWithOneBetween;
  }

  @override
  Object? part2(covariant List<String> input) {
    int nice = 0;

    for (var line in input) {
        if (isNiceStringPart2(line)) nice += 1;
    }

    return nice;
  }
}
