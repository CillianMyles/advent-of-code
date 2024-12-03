import 'dart:io';

void main() {
  final input = File('lib/day_02_test.txt').readAsStringSync();

  final safeReports = safeReportsCount(input);
  print('Safe Reports: $safeReports');

  final result2 = part2(input);
  print('Part 2: $result2');
}

enum Order { unknown, ascending, descending }

int safeReportsCount(String input) {
  var count = 0;
  final lines = input.split('\n');

  for (var i = 0; i < lines.length; i++) {
    final line = lines[i];
    if (line.trim().isEmpty) break;

    var order = Order.unknown;
    final values = line.split(' ');

    for (var j = 0; j < values.length - 1; j++) {
      final current = int.parse(values[j]);
      final next = int.parse(values[j + 1]);

      if (order == Order.unknown) {
        if (current == next) {
          order = Order.unknown;
          break;
        } else if (current < next) {
          order = Order.ascending;
        } else {
          order = Order.descending;
        }
      }

      if (order == Order.ascending) {
        final increasedBy = next - current;
        if (increasedBy < 1 || increasedBy > 3) {
          order = Order.unknown;
          break;
        }
      }

      if (order == Order.descending) {
        final decreasedBy = current - next;
        if (decreasedBy < 1 || decreasedBy > 3) {
          order = Order.unknown;
          break;
        }
      }

      if (j == values.length - 2) {
        count++;
        order = Order.unknown;
        break;
      }
    }
  }

  return count;
}

int part2(String input) {
  return 0;
}
