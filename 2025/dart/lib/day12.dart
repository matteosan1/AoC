import 'dart:io';

import 'package:aoc_2025/aoc_2025.dart';

typedef PuzzleData = ({List<int> patterns, List<({int width, int height, List<int> counts})> regions});

PuzzleData parser(String content) {
    final sections = content.trim().split('\n\n');
    final regionSection = sections.last;
    final regions = <({int width, int height, List<int> counts})>[];

    for (final line in regionSection.split('\n')) {
        final trimmedLine = line.trim();
        if (trimmedLine.isEmpty || !trimmedLine.contains(':')) {
            continue;
        }

        final parts = trimmedLine.split(':');
        final areaPart = parts.first.trim();

        if (!areaPart.contains('x')) {
            continue;
        }

        final sizeParts = areaPart.split('x');
        final width = int.parse(sizeParts[0]);
        final height = int.parse(sizeParts[1]);

        final numsPart = parts.sublist(1).join(':').trim();
        final nums = numsPart.split(RegExp(r'\s+')).where((s) => s.isNotEmpty).map(int.parse).toList();

        regions.add((width: width, height: height, counts: nums));    
    }  

    final patterns = sections.take(sections.length - 1)
        .map((section) => section.split('\n').map((line) => line.trim().replaceAll(RegExp(r'[0-9:\.\s]'), '')).join())
        .map((cleanedSection) => cleanedSection.runes.where((char) => String.fromCharCode(char) == '#').length)
        .toList();

    return (patterns: patterns, regions: regions);
}

void part1(PuzzleData inputs) {    
    var filledRegions = 0;

    for (final region in inputs.regions) {
        final area = region.width * region.height;
        var size = 0;

        for (var i = 0; i < region.counts.length; i++) {
            if (i < inputs.patterns.length) {
                size += inputs.patterns[i] * region.counts[i];
            }
        }
   
        if (size <= area) {
            filledRegions++;
        }
    }

    stdout.write('🎄 Part 1: $filledRegions');
}

void day12() {
    const title = "Day 12: Christmas Tree Farm";
    final sub = "❄ " * (title.length ~/ 2 + 2);
    print('');
    print(' $title ');
    print(sub);

    final inputData = loadInput("input_12.txt", parser);
    final stopwatch = Stopwatch()..start();

    part1(inputData);
    stopwatch.stop();
    stdout.write(' - ${stopwatch.elapsedMicroseconds / 1000000} s\n');
}
