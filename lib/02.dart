import 'dart:io';

import 'package:advent_of_code/utils.dart';

void main() {
  final input = File('lib/02.txt').readAsStringSync();
  final answer = part1(input);
  print(answer);
}

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

const _red = 12;
const _green = 13;
const _blue = 14;
