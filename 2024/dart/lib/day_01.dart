import 'dart:io';

void main() {
  final input = File('lib/day_01.txt').readAsStringSync();
  final answer = sumOfPairDistances(input);
  print(answer);
}

int sumOfPairDistances(String input) {
  var sum = 0;
  final lines = input.split('\n');

  final lhs = <int>[];
  final rhs = <int>[];

  for (final line in lines) {
    if (line.isEmpty) continue;

    final split = line.split('   ');
    lhs.add(int.parse(split[0]));
    rhs.add(int.parse(split[1]));
  }

  lhs.sort((a, b) => a.compareTo(b));
  rhs.sort((a, b) => a.compareTo(b));

  for (int i = 0; i < lhs.length; i++) {
    sum += (lhs[i] - rhs[i]).abs();
  }

  return sum;
}
