import 'package:flutter/material.dart';

Text customText({required String text, required double size}) {
  return Text(
    text,
    style: TextStyle(
      fontSize: size,
      fontWeight: FontWeight.bold,
      color: Colors.indigo,
      fontFamily: "BlackHanSans",
    ),
  );
}
