import 'dart:convert';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/custom_button.dart';
import 'package:praticesig/components/custom_progress_bar.dart';
import 'package:praticesig/domain/output/output.dart';
import 'package:praticesig/domain/output/output_repository.dart';
import 'package:praticesig/pages/resultpage.dart';

class LoadingPage extends StatefulWidget {
  const LoadingPage({Key? key}) : super(key: key);

  @override
  _LoadingPageState createState() => _LoadingPageState();
}

class _LoadingPageState extends State<LoadingPage> {
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
          const SizedBox(height: 70),
          Center(
            child: FutureBuilder<Output>(
              future: outputImage,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return TextButton(
                    onPressed: () {
                      Get.to(
                        () => ResultPage(),
                        arguments: [
                          snapshot.data!.prc_img,
                          snapshot.data!.warning_text,
                        ],
                      );
                    },
                    child: Text("hello"),
                  );
                } else {
                  return DefaultTextStyle(
                    style: const TextStyle(
                      fontSize: 20.0,
                    ),
                    child: AnimatedTextKit(
                      animatedTexts: [
                        WavyAnimatedText('Hello World'),
                        WavyAnimatedText('Look at the waves'),
                      ],
                      isRepeatingAnimation: true,
                      onTap: () {
                        print("Tap Event");
                      },
                    ),
                  );
                }
              },
            ),
          ),
        ],
      ),
    );
  }
}
