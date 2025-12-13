import 'dart:io';
import 'dart:math';

import 'package:aoc_2025/aoc_2025.dart';

List<Point> parser(List<String> contents) {
    final reds = <Point>[];
    for (final line in contents) {

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

void part1(List<Point> reds) {
    int maxArea = 0;
    for (final pair in combinations(reds)) {
        final a = area(pair.c1, pair.c2);
        maxArea = max(a, maxArea);
    }

    stdout.write("🎄 Part 1: $maxArea");
}

typedef EdgeBounds = ({int minX, int minY, int maxX, int maxY});

bool isFullyContained(List<EdgeBounds> edges, int minX, int minY, int maxX, int maxY) {
    for (final edge in edges) {
        if (minX < edge.maxX && maxX > edge.minX && minY < edge.maxY && maxY > edge.minY) {
            return false;
        }
    }
    return true;
}

void part2(List<Point> reds) {
    final edges = <EdgeBounds>[];
    final n = reds.length;

    for (int i = 0; i < n; i++) {
        final p1 = reds[i];
        final p2 = reds[(i + 1) % n]; // Wraps to the first point
        edges.add((
            minX: min(p1.x, p2.x),
            minY: min(p1.y, p2.y),
            maxX: max(p1.x, p2.x),
            maxY: max(p1.y, p2.y)
        ));
    }

    int maxArea = 0;
    for (final pair in combinations(reds)) {
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
    stdout.write("🎄🎅 Part 2: $maxArea");
}

void day9() {
    const title = "Day 9: Playground";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_9.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
