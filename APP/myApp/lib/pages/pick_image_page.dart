/*
import 'dart:convert';
import 'dart:html';
import 'dart:typed_data';
import 'package:file_picker/file_picker.dart';
*/
import 'dart:html';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:praticesig/domain/post_provider.dart';
import 'package:praticesig/domain/post_repository.dart';

class PickImagePage extends StatefulWidget {
  const PickImagePage({Key? key}) : super(key: key);

  @override
  _PickImagePageState createState() => _PickImagePageState();
}

class _PickImagePageState extends State<PickImagePage> {
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
    return Column(
      children: [
        // 이미지 화면에 표시
        Center(
          child:
              // Image.file(File(image!.path)); : 이미지 로컬 저장소 아마 이걸 써야 될 거 같긴함
              _image == null ? Text('no Image') : Image.network(_image!.path),
        ),
        // 이미지 고르는 버튼
        TextButton(
          onPressed: () {
            _openImageFile();
          },
          child: Text("clicked to choose Image"),
        ),

        // 이미지를 서버로 보내는 버튼
        TextButton(
          onPressed: () async {
            await p.postImage(_image!);
          },
          child: Text("post server"),
        ),
      ],
    );
  }
}
