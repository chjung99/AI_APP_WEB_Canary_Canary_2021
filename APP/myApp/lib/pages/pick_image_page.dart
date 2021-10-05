import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:image_picker/image_picker.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/components/logo.dart';
import 'package:praticesig/components/progress_bar.dart';
import 'package:praticesig/domain/postImage/post.dart';

import 'package:praticesig/domain/postImage/post_repository.dart';
import 'package:praticesig/pages/resultpage.dart';

class PickImagePage extends StatefulWidget {
  const PickImagePage({Key? key}) : super(key: key);

  @override
  _PickImagePageState createState() => _PickImagePageState();
}

class _PickImagePageState extends State<PickImagePage> {
  // Widget createProgressBar() {
  //   return Row(
  //     mainAxisAlignment: MainAxisAlignment.center,
  //     children: [
  //       Container(
  //         alignment: Alignment.center,
  //         height: 20,
  //         width: 20,
  //         child: Text(
  //           "1",
  //           style: TextStyle(color: Colors.black),
  //         ),
  //         decoration: BoxDecoration(
  //           color: Colors.green,
  //           shape: BoxShape.circle,
  //         ),
  //       ),
  //       //Icon(Icons.ac_unit),
  //       Container(
  //         height: 5,
  //         width: 150,
  //         color: Colors.black,
  //       ),
  //       Icon(Icons.ac_unit),
  //       Container(
  //         height: 5,
  //         width: 150,
  //         color: Colors.black,
  //       ),
  //       Icon(Icons.ac_unit),
  //     ],
  //   );
  // }

  bool uploadImage = false;

  String text = "post server";
  XFile? _image;
  final ImagePicker _picker = ImagePicker();
  //dynamic _file;
  final PostRepository p = PostRepository();

  // 이미지 고르기
  Future _openImageFile() async {
    _image = await _picker.pickImage(source: ImageSource.gallery);
    setState(() {});
    uploadImage = true;
  }

  Future _openCameraFile() async {
    _image = await _picker.pickImage(source: ImageSource.camera);
    uploadImage = true;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xff6E9FED),
        title: Logo(
          image: "CANARY.png",
          width: 50,
          height: 50,
        ),
      ),
      body: Center(
        child: Column(
          children: [
            SizedBox(height: 20),
            createProgressBar(),
            // 이미지 화면에 표시
            SizedBox(height: 100),
            // 이미지 화면에 표시
            InkWell(
              onTap: () {
                _openImageFile();
              },
              child: Container(
                child: _image == null
                    ? Container(
                        width: 300,
                        height: 300,
                        decoration: const BoxDecoration(
                          color: Colors.grey,
                        ),
                        child: const Text(
                          '확인할 이미지를 선택해주세요',
                          textAlign: TextAlign.center,
                        ),
                      )
                    : Container(
                        width: 300,
                        height: 300,
                        decoration: const BoxDecoration(
                          color: Colors.transparent,
                        ),
                        child: Image(
                          image: ResizeImage(
                            NetworkImage(_image!.path),
                            width: 300,
                            height: 300,
                          ),
                          fit: BoxFit.cover,
                        ),
                      ),
              ),
            ),

            // 이미지 고르는 버튼
            TextButton(
              child: GradationButton(title: "Camera"),
              onPressed: () {
                _openCameraFile();
              },
            ),
            const SizedBox(height: 40),
            // 이미지를 서버로 보내는 버튼
            TextButton(
              child: GradationButton(title: "post server"),
              onPressed: () async {
                if (uploadImage) {
                  Post _imgId = await p.postImage(_image!);
                  print(_imgId);
                  String success = _imgId.imd_id;
                  print(_imgId.imd_id);
                  if (success.length > 0) {
                    print(success);
                    Get.to(() => ResultPage(), arguments: success);
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
}
