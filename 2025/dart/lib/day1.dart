import 'dart:io';

import 'package:aoc_2025/aoc_2025.dart';

List<String> parser(List<String> content) {
    return content;
}

void part1(List<String> rotations) {
    int counts = 0;
    int pos = 50;

    for (String r in rotations) {
        String dir = r[0];
        int val = int.parse(r.substring(1));

        if (dir == "L") {
            pos -= val;
        } else {
            pos += val;
        }

        pos %= 100;

        if (pos == 0) {
            counts += 1;
        }
    }
    stdout.write('🎄 Part 1: $counts');
}

int countZerosInRotation(int startPos, String direction, int distance) {
    int clicksToFirstZero;

    if (direction == 'R') {
        clicksToFirstZero = 100 - startPos;
    } else if (direction == 'L') {
        clicksToFirstZero = (startPos == 0) ? 100 : (startPos);
    } else {
        return 0;
    }

    if (distance == 0) {
        return 0;
    }
  
    if (distance >= clicksToFirstZero) {
        int zeroCount = 1;
        int remainingDistance = distance - clicksToFirstZero;

        zeroCount += remainingDistance ~/ 100;
        return zeroCount;
    }
  
    return 0;
}

void part2(List<String> rotations) {
    int currentPos = 50;
    int totalZeros = 0;

    for (String rotation in rotations) {
        String direction = rotation[0];
        int distance = int.parse(rotation.substring(1));

        int zerosHit = countZerosInRotation(currentPos, direction, distance);
        totalZeros += zerosHit;
    
        if (direction == 'R') {
            currentPos = (currentPos + distance) % 100;
        } else if (direction == 'L') {
            currentPos = (currentPos - distance) % 100;
        }
    }
    stdout.write('🎄🎅 Part 2: $totalZeros');
}

void day1() {
    const title = "Day 1: Secret Entrance";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_1.txt", parser);
    
    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
