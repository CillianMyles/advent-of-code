import 'dart:io';

void main() {
  final input = File('lib/day_01.txt').readAsStringSync();

  final distances = sumOfPairDistances(input);
  print('distances: $distances');

  final similarity = getSimilarityScore(input);
  print('similarity: $similarity');
}

int sumOfPairDistances(String input) {
  var sum = 0;
  final (lhs, rhs) = _splitVertically(input);

  lhs.sort();
  rhs.sort();

  for (int i = 0; i < lhs.length; i++) {
    sum += (lhs[i] - rhs[i]).abs();
  }
  return sum;
}

int getSimilarityScore(String input) {
  var similarity = 0;
  final (lhs, rhs) = _splitVertically(input);

  for (var l in lhs) {
    var occurrences = 0;
    for (var r in rhs) {
      if (l == r) occurrences++;
    }
    similarity += l * occurrences;
  }
  return similarity;
}

(List<int> lhs, List<int> rhs) _splitVertically(String input) {
  final lhs = <int>[];
  final rhs = <int>[];

  for (final line in input.split('\n')) {
    if (line.isEmpty) break;

    final split = line.split('   ');
    lhs.add(int.parse(split[0]));
    rhs.add(int.parse(split[1]));
  }

  return (lhs, rhs);
}
