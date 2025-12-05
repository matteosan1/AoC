import 'dart:io';

import 'package:aoc_2025/aoc_2025.dart';

List<String> parser(List<String> contents) {
    return contents;
}

void part1(List<int> stones) {
    int length = 0;
 
    stdout.write('🎄 Part 1: $length');
}
  
void part2(List<int> stones) {
    int length = 0;

    stdout.write('🎄🎅 Part 2: $length');
}

void day3() async {
    const title = "";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_4.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
