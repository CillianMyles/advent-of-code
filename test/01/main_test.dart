import 'package:advent_of_code/01/main.dart';
import 'package:test/test.dart';

const _input = '''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
''';

void main() {
  test('verify sample', () {
    expect(sumOfCalibrationValues(_input), 142);
  });
}
