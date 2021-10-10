// UI 모음집 :  https://github.com/lohanidamodar/flutter_ui_challenges
// 애니메이션 : https://github.com/yumi0629/FlutterUI
import 'package:flutter/material.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/components/custom_text_form_field.dart';

import 'package:praticesig/domain/user/user_repository.dart';

import 'package:praticesig/pages/gallery_page.dart';
import 'package:get/get.dart';
import 'package:praticesig/pages/option_page.dart';
import 'package:praticesig/pages/signup.dart';
import 'package:praticesig/util/validator_util.dart';

class SignInPage extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();
  final _password = TextEditingController();
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
      appBar: appbarmaker(),
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
                fontFamily: "BlackHanSans",
              ),
              textAlign: TextAlign.left,
            ),
            const Text("군번과 비밀번호를 입력해주세요"),
            const SizedBox(height: 48),
            Form(
              key: _formKey,
              child: Column(
                children: [
                  CustomTextFormField(
                    signIn: true,
                    funValidator: validateUsername(),
                    hint: "군번을",
                    controller: _d_num,
                  ),
                  CustomTextFormField(
                    signIn: true,
                    funValidator: validateUsername(),
                    hint: "비밀번호를",
                    controller: _password,
                  ),
                ],
              ),
            ),
            const SizedBox(
              height: 48,
            ),
            TextButton(
              child: const GradationButton(
                title: "go",
                width: 400,
                height: 50,
              ),
              onPressed: () async {
                if (_formKey.currentState!.validate()) {
                  int success =
                      await u.postUserName(_d_num.text, _password.text);
                  if (success == 1) {
                    Get.to(() => const OptionPage());
                  }
                } else {
                  Get.snackbar("로그인 실패", "정보를 정확히 입력해주세요!");
                }
              },
            ),
            SizedBox(height: 10),
            TextButton(
              onPressed: () {
                Get.to(() => SignUpPage());
              },
              child: Text(
                "회원가입 하러가기",
                style: TextStyle(color: Colors.black),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
