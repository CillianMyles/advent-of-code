import 'dart:io';

void main() {
  final input = File('lib/day_02_test.txt').readAsStringSync();

  final safeReports = safeReportsCount(input);
  print('Safe Reports: $safeReports');

  final mostlySafeReports = mostlySafeReportsCount(input);
  print('Mostly Safe Reports: $mostlySafeReports');
}

/// Rules for a safe report:
/// * The levels are either all increasing or all decreasing.
/// * Any two adjacent levels differ by at least one and at most three.
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

/// Rules for a mostly safe report:
/// * The levels are either all increasing or all decreasing.
/// * Any two adjacent levels differ by at least one and at most three.
/// * If a report can be made safe by removing a single, then it is mostly safe.
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

    for (var j = 0; j < values.length; j++) {
      final variation = [
        for (var k = 0; k < values.length; k++)
          if (k != j) values[k]
      ];

      if (_isSafe(variation)) {
        count++;
        break;
      }
    }
  }

  return count;
}

enum _Order { unknown, ascending, descending }

bool _isSafe(List<int> values) {
  var order = _Order.unknown;

  for (var i = 0; i < values.length - 1; i++) {
    final current = values[i];
    final next = values[i + 1];

    if (order == _Order.unknown) {
      if (current == next) return false;
      if (current < next) {
        order = _Order.ascending;
      } else {
        order = _Order.descending;
      }
    }

    if (order == _Order.ascending) {
      final increasedBy = next - current;
      if (increasedBy < 1 || increasedBy > 3) return false;
    }

    if (order == _Order.descending) {
      final decreasedBy = current - next;
      if (decreasedBy < 1 || decreasedBy > 3) return false;
    }
  }

  return true;
}
