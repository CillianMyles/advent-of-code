import 'dart:io';

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

  final lines = input.split('\n');

  var sum = 0;
  for (int y = 0; y < lines.length; y++) {
    final line = lines[y];
    if (line.isEmpty) continue;

    var value = '';
    int start = 0;
    int end = line.length - 1;

    void reset() {
      value = '';
      start = 0;
      end = line.length - 1;
    }

    for (int x = 0; x < line.length; x++) {
      final char = line[x];

      if (x == 0) reset();

      void match() {
        print('$value [$y:$start-$end]');
        reset();
      }

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
  return 0;
}
