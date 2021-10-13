import 'dart:convert';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_progress_bar.dart';
import 'package:myapp/components/custom_text.dart';
import 'package:myapp/domain/output/output.dart';
import 'package:myapp/domain/output/output_repository.dart';
import 'package:myapp/screens/resultpage.dart';
import 'package:myapp/size.dart';

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
          const SizedBox(height: 150),
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
                    child: const GradationButton(
                        title: "결과보러가기", width: 200, height: 200),
                  );
                } else {
                  return Column(
                    children: [
                      Image.asset(
                        "assets/Image/canaryloading.gif",
                        width: 300,
                        height: 300,
                        fit: BoxFit.cover,
                      ),
                      const SizedBox(height: 10),
                      loadingtext(),
                    ],
                  );
                }
              },
            ),
          ),
        ],
      ),
    );
  }

  DefaultTextStyle loadingtext() {
    return DefaultTextStyle(
      style: const TextStyle(
        fontSize: 20.0,
      ),
      child: AnimatedTextKit(
        animatedTexts: [
          WavyAnimatedText(
            "잠시만 기다려주세요...",
            textStyle: const TextStyle(
              color: Colors.black,
              fontFamily: 'Gugi',
            ),
            //CustomText(size: titleTextSize),
          ),
          WavyAnimatedText(
            '보완 테스트 중입니다...',
            textStyle: const TextStyle(
              color: Colors.black,
              fontFamily: 'Gugi',
            ),
            //CustomText(size: titleTextSize),
          ),
        ],
        isRepeatingAnimation: true,
      ),
    );
  }
}
