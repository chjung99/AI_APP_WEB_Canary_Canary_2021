import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:image/image.dart' as ui;

class WaterMarkPage extends StatefulWidget {
  @override
  _WaterMarkPageState createState() => _WaterMarkPageState();
}

class _WaterMarkPageState extends State<WaterMarkPage> {
  var value = Get.arguments;
  dynamic _watermarkedImage;

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text("Watermark Example"),
        ),
        body: Center(
          child: Column(
            children: [
              watermarked(value),
            ],
          ),
        ),
      ),
    );
  }

  Image watermarked(dynamic value) {
    ui.Image? originalImage = ui.decodeImage(value);
    ui.Image? watermarkImage = ui.decodeImage(value);

    // add watermark over originalImage
    // initialize width and height of watermark image
    ui.Image image = ui.Image(160, 50);
    ui.drawImage(image, watermarkImage!);

    // give position to watermark over image
    // originalImage.width - 160 - 25 (width of originalImage - width of watermarkImage - extra margin you want to give)
    // originalImage.height - 50 - 25 (height of originalImage - height of watermarkImage - extra margin you want to give)
    ui.copyInto(originalImage!, image,
        dstX: originalImage.width - 160 - 25,
        dstY: originalImage.height - 50 - 25);

    // for adding text over image
    // Draw some text using 24pt arial font
    // 100 is position from x-axis, 120 is position from y-axis
    ui.drawString(originalImage, ui.arial_24, 100, 120, 'Think Different');

    // Store the watermarked image to a File
    List<int> wmImage = ui.encodePng(originalImage);

    return Image.memory(Uint8List.fromList(wmImage));
  }
}
