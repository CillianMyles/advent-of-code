import 'dart:io';

void main() {
  final input = File('lib/day_02_test.txt').readAsStringSync();

  final safeReports = safeReportsCount(input);
  print('Safe Reports: $safeReports');

  final mostlySafeReports = mostlySafeReportsCount(input);
  print('Mostly Safe Reports: $mostlySafeReports');
}

enum Order { unknown, ascending, descending }

int safeReportsCount(String input) {
  var count = 0;
  final lines = input.split('\n');

  for (var i = 0; i < lines.length; i++) {
    final line = lines[i].trim();
    if (line.isEmpty) break;

    final values = line.split(' ').map(int.parse).toList();
    if (_isSafe(values)) count++;
  }
  return count;
}

int mostlySafeReportsCount(String input) {
  var count = 0;
  final lines = input.split('\n');

  for (var i = 0; i < lines.length; i++) {
    final line = lines[i].trim();
    if (line.isEmpty) break;

    final values = line.split(' ').map(int.parse).toList();
    if (_isSafe(values)) {
      count++;
      continue;
    }

    for (var j = 0; j < values.length - 1; j++) {
      final alternative = [
        for (var k = 0; k < values.length; k++)
          if (k != j) values[k]
      ];

      if (_isSafe(alternative)) {
        count++;
        break;
      }
    }
  }

  return count;
}

bool _isSafe(List<int> values) {
  var order = Order.unknown;

  for (var i = 0; i < values.length - 1; i++) {
    final current = values[i];
    final next = values[i + 1];

    if (order == Order.unknown) {
      if (current == next) return false;
      if (current < next) {
        order = Order.ascending;
      } else {
        order = Order.descending;
      }
    }

    if (order == Order.ascending) {
      final increasedBy = next - current;
      if (increasedBy < 1 || increasedBy > 3) return false;
    }

    if (order == Order.descending) {
      final decreasedBy = current - next;
      if (decreasedBy < 1 || decreasedBy > 3) return false;
    }
  }

  return true;
}
