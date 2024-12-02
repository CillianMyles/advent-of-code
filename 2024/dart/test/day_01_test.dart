import 'dart:io';

import 'package:advent_of_code/day_01.dart';
import 'package:test/test.dart';

void main() {
  group('part 1 -> sumOfPairDistances', () {
    test('sample', () {
      final input = File('lib/day_01_sample.txt').readAsStringSync();
      expect(sumOfPairDistances(input), 11);
    });

    test('test', () {
      final input = File('lib/day_01_test.txt').readAsStringSync();
      expect(sumOfPairDistances(input), 2756096);
    });
  });

  group('part 2 -> getSimilarityScore', () {
    test('sample', () {
      final input = File('lib/day_01_sample.txt').readAsStringSync();
      expect(getSimilarityScore(input), 31);
    });

    test('test', () {
      final input = File('lib/day_01_test.txt').readAsStringSync();
      expect(getSimilarityScore(input), 23117829);
    });
  });
}
