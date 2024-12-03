import 'dart:io';

import 'package:advent_of_code/day_02.dart';
import 'package:test/test.dart';

void main() {
  group('part 1 -> safeReportsCount', () {
    test('sample', () {
      final input = File('lib/day_02_sample.txt').readAsStringSync();
      expect(safeReportsCount(input), 2);
    });

    test('test', () {
      final input = File('lib/day_02_test.txt').readAsStringSync();
      expect(safeReportsCount(input), 218);
    });
  });

  group('part 2 -> ...', () {
    test('sample', () {
      final input = File('lib/day_02_sample.txt').readAsStringSync();
      expect(safeReportsCount(input), -1);
    });

    test('test', () {
      final input = File('lib/day_02_test.txt').readAsStringSync();
      expect(safeReportsCount(input), -1);
    });
  });
}
