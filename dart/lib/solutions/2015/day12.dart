import 'dart:convert';
import '../../../base/day.dart';
import '../../utils/input_loader.dart';

class Day12 extends Day {
  Day12() : super(2015, 12);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  @override
  Object? part1(covariant String input) {
    final sum = RegExp(r'[-+]?\d+').allMatches(input)
      .fold(0, (acc, match) => acc + int.parse(match.group(0)!),);
    return sum;
  }

int sumNumbersExcludingKey(dynamic node, String forbiddenKey) {
    if (node is int) {
      return node;
    }

    if (node is List) {
      int sum = 0;
      for (final item in node) {
        sum += sumNumbersExcludingKey(item, forbiddenKey);
      }
      return sum;
    }

    if (node is Map<String, dynamic>) {
      if (node.values.contains(forbiddenKey)) {
        return 0;
      }

      int sum = 0;
      for (final value in node.values) {
        sum += sumNumbersExcludingKey(value, forbiddenKey);
      }
      return sum;
    }

    return 0;
  }

  @override
  Object? part2(covariant String input) {
    final parsedData = jsonDecode(input);
    return sumNumbersExcludingKey(parsedData, "red");
  }  
}
