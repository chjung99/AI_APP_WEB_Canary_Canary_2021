import 'dart:async';
import 'package:flutter/material.dart';
import 'package:praticesig/color.dart';

class SplashPage extends StatefulWidget {
  const SplashPage({Key? key}) : super(key: key);

  @override
  _SplashPageState createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> {
  startTime() async {
    var _duration = new Duration(seconds: 4);
    return new Timer(_duration, navigationPage);
  }

  void navigationPage() {
    Navigator.of(context).pushReplacementNamed('/HomeScreen');
  }

  @override
  void initState() {
    super.initState();
    startTime();
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      backgroundColor: splashBackgroundColor,
      body: new Center(
        child: Container(
          child: new Image.asset(
            "assets/CANARYLOGO.jpg",
          ),
        ),
      ),
    );
  }
}
