import 'dart:io';

import 'package:advent_of_code/day_01.dart';
import 'package:test/test.dart';

void main() {
  group('sumOfPairDistances', () {
    test('part 1 sample', () {
      expect(
        sumOfPairDistances(_sampleInput),
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

  group('getSimilarityScore', () {
    test('part 2 sample', () {
      expect(
        getSimilarityScore(_sampleInput),
        31,
      );
    });

    test('part 2 test', () {
      final input = File('lib/day_01.txt').readAsStringSync();
      expect(
        getSimilarityScore(input),
        23117829,
      );
    });
  });
}

const _sampleInput = r'''
3   4
4   3
2   5
1   3
3   9
3   3
''';
