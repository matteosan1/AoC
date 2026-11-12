import 'dart:math';
import '../../../base/day.dart';

typedef LoadResult = ({int action, (int, int) start, (int, int) end});

class Day06 extends Day {
  Day06() : super(2015, 6);

  @override
  List<LoadResult> parser(dynamic rawInput) {
    List<LoadResult> res = [];
    
    for (var line in rawInput) {
      final parts = line.split(' ');
      
      if (line.startsWith('turn off')) {
        final [startX, startY] = parts[2].split(',').map(int.parse).toList();
        final [endX, endY] = parts[4].split(',').map(int.parse).toList();
        res.add((action: -1, start: (startX, startY), end: (endX, endY)));
        
      } else if (line.startsWith('turn on')) {
        final [startX, startY] = parts[2].split(',').map(int.parse).toList();
        final [endX, endY] = parts[4].split(',').map(int.parse).toList();
        res.add((action: 1, start: (startX, startY), end: (endX, endY)));
        
      } else if (line.startsWith('toggle')) {
        final [startX, startY] = parts[1].split(',').map(int.parse).toList();
        final [endX, endY] = parts[3].split(',').map(int.parse).toList();
        res.add((action: 2, start: (startX, startY), end: (endX, endY)));
      }
    }

    return res;
  }

  void actLight(LoadResult res, List<List<int>> field) {
    for (int x=res.start.$1; x<=res.end.$1; x++) {
      for (int y=res.start.$2; y<=res.end.$2; y++) {
        if (res.action == -1) {
          field[x][y] = 0;
        } else if (res.action == 1) {
          field[x][y] = 1;
        } else {
          field[x][y] = 1-field[x][y];
        }
      }
    }
  }

  int lightOn(List<List<int>> field) {
    int totalSum = 0;
    for (var row in field) {
      for (var val in row) {
        totalSum += val;
      }
    }
    return totalSum;
  }

  @override
  Object? part1(covariant List<LoadResult> input) {
    List<List<int>> field = List.generate(1000, (_) => List.filled(1000, 0),);
    for (var action in input) {
      actLight(action, field);
    }

    return lightOn(field);
  }

  void actLightPart2(LoadResult res, List<List<int>> field) {
    for (int x=res.start.$1; x<=res.end.$1; x++) {
      for (int y=res.start.$2; y<=res.end.$2; y++) {
        field[x][y] += res.action;
        field[x][y] = max(0, field[x][y]);
      }
    }
  }

  @override
  Object? part2(covariant List<LoadResult> input) {
    List<List<int>> field = List.generate(1000, (_) => List.filled(1000, 0),);
    for (var action in input) {
      actLightPart2(action, field);
    }

    return lightOn(field);
  }
}
