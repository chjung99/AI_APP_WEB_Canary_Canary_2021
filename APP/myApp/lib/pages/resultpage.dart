import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/progress_bar.dart';

class ResultPage extends StatelessWidget {
  var value = Get.arguments;
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Image.memory(value),
      //child: ProgressBar(),
    );
  }
}
