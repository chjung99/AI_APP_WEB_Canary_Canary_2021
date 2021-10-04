// UI 모음집 :  https://github.com/lohanidamodar/flutter_ui_challenges
// 애니메이션 : https://github.com/yumi0629/FlutterUI
import 'package:flutter/material.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/components/custom_text_form_field.dart';

import 'package:praticesig/domain/user/user_repository.dart';

import 'package:praticesig/pages/pick_image_page.dart';
import 'package:get/get.dart';
import 'package:praticesig/util/validator_util.dart';

class PostUserNamePage extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();
  final _name = TextEditingController();
  final _d_num = TextEditingController();

  final UserRepository u = UserRepository();
  final _image = Image.asset('assets/nike.png');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //body나 scaffold 위젯이 높이가 정의된 스크린 키보드에 의해 스스로 크기를 재조정.
      resizeToAvoidBottomInset: true,
      //https://api.flutter.dev/flutter/material/Scaffold/extendBody.html
      extendBody: true,
      appBar: AppBar(
        backgroundColor: Color(0xff6E9FED),
      ),
      body: Center(
        child: ListView(
          shrinkWrap: true,
          padding: const EdgeInsets.only(left: 24.0, right: 24.0),
          children: <Widget>[
            const Text(
              "카나리아",
              style: TextStyle(
                fontSize: 40,
                color: Colors.indigo,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.left,
            ),
            const Text("자신의 군번을 입력해주세요!"),
            const SizedBox(height: 48),
            Form(
              key: _formKey,
              child: Column(
                children: [
                  CustomTextFormField(
                    funValidator: validateUsername(),
                    hint: "이름",
                    controller: _name,
                  ),
                  CustomTextFormField(
                    funValidator: validateUsername(),
                    hint: "군번",
                    controller: _d_num,
                  ),
                ],
              ),
            ),
            const SizedBox(
              height: 48,
            ),
            TextButton(
              child: const GradationButton(title: "go"),
              onPressed: () async {
                if (_formKey.currentState!.validate()) {
                  int success = await u.postUserName(_name.text, _d_num.text);
                  if (success == 1) {
                    Get.to(() => const PickImagePage());
                  }
                } else {
                  Get.snackbar("로그인 실패", "정보를 정확히 입력해주세요!");
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
