import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/custom_progress_bar.dart';
import 'package:praticesig/domain/output/output.dart';
import 'package:praticesig/domain/output/output_repository.dart';

class ResultPage extends StatefulWidget {
  @override
  _ResultPageState createState() => _ResultPageState();
}

class _ResultPageState extends State<ResultPage> {
  final OutputRepository o = OutputRepository();
  var value = Get.arguments;
  late Future<Output> outputImage;
  //late Future<Output> output;
  @override
  void initState() {
    super.initState();
    var host3 =
        "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/img/output-params/$value";
    outputImage = o.getImage(host3);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Column(
        children: [
          createProgressBar(true, false, false),
          const SizedBox(
            height: 100,
          ),
          Center(
            child: FutureBuilder<Output>(
              future: outputImage,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  //return Image.memory(base64.decode(snapshot.data!.output));
                  return Container(
                    width: 300,
                    height: 300,
                    child: Column(
                      children: [
                        Image.memory(
                          base64.decode(snapshot.data!.prc_img),
                        ),
                        SizedBox(height: 20),
                        Text(snapshot.data!.warning_text),
                      ],
                    ),
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
}