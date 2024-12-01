import 'dart:io';

import 'package:advent_of_code/utils.dart';

void main() {
  final input = File('lib/day_03.txt').readAsStringSync();
  final answer1 = part1(input);
  final answer2 = part2(input);
  print('----------');
  print('Part 1: $answer1');
  print('Part 2: $answer2');
}

const _dot = '.';
const _star = '*';
const _numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

bool _isDot(String char) => char == _dot;

bool _isStar(String char) => char == _star;

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
      final adjacentSymbol = _enclosingBoxScan(
        lines: lines,
        y: y,
        x1: start,
        x2: end,
        matches: _isSymbol,
      );

      if (adjacentSymbol) sum += value.toInt();

      print('$value [$y:$start-$end] $adjacentSymbol');
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
      final adjacentSymbol = _enclosingBoxScan(
        lines: lines,
        y: y,
        x1: start,
        x2: end,
        matches: _isSymbol,
      );

      if (adjacentSymbol) sum += value.toInt();

      print('$value [$y:$start-$end] $adjacentSymbol');
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

bool _enclosingBoxScan({
  required List<String> lines,
  required int y,
  required int x1,
  required int x2,
  required bool Function(String char) matches,
}) {
  final line = lines[y];

  final hasRowAbove = y > 0;
  final hasRowBelow = y < lines.length - 1;
  final hasColumnLeft = x1 > 0;
  final hasColumnRight = x2 < line.length - 1;

  if (hasRowAbove) {
    final lineAbove = lines[y - 1];
    final lineSubstring = lineAbove.substring(
      hasColumnLeft ? x1 - 1 : x1,
      hasColumnRight ? x2 + 1 : x2,
    );
    final charsAbove = lineSubstring.chars();
    if (charsAbove.any(matches)) return true;
  }

  if (hasRowBelow) {
    final lineBelow = lines[y + 1];
    final lineSubstring = lineBelow.substring(
      hasColumnLeft ? x1 - 1 : x1,
      hasColumnRight ? x2 + 1 : x2,
    );
    final charsBelow = lineSubstring.chars();
    if (charsBelow.any(matches)) return true;
  }

  if (hasColumnLeft) {
    final char = line.substring(x1 - 1, x1);
    if (matches(char)) return true;
  }

  if (hasColumnRight) {
    final char = line.substring(x2, x2 + 1);
    if (matches(char)) return true;
  }

  return false;
}
