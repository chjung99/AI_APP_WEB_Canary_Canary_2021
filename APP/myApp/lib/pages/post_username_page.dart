// UI 모음집 :  https://github.com/lohanidamodar/flutter_ui_challenges
// 애니메이션 : https://github.com/yumi0629/FlutterUI
import 'package:flutter/material.dart';
import 'package:praticesig/pages/pick_image_page.dart';
import 'package:praticesig/domain/post_repository.dart';
import 'package:get/get.dart';

class PostUserNamePage extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();
  final _username = TextEditingController();
  final PostRepository p = PostRepository();
  final _image = Image.asset('assets/nike.png');

  @override
  Widget build(BuildContext context) {
    ThemeData _theme = Theme.of(context);

    return Scaffold(
      //body나 scaffold 위젯이 높이가 정의된 스크린 키보드에 의해 스스로 크기를 재조정.
      resizeToAvoidBottomInset: true,
      //https://api.flutter.dev/flutter/material/Scaffold/extendBody.html
      extendBody: true,
      appBar: AppBar(),
      body: ListView(
        children: [
          Form(
            key: _formKey,
            child: TextFormField(
              controller: _username,
              style: _theme.inputDecorationTheme.labelStyle,
            ),
          ),
          TextButton(
            onPressed: () async {
              Get.to(() => PickImagePage());
              //await p.postUserInfo(_username.text, _image);
              await p.postUserName(_username.text);
            },
            child: Text("Clicked"),
          ),
        ],
      ),
    );
  }
}
