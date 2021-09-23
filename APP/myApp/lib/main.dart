import 'package:flutter/material.dart';
import 'package:praticesig/pages/pick_image_page.dart';

import 'package:praticesig/pages/post_username_page.dart';
import 'package:get/get.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      debugShowCheckedModeBanner: false,
      // 라우트 설계 필요없음. GetX 사용 예정
      home: PostUserNamePage(),
    );
  }
}
