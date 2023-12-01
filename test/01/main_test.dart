import 'package:advent_of_code/01/main.dart';
import 'package:test/test.dart';

void main() {
  group('verify samples', () {
    test('part 1', () {
      expect(
        sumOfCalibrationValues(_inputPart1),
        142,
      );
    });

    test('part 2', () {
      expect(
        sumOfCalibrationValues(_inputPart2),
        281,
      );
    });
  });
}

const _inputPart1 = '''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
''';

const _inputPart2 = '''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
''';
