import 'dart:io';

import 'package:advent_of_code/utils.dart';

void main() {
  final input = File('lib/day_02.txt').readAsStringSync();
  final answer1 = part1(input);
  final answer2 = part2(input);
  print('----------');
  print('Part 1: $answer1');
  print('Part 2: $answer2');
}

const _red = 12;
const _green = 13;
const _blue = 14;

/// Sum of the ids of all games that are possible.
int part1(String input) {
  final lines = input.split('\n');

  var sum = 0;
  for (final line in lines) {
    if (line.isEmpty) continue;

    final splitString = line.split(':');
    final gameString = splitString[0];
    final setsString = splitString[1].split(';');

    final id = RegExp(r'Game (\d+)').firstMatch(gameString)!.group(1)!.toInt();
    print('Game $id');

    var red = 0;
    var green = 0;
    var blue = 0;

    for (final setString in setsString) {
      print(' ${setString.trim()}');
      final valuesString = setString.split(',');

      for (final valueString in valuesString) {
        final match = RegExp(r'(\d+) (\w+)').firstMatch(valueString)!;
        final value = match.group(1)!.toInt();
        final color = match.group(2)!;

        switch (color) {
          case 'red':
            if (value > red) red = value;
          case 'green':
            if (value > green) green = value;
          case 'blue':
            if (value > blue) blue = value;
        }
      }
    }

    print('   MAX: $red red, $green green, $blue blue');
    if (red <= _red && green <= _green && blue <= _blue) {
      sum += id;
      print('    POSSIBLE: $sum');
    }
  }

  return sum;
}

/// Sum of powers of minimum sets of color values.
int part2(String input) {
  final lines = input.split('\n');

  var sum = 0;
  for (final line in lines) {
    if (line.isEmpty) continue;

    final splitString = line.split(':');
    final gameString = splitString[0];
    final setsString = splitString[1].split(';');

    final id = RegExp(r'Game (\d+)').firstMatch(gameString)!.group(1)!.toInt();
    print('Game $id');

    int? red;
    int? green;
    int? blue;

    for (final setString in setsString) {
      print(' ${setString.trim()}');
      final valuesString = setString.split(',');

      for (final valueString in valuesString) {
        final match = RegExp(r'(\d+) (\w+)').firstMatch(valueString)!;
        final value = match.group(1)!.toInt();
        final color = match.group(2)!;

        switch (color) {
          case 'red':
            if (red == null || value > red) red = value;
          case 'green':
            if (green == null || value > green) green = value;
          case 'blue':
            if (blue == null || value > blue) blue = value;
        }
      }
    }

    print('   MIN: $red red, $green green, $blue blue');
    final power = red! * green! * blue!;
    sum += power;
    print('    POWER: $power - SUM: $sum');
  }

  return sum;
}
