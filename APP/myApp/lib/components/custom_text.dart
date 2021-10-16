import 'package:flutter/material.dart';
import 'package:praticesig/color.dart';

TextStyle CustomText({required double size}) {
  return TextStyle(
    fontSize: size,
    fontWeight: FontWeight.bold,
    color: primaryColor,
    fontFamily: "BlackHanSans",
  );
}
