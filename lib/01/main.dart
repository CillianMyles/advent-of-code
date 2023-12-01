import 'dart:io';

import 'package:advent_of_code/utils.dart';

void main() {
  final input = File('lib/01/input.txt').readAsStringSync();
  final answer = sumOfCalibrationValues(input);
  print(answer);
}

int sumOfCalibrationValues(String input) {
  final lines = input.split('\n');

  var sum = 0;
  for (final line in lines) {
    if (line.isEmpty) continue;

    final firstMatch =
        RegExp(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
            .firstMatch(line)!
            .group(0);

    final lastMatch =
        RegExp(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)')
            .firstMatch(line.reversed())!
            .group(0);

    final first = firstMatch!.length > 1 ? _wordLookup[firstMatch] : firstMatch;
    final last = lastMatch!.length > 1 ? _reversedLookup[lastMatch] : lastMatch;

    final value = int.parse('$first$last');
    sum += value;

    print('$line - $first - $last - $value');
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

const _reversedLookup = {
  'eno': '1',
  'owt': '2',
  'eerht': '3',
  'ruof': '4',
  'evif': '5',
  'xis': '6',
  'neves': '7',
  'thgie': '8',
  'enin': '9',
};
