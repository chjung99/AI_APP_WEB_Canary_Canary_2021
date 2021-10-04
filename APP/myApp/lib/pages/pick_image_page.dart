import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:image_picker/image_picker.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/components/logo.dart';

import 'package:praticesig/domain/postImage/post_repository.dart';
import 'package:praticesig/pages/resultpage.dart';

class PickImagePage extends StatefulWidget {
  const PickImagePage({Key? key}) : super(key: key);

  @override
  _PickImagePageState createState() => _PickImagePageState();
}

class _PickImagePageState extends State<PickImagePage> {
  String text = "post server";
  XFile? _image;
  final ImagePicker _picker = ImagePicker();
  //dynamic _file;
  final PostRepository p = PostRepository();

  // 이미지 고르기
  Future _openImageFile() async {
    _image = await _picker.pickImage(source: ImageSource.gallery);
    setState(() {});
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
            //createProgressBar(),
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

            const SizedBox(height: 40),
            // 이미지를 서버로 보내는 버튼
            TextButton(
              child: GradationButton(title: "post server"),
              onPressed: () async {
                await p.postImage(_image!);
                Get.to(() => ResultPage());
                //Map data = await p.postImage(_image!);
                //data["convertBody"]가 base64이면 무조건 돌아간다!
                //Get.to(() => ResultPage(), arguments: data["convertBody"]);
              },
            ),
          ],
        ),
      ),
    );
  }
}
