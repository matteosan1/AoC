import 'dart:io';

import 'package:aoc_2025/aoc_2025.dart';

// final RegExp repeated = RegExp(r"^(..*?)\1{1,}$");
final RegExp repeated = RegExp(r'^(\d+)\1+$');

List<List<int>> parser(String contents) {
    List<String> ranges = contents.split(",").where((s)=> s.isNotEmpty).toList(); 
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

void part1(List<List<int>> ranges) {
    List<int> invalid = [];
  
    for (List<int> r in ranges) {
        invalid.addAll(findRepeatedSequenceNumbers(r[0], r[1]));
    }

    int sumInvalid = invalid.fold(0, (prev, element) => prev + element);
    stdout.write('🎄 Part 1: $sumInvalid');
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

void part2(List<List<int>> ranges) {
    List<int> invalid = [];
  
    for (List<int> r in ranges) {
        invalid.addAll(findInvalidNumbersInRange(r[0], r[1]));
    }
  
    Set<int> uniqueInvalid = invalid.toSet();
    int sumUniqueInvalid = uniqueInvalid.fold(0, (prev, element) => prev + element);
  
    stdout.write('🎄🎅 Part 2: $sumUniqueInvalid');
}

void day2() {
    const title = "Day 2: Gift Shop";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadInput("input_2.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
