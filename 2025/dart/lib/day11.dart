import 'dart:io';
import 'dart:collection';

import 'package:aoc_2025/aoc_2025.dart';

typedef Graph = Map<String, List<String>>;

Graph parser(List<String> contents) {
    final nodes = Graph();

    for (final line in contents) {
        if (line.trim().isEmpty) continue;
        final parts = line.split(":");
        if (parts.length < 2) continue;
        final source = parts[0].trim();
        final destinations = parts[1].trim().split(RegExp(r'\s+'));
        nodes[source] = destinations;
    }
    return nodes;
} 

// List<List<String>> dfs(Graph nodes, {String start = "you", String end = "out"}) {
//      final allPaths = <List<String>>[];
//     void dfsHelper(String currentNode, List<String> currentPath) {
//      final newPath = List<String>.from(currentPath)..add(currentNode);   
//      if (currentNode == end) {
//              allPaths.add(newPath);
//              return;
//      }
//      if (nodes.containsKey(currentNode)) {
//              for (final neighbor in nodes[currentNode]!) {
//              if (!newPath.contains(neighbor)) {
//                      dfsHelper(neighbor, newPath);
//              }
//              }
//      }
//      }
//      dfsHelper(start, []);
//      return allPaths;
// }

typedef MemoKey = ({String start, String end});
typedef MemoTable = HashMap<MemoKey, int>;

int dfsMemoized(Graph graph, String startNode, String endNode, MemoTable memo) {
    final memoKey = (start: startNode, end: endNode);

    if (memo.containsKey(memoKey)) {
        return memo[memoKey]!;
    }  

    if (startNode == endNode) {
        return 1;
    }

    if (!graph.containsKey(startNode)) {
        return 0;
    }

    int count = 0;
    for (final neighbor in graph[startNode]!) {
        count += dfsMemoized(graph, neighbor, endNode, memo);
    }

    memo[memoKey] = count;
    return count;
}

void part1(Graph nodes) {
    final memo = MemoTable();
    final paths = dfsMemoized(nodes, "you", "out", memo);
    stdout.write("🎄 Part 1: $paths");
}
 
void part2(Graph nodes) {
    final memo = MemoTable();

    final PsrToDac = dfsMemoized(nodes, "svr", "dac", memo);
    final PdacToFft = dfsMemoized(nodes, "dac", "fft", memo);
    final PfftToDac = dfsMemoized(nodes, "fft", "dac", memo);
    final PdacToOut = dfsMemoized(nodes, "dac", "out", memo);
    final PsrToFft = dfsMemoized(nodes, "svr", "fft", memo);
    final PfftToOut = dfsMemoized(nodes, "fft", "out", memo);

    final totalPaths = (PsrToDac * PdacToFft * PfftToOut) + (PsrToFft * PfftToDac * PdacToOut);
    stdout.write("🎄🎅 Part 2: $totalPaths");
}

void day11() {
    const title = "Day 11: Reactor";
    final sub = "❄ " * (title.length ~/ 2 + 2);

    print('');
    print(' $title ');
    print(sub);
  
    final inputData = loadMultiLines("input_11.txt", parser);

    final stopwatch1 = Stopwatch()..start();
    part1(inputData);
    stopwatch1.stop();
    stdout.write(' - ${stopwatch1.elapsedMicroseconds / 1000000} s\n');
  
    final stopwatch2 = Stopwatch()..start();
    part2(inputData);
    stopwatch2.stop();
    stdout.write(' - ${stopwatch2.elapsedMicroseconds / 1000000} s\n');
}
