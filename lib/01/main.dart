import 'dart:io';

void main() {
  // read contents of file called input.txt in the current directory
  final input = File('lib/01/input.txt').readAsStringSync();
  final answer = sumOfCalibrationValues(input);
  print(answer);
}

int sumOfCalibrationValues(String input) {
  final lines = input.split('\n');

  var sum = 0;
  for (final line in lines) {
    if (line.isEmpty) continue;

    final numbers =
        RegExp(r'\d').allMatches(line).map((m) => m.group(0)!).toList();

    final value = int.parse('${numbers.first}${numbers.last}');
    sum += value;
  }

  return sum;
}
