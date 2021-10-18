import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_text.dart';
import 'package:myapp/components/custom_text_form_field.dart';
import 'package:myapp/domain/signup/signup_repository.dart';
import 'package:myapp/screens/signinpage.dart';
import 'package:myapp/util/validator_util.dart';

import '../size.dart';

class SignUpPage extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();
  final _name = TextEditingController();
  final _d_num = TextEditingController();
  final _password = TextEditingController();

  final SignUpRepository s = SignUpRepository();

  SignUpPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Center(
        child: ListView(
          shrinkWrap: true,
          padding: const EdgeInsets.symmetric(horizontal: marginHorizontalSize),
          children: <Widget>[
            const SizedBox(height: marginVerticalSize),
            Text(
              "Sign up",
              style: CustomText(size: titleTextSize),
            ),
            const Text("군번과 비밀번호를 입력해주세요"),
            const SizedBox(height: marginVerticalSize),
            Form(
              key: _formKey,
              child: Column(
                children: [
                  CustomTextFormField(
                    signIn: false,
                    funValidator: validateUsername(),
                    hint: "이름을",
                    controller: _name,
                  ),
                  const SizedBox(height: 10),
                  CustomTextFormField(
                    signIn: false,
                    funValidator: validateDnum(),
                    hint: "군번(-은 제외)을",
                    controller: _d_num,
                  ),
                  const SizedBox(height: 10),
                  CustomTextFormField(
                    signIn: false,
                    funValidator: validateEng(),
                    hint: "비밀번호를",
                    controller: _password,
                  ),
                  SizedBox(height: 5),
                  validatePassWord(_password),
                ],
              ),
            ),
            const SizedBox(height: marginVerticalSize),
            TextButton(
              child: const GradationButton(
                title: "가입완료",
              ),
              onPressed: () async {
                if (_formKey.currentState!.validate()) {
                  int success = await s.signup(_name.text.trim(),
                      _d_num.text.trim(), _password.text.trim());
                  if (success == 1) {
                    Get.to(() => SignInPage());
                    Get.snackbar("회원가입 완료", "회원가입이 완료되었습니다!");
                  }
                } else {
                  Get.snackbar("회원가입 실패", "누락된 정보를 입력해주세요!");
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
