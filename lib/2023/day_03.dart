import 'dart:io';

import 'package:advent_of_code/utils.dart';

void main() {
  final input = File('lib/2023/day_03.txt').readAsStringSync();
  final answer1 = part1(input);
  final answer2 = part2(input);
  print('----------');
  print('Part 1: $answer1');
  print('Part 2: $answer2');
}

const _dot = '.';
const _numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

bool _isDot(String char) => char == _dot;

bool _isNumber(String char) => _numbers.contains(char);

bool _isSymbol(String char) => !_isDot(char) && !_isNumber(char);

int part1(String input) {
  print(input);
  print('----------');

  final lines = input
      .split('\n')
      .where((line) => line.isNotEmpty)
      .toList(growable: false);

  var sum = 0;
  for (int y = 0; y < lines.length; y++) {
    final line = lines[y];

    var value = '';
    int start = 0;
    int end = line.length - 1;

    void reset() {
      value = '';
      start = 0;
      end = line.length - 1;
    }

    void match() {
      var match = false;

      final hasRowAbove = y > 0;
      final hasRowBelow = y < lines.length - 1;
      final hasColumnLeft = start > 0;
      final hasColumnRight = end < line.length - 1;

      if (hasRowAbove) {
        final lineAbove = lines[y - 1];
        final lineSubstring = lineAbove.substring(
          hasColumnLeft ? start - 1 : start,
          hasColumnRight ? end + 1 : end,
        );
        final charsAbove = lineSubstring.split('');
        if (charsAbove.any(_isSymbol)) match = true;
      }

      if (hasRowBelow) {
        final lineBelow = lines[y + 1];
        final lineSubstring = lineBelow.substring(
          hasColumnLeft ? start - 1 : start,
          hasColumnRight ? end + 1 : end,
        );
        final charsBelow = lineSubstring.split('');
        if (charsBelow.any(_isSymbol)) match = true;
      }

      if (hasColumnLeft) {
        final char = line.substring(start - 1, start);
        if (_isSymbol(char)) match = true;
      }

      if (hasColumnRight) {
        final char = line.substring(end, end + 1);
        if (_isSymbol(char)) match = true;
      }

      if (match) {
        sum += value.toInt();
      }

      print('$value [$y:$start-$end] $match');
      reset();
    }

    for (int x = 0; x < line.length; x++) {
      if (x == 0) reset();
      final char = line[x];

      if (_isNumber(char)) {
        if (value.isEmpty) start = x;
        value += char;
        if (x == line.length - 1) {
          end = x;
          match();
        }
      } else if (value.isNotEmpty) {
        end = x;
        match();
      }
    }
  }

  return sum;
}

int part2(String input) {
  print(input);
  print('----------');
  return 0;
}
