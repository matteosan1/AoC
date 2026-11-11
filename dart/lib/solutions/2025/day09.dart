import 'dart:math';
import '../../../base/day.dart';
import '../../utils/geometry.dart';

typedef EdgeBounds = ({int minX, int minY, int maxX, int maxY});

class Day09 extends Day {
  Day09() : super(2025, 9);

  @override
  List<Point> parser(dynamic rawInput) {
    final reds = <Point>[];
    for (final line in rawInput) {

        if (line.trim().isEmpty) continue;
        final parts = line.split(',').map((s) => int.parse(s.trim())).toList();
        reds.add(Point(parts[0], parts[1]));      
    }
    return reds;
  }

  int area(Point p1, Point p2) {
    return ((p1.x - p2.x).abs() + 1) * ((p1.y - p2.y).abs() + 1);
  }

  Iterable<({Point c1, Point c2})> combinations(List<Point> list) sync* {
    for (int i = 0; i < list.length; i++) {
        for (int j = i + 1; j < list.length; j++) {
            yield (c1: list[i], c2: list[j]);
        }
    }
  }

  @override
  Object? part1(covariant List<Point> input) {
    int maxArea = 0;
    for (final pair in combinations(input)) {
      final a = area(pair.c1, pair.c2);
      maxArea = max(a, maxArea);
    }

    return maxArea;
  }

  bool isFullyContained(List<EdgeBounds> edges, int minX, int minY, int maxX, int maxY) {
    for (final edge in edges) {
        if (minX < edge.maxX && maxX > edge.minX && minY < edge.maxY && maxY > edge.minY) {
            return false;
        }
    }
    return true;
  }

  @override
  Object? part2(covariant List<Point> input) {
    final edges = <EdgeBounds>[];
    final n = input.length;

    for (int i = 0; i < n; i++) {
        final p1 = input[i];
        final p2 = input[(i + 1) % n]; // Wraps to the first point
        edges.add((
            minX: min(p1.x, p2.x),
            minY: min(p1.y, p2.y),
            maxX: max(p1.x, p2.x),
            maxY: max(p1.y, p2.y)
        ));
    }

    int maxArea = 0;
    for (final pair in combinations(input)) {
        final p1 = pair.c1;
        final p2 = pair.c2;
        final a = area(p1, p2);

        if (a > maxArea) {
            final minX = min(p1.x, p2.x);
            final maxX = max(p1.x, p2.x);
            final minY = min(p1.y, p2.y);
            final maxY = max(p1.y, p2.y);

            if (isFullyContained(edges, minX, minY, maxX, maxY)) {
                maxArea = a;
            }
        }
    }
    return maxArea;
  }
}
