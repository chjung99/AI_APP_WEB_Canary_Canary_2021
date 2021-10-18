import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:myapp/color.dart';

class GradationButton extends StatelessWidget {
  final String title;
  final double width;
  final double height;
  const GradationButton(
      {required this.title, this.width = 400, this.height = 50});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.center,
      width: this.width,
      height: this.height,
      decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: <Color>[
              primaryColor,
              secondaryColor,
            ],
          ),
          borderRadius: BorderRadius.all(Radius.circular(20.0))),
      padding: const EdgeInsets.fromLTRB(20, 10, 20, 10),
      child: Text(
        title,
        style: const TextStyle(
          fontSize: 20,
          color: Colors.white,
        ),
      ),
    );
  }
}
