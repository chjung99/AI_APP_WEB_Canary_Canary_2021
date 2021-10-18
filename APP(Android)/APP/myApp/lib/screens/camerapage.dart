import 'dart:io';

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:image_picker/image_picker.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';

import 'package:myapp/components/custom_progress_bar.dart';
import 'package:myapp/domain/postImage/post.dart';

import 'package:myapp/domain/postImage/post_repository.dart';
import 'package:myapp/screens/loadingpage.dart';

class CameraPage extends StatefulWidget {
  const CameraPage({Key? key}) : super(key: key);

  @override
  _CameraPageState createState() => _CameraPageState();
}

class _CameraPageState extends State<CameraPage> {
  bool uploadImage = false;

  String text = "post server";
  String d_num = Get.arguments;
  XFile? _image;
  final ImagePicker _picker = ImagePicker();
  final PostRepository p = PostRepository();

  Future _openCameraFile() async {
    _image = await _picker.pickImage(source: ImageSource.camera);
    uploadImage = true;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Center(
        child: Column(
          children: [
            const SizedBox(height: 40),
            createProgressBar(false, false, false),
            const SizedBox(height: 30),
            InkWell(
              onTap: () {
                _openCameraFile();
              },
              child: (_image == null) ? noImageContainer() : imageContainer(),
            ),
            const SizedBox(height: 40),
            TextButton(
              child: const GradationButton(
                title: "post server",
                width: 300,
              ),
              onPressed: () async {
                if (uploadImage) {
                  Post _imgId = await p.postImage(_image!, d_num);
                  String success = _imgId.imd_id;
                  if (success.length > 0) {
                    Get.to(
                      () => LoadingPage(),
                      arguments: [success, d_num],
                      transition: Transition.rightToLeft,
                    );
                  }
                } else {
                  Get.snackbar("사진이 없습니다", "사진을 골라주세요!");
                }
              },
            ),
          ],
        ),
      ),
    );
  }

  Container imageContainer() {
    return Container(
      width: 300,
      height: 300,
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.black12,
          width: 2,
        ),
        color: Colors.transparent,
      ),
      child: Image.file(
        File(_image!.path),
        fit: BoxFit.cover,
      ),
      //
    );
  }

  Container noImageContainer() {
    return Container(
      width: 300,
      height: 300,
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.black12,
          width: 2,
        ),
        color: Colors.grey,
      ),
      child: const Text(
        '확인할 이미지를 선택해주세요',
        textAlign: TextAlign.center,
      ),
    );
  }
}

//  Image(
//                             image: ResizeImage(
//                               NetworkImage(_image!.path),
//                               width: 300,
//                               height: 300,
//                             ),
//                             fit: BoxFit.cover),