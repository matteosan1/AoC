import '../../../base/day.dart';

typedef Instruction = ({String op, String left, String? right});

extension InstructionExt on Instruction {
  int eval(Map<String, Instruction> circuit, Map<String, int> cache) {
    int resolve(String token) {
      final literal = int.tryParse(token);
      if (literal != null) return literal;
      return cache.putIfAbsent(token, () => circuit[token]!.eval(circuit, cache));
    }

    final result = switch(op) {
      'ASSIGN' => resolve(left),
      'NOT'    => ~resolve(left),
      'AND'    => resolve(left) & resolve(right!),
      'OR'     => resolve(left) | resolve(right!),
      'LSHIFT' => resolve(left) << resolve(right!),
      'RSHIFT' => resolve(left) >> resolve(right!),
      _        => throw StateError('Operatore sconosciuto: $op'),
    };

    return result & 0xFFFF;
  }
}

class Day07 extends Day {
  Day07() : super(2015, 7);

  @override
  Map<String, Instruction> parser(dynamic rawInput) {
    Map<String, Instruction> circuit = {};

    for (var line in rawInput) {
      final [expr, target] = line.split(' -> ');
      final tokens = expr.split(' ');

      final Instruction i = switch (tokens) {
        [var src] => (op: 'ASSIGN', left: src, right: null),
        ['NOT', var src] => (op: 'NOT', left: src, right: null),
        [var l, var op, var r] => (op: op, left: l, right: r),
        _  => throw FormatException('Riga non valida: $line'),
      };
      circuit[target] = i;
    }
    return circuit;
  }

  @override
  Object? part1(covariant Map<String, Instruction> input) {
    Map<String, int> cache = {};
    final result = input['a']!.eval(input, cache);
    part1Result = result;
    return result;
  }

  @override
  Object? part2(covariant Map<String, Instruction> input) {
    final Map<String, int> cache = {'b': part1Result as int};
    return input['a']!.eval(input, cache);
  }
}
