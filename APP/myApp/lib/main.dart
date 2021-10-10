import 'package:flutter/material.dart';
import 'package:praticesig/pages/homepage.dart';

import 'package:get/get.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const GetMaterialApp(
      debugShowCheckedModeBanner: false,
      // 라우트 설계 필요없음. GetX 사용 예정
      home: HomePage(),
    );
  }
}
