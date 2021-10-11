import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/custom_button.dart';
import 'package:praticesig/components/custom_progress_bar.dart';
import 'package:praticesig/domain/output/output.dart';
import 'package:praticesig/domain/output/output_repository.dart';
import 'package:praticesig/pages/savepage.dart';

class ResultPage extends StatefulWidget {
  @override
  _ResultPageState createState() => _ResultPageState();
}

class _ResultPageState extends State<ResultPage> {
  final OutputRepository o = OutputRepository();
  var value = Get.arguments;

  @override
  Widget build(BuildContext context) {
    var pre_img = value[0];
    var warning_text = value[1];

    return Scaffold(
      appBar: appbarmaker(),
      body: Column(
        children: [
          const SizedBox(height: 40),
          createProgressBar(true, false, false),
          const SizedBox(height: 30),
          Center(
            child: Column(
              children: [
                InkWell(
                  onTap: () {
                    showWarningDialog(context, warning_text);
                  },
                  child: Container(
                    width: 300,
                    height: 300,
                    child: Image.memory(
                      base64.decode(pre_img),
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                SizedBox(height: 20),
                TextButton(
                  child: const GradationButton(
                    title: "save",
                    width: 300,
                  ),
                  onPressed: () {
                    Get.to(() => SavePage(),
                        transition: Transition.rightToLeft);
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  void showWarningDialog(BuildContext context, String warning_text) {
    showDialog(
      context: context,
      //barrierDismissible - Dialog를 제외한 다른 화면 터치 x
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          // RoundedRectangleBorder - Dialog 화면 모서리 둥글게 조절
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
          //Dialog Main Title
          title: const Text('⚠ Warning ⚠'),
          content: Text(warning_text),
          //

          actions: <Widget>[
            TextButton(
              onPressed: () => Navigator.of(context).pop('알겠습니다!'),
              child: const Text(
                '알겠습니다!',
                style: TextStyle(color: Colors.red),
              ),
            )
          ],
        );
      },
    );
  }
}
