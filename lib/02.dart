import 'dart:io';

void main() {
  final input = File('lib/02.txt').readAsStringSync();
  final answer = sumOfIdsOfPossibleGames(input);
  print(answer);
}

int sumOfIdsOfPossibleGames(String input) {
  return 42;
}
