import 'package:flutter/material.dart';
import 'package:myapp/color.dart';

Text customText({required String text, required double size}) {
  return Text(
    text,
    style: TextStyle(
      fontSize: size,
      fontWeight: FontWeight.bold,
      color: primaryColor,
      fontFamily: "BlackHanSans",
    ),
  );
}
