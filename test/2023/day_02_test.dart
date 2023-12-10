import 'dart:io';

import 'package:advent_of_code/2023/day_02.dart';
import 'package:test/test.dart';

void main() {
  group('part 1', () {
    test('sample', () {
      expect(
        part1(_sampleInput),
        8,
      );
    });

    test('final test', () {
      final input = File('lib/2023/day_02.txt').readAsStringSync();
      expect(
        part1(input),
        2879,
      );
    });
  });

  group('part 2', () {
    test('sample', () {
      expect(
        part2(_sampleInput),
        2286,
      );
    });

    test('final test', () {
      final input = File('lib/2023/day_02.txt').readAsStringSync();
      expect(
        part2(input),
        65122,
      );
    });
  });
}

const _sampleInput = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
''';
