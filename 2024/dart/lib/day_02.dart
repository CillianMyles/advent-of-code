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

const _maxOutliers = 1;

int mostlySafeReportsCount(String input) {
  var count = 0;
  final lines = input.split('\n');

  for (var i = 0; i < lines.length; i++) {
    final line = lines[i];
    if (line.trim().isEmpty) break;

    var order = Order.unknown;
    var outliers = 0;
    final values = line.split(' ');
    print('=' * 20);
    print('values: [i=$i]: [len=${values.length}]: $values');

    for (var j = 0; j < values.length - 1; j++) {
      final current = int.parse(values[j]);
      final next = int.parse(values[j + 1]);
      print(
        '[j=$j]: current: $current, next: $next, order: ${order.name}, outliers: $outliers',
      );

      if (order == Order.unknown) {
        if (current == next) {
          if (outliers < _maxOutliers) {
            print('outliers++');
            outliers++;
            continue;
          } else {
            print('break: current == next');
            order = Order.unknown;
            outliers = 0;
            break;
          }
        } else if (current < next) {
          order = Order.ascending;
        } else {
          order = Order.descending;
        }
      }

      if (order == Order.ascending) {
        final increasedBy = next - current;
        if (increasedBy < 1 || increasedBy > 3) {
          if (outliers < _maxOutliers) {
            print('outliers++');
            outliers++;
            continue;
          } else {
            print('break: increasedBy: $increasedBy');
            order = Order.unknown;
            outliers = 0;
            break;
          }
        }
      }

      if (order == Order.descending) {
        final decreasedBy = current - next;
        if (decreasedBy < 1 || decreasedBy > 3) {
          if (outliers < _maxOutliers) {
            print('outliers++');
            outliers++;
            continue;
          } else {
            print('break: decreasedBy: $decreasedBy');
            order = Order.unknown;
            outliers = 0;
            break;
          }
        }
      }

      if (j == values.length - 2) {
        count++;
        print('safe: [i=$i]: [count=$count]: [${order.name}]: $line');
        order = Order.unknown;
        outliers = 0;
        break;
      }
    }
  }

  return count;
}
