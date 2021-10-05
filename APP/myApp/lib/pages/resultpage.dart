import 'dart:convert';
import 'dart:html';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:get/get.dart';
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
  @override
  void initState() {
    super.initState();
    var host3 =
        "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/img/output-params/${value}";
    outputImage = o.getImage(host3);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Diet-ListView'),
      ),
      body: Center(
        child: FutureBuilder<Output>(
          future: outputImage,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Image.memory(base64.decode(snapshot.data!.output));
            } else {
              return const CircularProgressIndicator();
            }
          },
        ),
      ),
    );
  }
}