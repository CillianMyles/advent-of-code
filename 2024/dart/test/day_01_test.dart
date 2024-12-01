import 'dart:io';

import 'package:advent_of_code/day_01.dart';
import 'package:test/test.dart';

void main() {
  group('sumOfPairDistances', () {
    test('part 1 sample', () {
      expect(
        sumOfPairDistances(_sampleInputPart1),
        11,
      );
    });

    test('part 1 test', () {
      final input = File('lib/day_01.txt').readAsStringSync();
      expect(
        sumOfPairDistances(input),
        2756096,
      );
    });
  });
}

const _sampleInputPart1 = r'''
3   4
4   3
2   5
1   3
3   9
3   3
''';
