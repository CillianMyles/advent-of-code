import 'dart:io';

import 'package:advent_of_code/utils.dart';

void main() {
  final input = File('lib/02.txt').readAsStringSync();
  final answer = sumOfIdsOfPossibleGames(input);
  print(answer);
}

int sumOfIdsOfPossibleGames(String input) {
  final lines = input.split('\n').where((line) => line.isNotEmpty);

  var sum = 0;
  for (final line in lines) {
    final splitString = line.split(':');
    final gameString = splitString[0];
    final setsString = splitString[1].split(';');

    final id = RegExp(r'Game (\d+)').firstMatch(gameString)!.group(1)!.toInt();

    for (final setString in setsString) {
      print(' ${setString.trim()}');
      final valuesString = setString.split(',');

      var red = 0;
      var green = 0;
      var blue = 0;

      for (final valueString in valuesString) {
        final match = RegExp(r'(\d+) (\w+)').firstMatch(valueString)!;
        final value = int.parse(match.group(1)!);
        final color = match.group(2)!;

        switch (match.group(2)) {
          case 'red':
            if (value > red) red = value;
          case 'green':
            if (value > green) green = value;
          case 'blue':
            if (value > blue) blue = value;
        }
        print('  $value $color');
      }

      sum += _Game(id: id, red: red, green: green, blue: blue).id;
    }
  }

  return 42;
}

class _Game {
  const _Game({
    required this.id,
    this.red = 0,
    this.green = 0,
    this.blue = 0,
  });

  final int id;
  final int red;
  final int green;
  final int blue;
}
