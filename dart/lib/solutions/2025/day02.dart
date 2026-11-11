import '../../../base/day.dart';

class Day02 extends Day {
  Day02() : super(2025, 2);

  // final RegExp repeated = RegExp(r"^(..*?)\1{1,}$");
  final RegExp repeated = RegExp(r'^(\d+)\1+$');

  @override
  dynamic parser(dynamic rawInput) {
    List<String> ranges = rawInput.split(",").where((s)=> s.isNotEmpty).toList(); 
    return ranges.map((range) {
        List<String> parts = range.split('-');
        return parts.map((part) => int.parse(part)).toList();
    }).toList();
  }

  List<int> findRepeatedSequenceNumbers(int start, int end) {
    List<int> matchingNumbers = [];

    for (int n = start; n <= end; n++) {
        String s = n.toString();
        int length = s.length;

        if (length % 2 == 0) {
            int halfLength = length ~/ 2;

            String firstHalf = s.substring(0, halfLength);
            String secondHalf = s.substring(halfLength);

            if (firstHalf == secondHalf) {
                matchingNumbers.add(n);
            }
        }
    }
    return matchingNumbers;
  }

  @override
  Object? part1(covariant List<List<int>> input) {
    List<int> invalid = [];
  
    for (List<int> r in input) {
        invalid.addAll(findRepeatedSequenceNumbers(r[0], r[1]));
    }

    int sumInvalid = invalid.fold(0, (prev, element) => prev + element);
    return sumInvalid;
  }

  List<int> findInvalidNumbersInRange(int start, int end) {
    List<int> invalidNumbers = [];
  
    for (int n = start; n <= end; n++) {
        String s = n.toString();
        if (repeated.hasMatch(s)) {
            invalidNumbers.add(n);
        }
    }
    return invalidNumbers;
  }

  @override
  Object? part2(covariant List<List<int>> input) {
    List<int> invalid = [];
  
    for (List<int> r in input) {
        invalid.addAll(findInvalidNumbersInRange(r[0], r[1]));
    }
  
    Set<int> uniqueInvalid = invalid.toSet();
    int sumUniqueInvalid = uniqueInvalid.fold(0, (prev, element) => prev + element);
  
    return sumUniqueInvalid;
  }
}
