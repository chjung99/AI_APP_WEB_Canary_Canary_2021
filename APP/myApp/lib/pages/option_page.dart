import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/pages/camera_page.dart';
import 'package:praticesig/pages/gallery_page.dart';

class OptionPage extends StatelessWidget {
  const OptionPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: <Widget>[
            SizedBox(height: 120),
            Text(
              "Choose Image",
              style: TextStyle(
                fontSize: 40,
                color: Color(0xff6E9FED),
                fontWeight: FontWeight.bold,
                fontFamily: "BlackHanSans",
              ),
              textAlign: TextAlign.left,
            ),
            SizedBox(
              height: 5,
            ),
            Text("카메라와 갤러리 중 선택해주세요"),
            SizedBox(
              height: 70,
            ),
            Row(
              children: <Widget>[
                toGallery(),
                toCamera(),
              ],
            ),
          ],
        ),
      ),
    );
  }

  TextButton toGallery() {
    return TextButton(
      onPressed: () {
        Get.to(() => GalleryPage());
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

  TextButton toCamera() {
    return TextButton(
      onPressed: () {
        Get.to(() => CameraPage());
      },
      child: Container(
        width: 170,
        height: 170,
        child: Column(
          children: [
            Icon(Icons.photo_camera),
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
}
