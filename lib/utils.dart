extension StringX on String {
  String reversed() {
    return String.fromCharCodes(runes.toList().reversed);
  }
}