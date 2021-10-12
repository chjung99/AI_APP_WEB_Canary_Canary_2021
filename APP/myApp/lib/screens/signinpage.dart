// UI 모음집 :  https://github.com/lohanidamodar/flutter_ui_challenges
// 애니메이션 : https://github.com/yumi0629/FlutterUI
import 'package:flutter/material.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_text.dart';
import 'package:myapp/components/custom_text_form_field.dart';

import 'package:myapp/domain/user/user_repository.dart';

import 'package:get/get.dart';
import 'package:myapp/screens/optionpage.dart';
import 'package:myapp/screens/signuppage.dart';
import 'package:myapp/size.dart';
import 'package:myapp/util/validator_util.dart';

class SignInPage extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();
  final _password = TextEditingController();
  final _d_num = TextEditingController();

  final UserRepository u = UserRepository();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      extendBody: true,
      appBar: appbarmaker(),
      body: Center(
        child: ListView(
          shrinkWrap: true,
          padding: const EdgeInsets.symmetric(horizontal: marginHorizontalSize),
          children: <Widget>[
            customText(text: "Login", size: titleTextSize),
            const Text("군번과 비밀번호를 입력해주세요"),
            const SizedBox(height: marginVerticalSize),
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
            const SizedBox(height: marginVerticalSize),
            TextButton(
              child: const GradationButton(
                title: "go",
              ),
              onPressed: () async {
                if (_formKey.currentState!.validate()) {
                  int success =
                      await u.postUserName(_d_num.text, _password.text);
                  if (success == 1) {
                    Get.to(() => const OptionPage(),
                        transition: Transition.rightToLeft);
                  }
                } else {
                  Get.snackbar("로그인 실패", "정보를 정확히 입력해주세요!");
                }
              },
            ),
            const SizedBox(height: 10),
            TextButton(
              onPressed: () {
                Get.to(() => SignUpPage(), transition: Transition.upToDown);
              },
              child: const Text(
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
