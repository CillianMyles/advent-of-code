import 'dart:io';

void main() {
  final input = File('lib/day_02_test.txt').readAsStringSync();

  final safeReports = safeReportsCount(input);
  print('Safe Reports: $safeReports');

  final result2 = part2(input);
  print('Part 2: $result2');
}

int safeReportsCount(String input) {
  var count = 0;
  final lines = input.split('\n');
  print('lines: [len=${lines.length}]: $lines');

  bool? ascending;
  for (var i = 0; i < lines.length; i++) {
    final line = lines[i];
    if (line.trim().isEmpty) break;

    final values = line.split(' ');
    print('=' * 20);
    print('values: [i=$i]: [len=${values.length}]: $values');

    for (var j = 0; j < values.length - 1; j++) {
      final current = int.parse(values[j]);
      final next = int.parse(values[j + 1]);
      print('[j=$j]: current: $current, next: $next, ascending: $ascending');

      if (current == next) {
        print('break: current == next');
        ascending = null;
        break;
      }

      ascending ??= (next > current);

      if (ascending) {
        final increasedBy = next - current;
        if (increasedBy < 1 || increasedBy > 3) {
          print('break: increasedBy: $increasedBy');
          ascending = null;
          break;
        }
      }

      if (!ascending) {
        final decreasedBy = current - next;
        if (decreasedBy < 1 || decreasedBy > 3) {
          print('break: decreasedBy: $decreasedBy');
          ascending = null;
          break;
        }
      }

      if (j == values.length - 2) {
        count++;
        print(
            'safe: [i=$i]: [count=$count]: [${ascending ? 'asc' : 'desc'}]: $line');
        ascending = null;
        break;
      }
    }
  }

  return count;
}

int part2(String input) {
  return 0;
}
