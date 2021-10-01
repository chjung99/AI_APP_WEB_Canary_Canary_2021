import 'package:flutter/material.dart';

class Logo extends StatelessWidget {
  final String image;
  final double width;
  final double height;

  const Logo(
      {Key? key,
      required this.image,
      required this.width,
      required this.height})
      : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Image.asset(
          "assets/$image",
          height: height,
          width: width,
          fit: BoxFit.cover,
        ),
      ],
    );
  }
}
