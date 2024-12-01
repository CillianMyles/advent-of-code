import 'dart:io';

import 'package:advent_of_code/day_03.dart';
import 'package:test/test.dart';

void main() {
  group('part 1', () {
    test('sample', () {
      expect(
        part1(_sampleInput),
        4361,
      );
    });

    test('final test', () {
      final input = File('lib/day_03.txt').readAsStringSync();
      expect(
        part1(input),
        525911,
      );
    });
  });

  group('part 2', () {
    test('sample', () {
      expect(
        part2(_sampleInput),
        467835,
      );
    });

    test('final test', () {
      final input = File('lib/day_03.txt').readAsStringSync();
      expect(
        part2(input),
        42,
      );
    });
  });
}

const _sampleInput = r'''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
''';
