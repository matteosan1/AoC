import 'dart:io';
import 'dart:math';

import 'package:aoc_2025/aoc_2025.dart';

List<String> parser(List<String> contents) {
    return contents;
}

(int, int) findMax(List<int> bank, int start, int end) {
    List<int> sublist = bank.sublist(start, end);
    int val = sublist.reduce(max);
    int index = sublist.indexOf(val);

    return (val, index);
}
  
List<int> convertBank(String bank) {
    return bank.split('').map((char) => int.parse(char)).toList();
}  

void part1(List<String> banks) {
    int totJoltage = 0;
    for (String bankString in banks) {
        List<int> bank = convertBank(bankString);
        final (int jolt, int index) = findMax(bank, 0, bank.length - 1);    
        final (int jolt2, _) = findMax(bank, index + 1, bank.length);
    
        int combinedJoltage = jolt * 10 + jolt2;
    
        totJoltage += combinedJoltage;
    }
  
    stdout.write('🎄 Part 1: $totJoltage');
}
  
void part2(List<String> banks) {
    int totJoltage = 0;
    for (String bankString in banks) {
        List<int> bank = convertBank(bankString);
        List<int> jolts = [];
        int start = 0;
        int end = bank.length - 11;
        for (int i=0; i<12; i++) {
            final (int jolt, int index) = findMax(bank, start, end);
            jolts.add(jolt); 
            start += index + 1;
            end = bank.length - 11 + i + 1;
        }
        int joltage = 0;
        for (int jolt in jolts) {
            joltage = joltage * 10 + jolt;
        }
        totJoltage += joltage;
    }
    stdout.write('🎄🎅 Part 2: $totJoltage');
}

void day3() {
    const title = "Day 3: Lobby";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_3.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
