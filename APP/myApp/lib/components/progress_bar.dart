import 'package:flutter/material.dart';

Widget createProgressBar() {
  return Row(
    mainAxisAlignment: MainAxisAlignment.center,
    children: [
      Icon(Icons.ac_unit),
      Container(
        height: 5,
        width: 150,
        color: Colors.black,
      ),
      Icon(Icons.ac_unit),
      Container(
        height: 5,
        width: 150,
        color: Colors.black,
      ),
      Icon(Icons.ac_unit),
    ],
  );
}
