import 'dart:math';
import '../../../base/day.dart';

class Day03 extends Day {
  Day03() : super(2025, 3);

  (int, int) findMax(List<int> bank, int start, int end) {
    List<int> sublist = bank.sublist(start, end);
    int val = sublist.reduce(max);
    int index = sublist.indexOf(val);

    return (val, index);
  }

  List<int> convertBank(String bank) {
    return bank.split('').map((char) => int.parse(char)).toList();
  }  

  @override
  Object? part1(covariant List<String> input) {
    int totJoltage = 0;
    for (String bankString in input) {
        List<int> bank = convertBank(bankString);
        final (int jolt, int index) = findMax(bank, 0, bank.length - 1);    
        final (int jolt2, _) = findMax(bank, index + 1, bank.length);
    
        int combinedJoltage = jolt * 10 + jolt2;
    
        totJoltage += combinedJoltage;
    }
  
    return totJoltage;
  }

  @override
  Object? part2(covariant List<String> input) {
    int totJoltage = 0;
    for (String bankString in input) {
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
    return totJoltage;

  }
}
