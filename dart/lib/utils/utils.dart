extension PermutationsExt<T> on List<T> {
  Iterable<List<T>> permutations() sync* {
    final list = List<T>.of(this);
    final n = list.length;
    final c = List<int>.filled(n, 0);

    yield List<T>.unmodifiable(list);

    int i = 0;
    while (i < n) {
      if (c[i] < i) {
        final swapIdx = i.isEven ? 0 : c[i];
        final tmp = list[swapIdx];
        list[swapIdx] = list[i];
        list[i] = tmp;

        yield List<T>.unmodifiable(list);
        c[i]++;
        i = 0;
      } else {
        c[i] = 0;
        i++;
      }
    }
  }
}

extension AdjacentPairsExtension<T> on List<T> {
  Iterable<(T, T)> get adjacentPairs sync* {
    for (int i = 0; i < length - 1; i++) {
      yield (this[i], this[i + 1]);
    }
  }
}