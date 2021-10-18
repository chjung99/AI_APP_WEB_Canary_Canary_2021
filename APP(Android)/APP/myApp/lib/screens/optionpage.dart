import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_text.dart';
import 'package:myapp/screens/camerapage.dart';
import 'package:myapp/screens/gallerypage.dart';
import 'package:myapp/size.dart';

class OptionPage extends StatelessWidget {
  var d_num = Get.arguments;
  OptionPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Center(
          child: Column(
            children: <Widget>[
              const SizedBox(height: 120),
              Text(
                "Choose Image",
                style: CustomText(size: titleTextSize),
              ),
              const SizedBox(height: 5),
              const Text("카메라와 갤러리 중 선택해주세요"),
              const SizedBox(height: 70),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  toGallery(d_num),
                  toCamera(d_num),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  TextButton toGallery(String d_num) {
    return TextButton(
      onPressed: () {
        Get.to(
          () => GalleryPage(),
          arguments: d_num,
          transition: Transition.rightToLeft,
        );
      },
      child: Container(
        width: 170,
        height: 170,
        child: Column(
          children: [
            Icon(Icons.photo_library),
            GradationButton(
              title: "Gallery",
              width: 120,
              height: 120,
            ),
          ],
        ),
      ),
    );
  }

  TextButton toCamera(String d_num) {
    return TextButton(
      onPressed: () {
        Get.to(() => const CameraPage(),
            arguments: d_num, transition: Transition.rightToLeft);
      },
      child: Container(
        width: 170,
        height: 170,
        child: Column(
          children: [
            Icon(Icons.photo_camera),
            GradationButton(
              title: "Camera",
              width: 120,
              height: 120,
            ),
          ],
        ),
      ),
    );
  }
}
