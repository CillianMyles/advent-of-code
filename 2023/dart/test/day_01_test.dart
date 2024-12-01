import 'dart:io';

import 'package:advent_of_code/day_01.dart';
import 'package:test/test.dart';

void main() {
  group('sumOfCalibrationValues', () {
    test('part 1 sample', () {
      expect(
        sumOfCalibrationValues(_sampleInputPart1),
        142,
      );
    });

    test('part 2 sample', () {
      expect(
        sumOfCalibrationValues(_sampleInputPart2),
        281,
      );
    });

    test('final test', () {
      final input = File('lib/day_01.txt').readAsStringSync();
      expect(
        sumOfCalibrationValues(input),
        54581,
      );
    });
  });
}

const _sampleInputPart1 = r'''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
''';

const _sampleInputPart2 = r'''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
''';
