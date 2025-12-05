import 'dart:io';
import 'dart:math';

import 'package:aoc_2025/aoc_2025.dart'; 


//List<int> startPoints = ranges.map((r) => r[0]).toList();

int bisectRight(List<int> array, int target) {
    int low = 0;
    int high = array.length;

    while (low < high) {
        int mid = low + ((high - low) ~/ 2);
        if (array[mid] <= target) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}

typedef LoadResult = ({List<List<int>> ranges, List<int> ids});

List<List<int>> mergeIntervals(List<List<int>> intervals) {
    final sortedIntervals = List<List<int>>.from(intervals);
    sortedIntervals.sort((a, b) => a[0].compareTo(b[0]));

    final merged = [sortedIntervals[0]];
    for (final currentInterval in sortedIntervals.sublist(1)) {
        final currentStart = currentInterval[0];
        final currentEnd = currentInterval[1];
        final lastMerged = merged.last;
        final lastMergedEnd = lastMerged[1];
        if (currentStart <= lastMergedEnd) {
            lastMerged[1] = max(lastMergedEnd, currentEnd);
        } else {
            merged.add(currentInterval);
        }
    }
    return merged;
}

LoadResult parser(List<String> content) {
    final ranges = <List<int>>[];
    final ids = <int>[];
    for (final line in content) {
        if (line.trim().isEmpty) {
            continue;
        }

        if (line.contains('-')) {
            final parts = line.split('-').map(int.parse).toList();
            ranges.add(parts);
        } else {
            ids.add(int.parse(line.trim()));
        }
    }
    final mergedRanges = mergeIntervals(ranges);

    return (ranges: mergedRanges, ids: ids);
}

void part1(List<List<int>> ranges, List<int> ids) {
    List<int> startPoints = ranges.map((r) => r[0]).toList();
    var fresh = 0;
    for (final item in ids) {
        int index = bisectRight(startPoints, item);
        if ((index > 0) && (item < ranges[index-1][1])) {
            fresh += 1;    
        }

        // for (final range in ranges) {
        //     final start = range[0];
        //     final end = range[1];

        //     if (start <= item && item <= end) {
        //         fresh += 1;
        //         break;
        //     }
        // }
    }
    stdout.write('🎄 Part 1: $fresh');
}

void part2(List<List<int>> ranges) {
    final freshIDs = ranges.map((range) => range[1] - range[0] + 1).fold<int>(0, (prev, element) => prev + element);
    stdout.write('🎄🎅 Part 2: $freshIDs');
}

// //  part1(inputs.ranges, inputs.ids);
// # int countFreshItems(List<int> ids) {

// #     int freshCount = 0;

 

// #     for (int item in ids) {

// #         int i = _bisectRight(item);

 

// #         if (i > 0) && (item <= ranges[i - 1][1]) {

// #             freshCount++;

// #         }

// #     }    

// # }

void day5() {
    const title = "Day 5: Cafeteria";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_5.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData.ranges, inputData.ids);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData.ranges);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
