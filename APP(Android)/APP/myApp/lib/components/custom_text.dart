import 'package:flutter/material.dart';
import 'package:myapp/color.dart';

TextStyle CustomText({required double size}) {
  return TextStyle(
    fontSize: size,
    fontWeight: FontWeight.bold,
    color: primaryColor,
    fontFamily: "BlackHanSans",
  );
}
