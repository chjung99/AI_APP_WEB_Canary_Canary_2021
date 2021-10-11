// import 'dart:typed_data';
// import 'package:flutter/material.dart';
// import 'package:get/get.dart';
// import 'package:image/image.dart' as ui;
// import 'package:praticesig/components/app_bar_maker.dart';

// class WaterMarkPage extends StatefulWidget {
//   @override
//   _WaterMarkPageState createState() => _WaterMarkPageState();
// }

// class _WaterMarkPageState extends State<WaterMarkPage> {
//   var value = Get.arguments;
//   dynamic _watermarkedImage;

//   @override
//   void initState() {
//     super.initState();
//   }

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       home: Scaffold(
//         appBar: appbarmaker(),
//         body: Center(
//           child: Column(
//             children: [
//               watermarked(value),
//             ],
//           ),
//         ),
//       ),
//     );
//   }

//   Image watermarked(dynamic value) {
//     ui.Image? originalImage = ui.decodeImage(value);
//     ui.Image? watermarkImage = ui.decodeImage(value);

//     // add watermark over originalImage
//     // initialize width and height of watermark image
//     ui.Image image = ui.Image(160, 50);
//     ui.drawImage(image, watermarkImage!);

//     // give position to watermark over image
//     // originalImage.width - 160 - 25 (width of originalImage - width of watermarkImage - extra margin you want to give)
//     // originalImage.height - 50 - 25 (height of originalImage - height of watermarkImage - extra margin you want to give)
//     ui.copyInto(originalImage!, image,
//         dstX: originalImage.width - 160 - 25,
//         dstY: originalImage.height - 50 - 25);

//     // for adding text over image
//     // Draw some text using 24pt arial font
//     // 100 is position from x-axis, 120 is position from y-axis
//     ui.drawString(originalImage, ui.arial_24, 100, 120, 'Think Different');

//     // Store the watermarked image to a File
//     List<int> wmImage = ui.encodePng(originalImage);

//     return Image.memory(Uint8List.fromList(wmImage));
//   }
// }

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_progress_bar.dart';
import 'package:myapp/screens/homepage.dart';

class SavePage extends StatelessWidget {
  const SavePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Column(
        children: [
          const SizedBox(height: 40),
          createProgressBar(true, true, false),
          const SizedBox(height: 30),
          Center(
            child: Column(
              children: [
                InkWell(
                  onLongPress: () {
                    showSaveDialog(context);
                  },
                  child: Container(
                    width: 300,
                    height: 300,
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: Colors.black12,
                        width: 2,
                      ),
                    ),
                    child: Image.asset(
                      "assets/CANARY.png",
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                const SizedBox(height: 20),
                TextButton(
                  child: const GradationButton(
                    title: "Try Again",
                    width: 300,
                  ),
                  onPressed: () {
                    Get.to(() => const HomePage(),
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

  void showSaveDialog(BuildContext context) {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
          title: const Text('이미지 저장'),
          content: const Text("이미지를 저장하시겠습니까"),
          actions: <Widget>[
            saveButton(context),
            notSaveButton(context),
          ],
        );
      },
    );
  }

  TextButton notSaveButton(BuildContext context) {
    return TextButton(
      onPressed: () {
        Navigator.of(context).pop('no');
      },
      child: const Text(
        'no',
        style: TextStyle(color: Colors.black),
      ),
    );
  }

  TextButton saveButton(BuildContext context) {
    return TextButton(
      onPressed: () {
        Navigator.of(context).pop('yes');
        Get.snackbar("저장 완료", "이미지 저장이 완료되었습니다");
        //GallerySaver.saveImage("path");
        //https://pub.dev/packages/gallery_saver
      },
      child: const Text(
        'yes',
        style: TextStyle(color: Colors.black),
      ),
    );
  }
}
