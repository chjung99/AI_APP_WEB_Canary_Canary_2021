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
  late Future<Output> outputImage;

  @override
  void initState() {
    super.initState();
    var host3 =
        "https://osam-project-testing-tkqtg.run.goorm.io/img/output-params/$value";

    outputImage = o.getImage(host3);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Column(
        children: [
          const SizedBox(height: 40),
          createProgressBar(true, false, false),
          const SizedBox(height: 30),
          Center(
            child: FutureBuilder<Output>(
              future: outputImage,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  showWarningDialog(context, snapshot);
                  return Column(
                    children: [
                      Container(
                        width: 300,
                        height: 300,
                        child: Image.memory(
                          base64.decode(snapshot.data!.prc_img),
                          fit: BoxFit.cover,
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
                  );
                } else {
                  return const CircularProgressIndicator();
                }
              },
            ),
          ),
        ],
      ),
    );
  }

  Future<void> showWarningDialog(
      BuildContext context, AsyncSnapshot<Output> snapshot) {
    return Future(
      () {
        // Future Callback
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: const Text('⚠ Warning ⚠'),
            content: Text(snapshot.data!.warning_text),
            actions: <Widget>[
              TextButton(
                onPressed: () => Navigator.of(context).pop('알겠습니다!'),
                child: const Text(
                  '알겠습니다!',
                  style: TextStyle(color: Colors.red),
                ),
              )
            ],
          ),
        );
      },
    );
  }
}
