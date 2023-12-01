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

    final numbers = RegExp(r'\d|one|two|three|four|five|six|seven|eight|nine')
        .allMatches(line)
        .map((m) => m.group(0)!)
        .toList();

    final first =
        numbers.first.length > 1 ? _wordLookup[numbers.first] : numbers.first;
    final last =
        numbers.last.length > 1 ? _wordLookup[numbers.last] : numbers.last;

    final value = int.parse('$first$last');
    sum += value;

    print('$line - $numbers - $first - $last - $value');
  }

  return sum;
}

const _wordLookup = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
};
