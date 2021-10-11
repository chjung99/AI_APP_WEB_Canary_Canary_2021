import 'package:flutter/material.dart';
import 'package:myapp/screens/homepage.dart';

import 'package:get/get.dart';
import 'package:myapp/screens/splash_page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      debugShowCheckedModeBanner: false,
      // 라우트 설계 필요없음. GetX 사용 예정
      home: SplashPage(),
      routes: <String, WidgetBuilder>{
        '/HomeScreen': (BuildContext context) => HomePage()
      },
    );
  }
}
