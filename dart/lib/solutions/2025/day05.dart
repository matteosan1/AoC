import 'dart:math';
import '../../../base/day.dart';

typedef LoadResult = ({List<List<int>> ranges, List<int> ids});

class Day05 extends Day {
  Day05() : super(2025, 5);

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

  @override
  LoadResult parserPart1(dynamic rawInput) {
    List<String> lines = rawInput;
    
    final ranges = <List<int>>[];
    final ids = <int>[];
    for (final line in lines) {
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
  
  // @override
  // List<int> parserPart2(dynamic rawInput) {
  //   List<String> lines = rawInput;
        
  //   final ids = <int>[];
  //   for (final line in lines) {
  //     if (line.trim().isEmpty) {
  //       continue;
  //     }

  //     if (!line.contains('-')) {        
  //       ids.add(int.parse(line.trim()));
  //     }
  //   }

  //   return ids;    
  // }

  @override
  Object? part1(covariant LoadResult input) {
    List<int> startPoints = input.ranges.map((r) => r[0]).toList();
    var fresh = 0;
    for (final item in input.ids) {
        int index = bisectRight(startPoints, item);
        if ((index > 0) && (item < input.ranges[index-1][1])) {
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
    return fresh;
  }


  @override
  Object? part2(covariant LoadResult input) {
    final freshIDs = input.ranges.map((range) => range[1] - range[0] + 1).fold<int>(0, (prev, element) => prev + element);
    return freshIDs;
  }
}
