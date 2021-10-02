import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class GradationButton extends StatelessWidget {
  final String title;
  const GradationButton({required this.title});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.center,
      width: 400,
      height: 50,
      decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: <Color>[
              Color(0xFF0D47A1),
              Color(0xFF1976D2),
              Color(0xFF42A5F5),
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
