import '../../../base/day.dart';

typedef LoadResult1 = ({List<List<int>> numbers, List<String> operators});
typedef LoadResult2 = ({List<List<String>> columns, List<String> operators});

class Day06 extends Day {
  Day06() : super(2025, 6);

  @override
  LoadResult1 parserPart1(dynamic rawInput) {
    var dataLines = rawInput.sublist(0, rawInput.length - 1);
    var operators = rawInput.last.trim().split(RegExp(r'\s+'));

    List<List<int>> numbers = dataLines.map((line) {
      return line.trim().split(RegExp(r'\s+')).map(int.parse).toList();
    }).toList();

    return (numbers: numbers, operators: operators);
  }

  @override
  LoadResult2 parserPart2(dynamic rawInput) {
    var dataLines = rawInput.sublist(0, rawInput.length - 1);
    var operators = rawInput.last.trim().split(RegExp(r'\s+')).reversed.toList();

    List<List<String>> charRows = dataLines
        .map((line) => line.split('').reversed.toList())
        .toList();

    int maxLen = charRows.fold(0, (max, row) => row.length > max ? row.length : max);

    List<List<String>> columns = [];
    for (int colIdx = 0; colIdx < maxLen; colIdx++) {
      List<String> colChars = [];
      for (int rowIdx = 0; rowIdx < charRows.length; rowIdx++) {
        if (colIdx < charRows[rowIdx].length) {
          colChars.add(charRows[rowIdx][colIdx]);
        } else {
          colChars.add(' ');
        }
      }
      columns.add(colChars);
    }
    return (columns: columns, operators: operators);
  }

  @override
  Object? part1(covariant LoadResult1 input) {
    List<List<int>> numbers = input.numbers;
    List<String> operators = input.operators;

    int grandTotal = 0;

    for (int col = 0; col < operators.length; col++) {
      String op = operators[col];
      if (op == '+') {
        int colSum = 0;
        for (int row = 0; row < numbers.length; row++) {
          colSum += numbers[row][col];
        }
        grandTotal += colSum;
      } else {
        int colProd = 1;
        for (int row = 0; row < numbers.length; row++) {
          colProd *= numbers[row][col];
        }
        grandTotal += colProd;
      }
    }

    return grandTotal;
  }

  @override
  Object? part2(covariant LoadResult2 input) {
    List<List<String>> columns = input.columns;
    List<String> operators = input.operators;

    int grandTotal = 0;
    int operationIdx = 0;
    int currentResult = 0;
    bool hasStarted = false;

    for (var colChars in columns) {
      String colStr = colChars.join('');
      if (colStr.trim().isEmpty) {
        grandTotal += currentResult;
        currentResult = 0;
        operationIdx++;
        hasStarted = false;
      } else {
        int val = int.parse(colStr.trim());
        String op = operators[operationIdx];
        if (op == '+') {
          currentResult += val;
        } else {
          if (!hasStarted) {
            currentResult = val;
            hasStarted = true;
          } else {
            currentResult *= val;
          }
        }
      }
    }
    grandTotal += currentResult;

    return grandTotal;
  }
}
