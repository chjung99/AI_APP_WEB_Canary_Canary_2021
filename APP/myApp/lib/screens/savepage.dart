import 'dart:convert';
import 'dart:typed_data';
import 'package:image/image.dart' as ui;
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_progress_bar.dart';
import 'package:myapp/components/qrcode_maker.dart';
import 'package:myapp/screens/homepage.dart';
import 'package:image_gallery_saver/image_gallery_saver.dart';

class SavePage extends StatelessWidget {
  var value = Get.arguments;

  SavePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    String pre_img = value[0];
    String hashed_d_num = value[1];
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
                FutureBuilder(
                  future: qrwatermark(pre_img, hashed_d_num),
                  builder: (context, AsyncSnapshot<Uint8List> snapshot) {
                    return InkWell(
                      onLongPress: () {
                        showSaveDialog(context, snapshot.data!);
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
                        child: (snapshot.hasData)
                            ? Image.memory(
                                snapshot.data!,
                                fit: BoxFit.cover,
                              )
                            : Container(),
                      ),
                    );
                  },
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

  void showSaveDialog(BuildContext context, Uint8List imagebytes) {
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
            saveButton(context, imagebytes),
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

  TextButton saveButton(BuildContext context, Uint8List imagebytes) {
    return TextButton(
      onPressed: () async {
        Navigator.of(context).pop('yes');
        Get.snackbar("저장 완료", "이미지 저장이 완료되었습니다");
        await ImageGallerySaver.saveImage(imagebytes); //저장코드

        //https://pub.dev/packages/gallery_saver
      },
      child: const Text(
        'yes',
        style: TextStyle(color: Colors.black),
      ),
    );
  }

  Future<Uint8List> qrwatermark(String pre_img, String hashed_d_num) async {
    List<int> qrlist = await toQrImageData(hashed_d_num);

    ui.Image? originalImage = ui.decodeImage(base64Decode(pre_img));

    ui.Image? qrcodeImage = ui.decodeImage(qrlist);

    ui.Image image = ui.Image(50, 50);
    ui.drawImage(image, qrcodeImage!);
    ui.copyInto(
      originalImage!,
      image,
      /***/ dstX: originalImage.width - 50,
      /***/ dstY: originalImage.height - 50,
    );
    List<int> wmImage = ui.encodePng(originalImage);

    return Uint8List.fromList(wmImage);
  }
}
