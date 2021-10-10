import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/custom_button.dart';
import 'package:praticesig/components/custom_text.dart';
import 'package:praticesig/components/custom_text_form_field.dart';
import 'package:praticesig/pages/signin.dart';
import 'package:praticesig/util/validator_util.dart';

class SignUpPage extends StatelessWidget {
  final _formKey = GlobalKey<FormState>();
  final _name = TextEditingController();
  final _d_num = TextEditingController();
  final _password = TextEditingController();
  final _classes = TextEditingController();

  SignUpPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Center(
        child: ListView(
          shrinkWrap: true,
          padding: const EdgeInsets.only(left: 24.0, right: 24.0),
          children: <Widget>[
            const SizedBox(height: 48),
            customText(text: "회원가입", size: 40),
            const Text("군번과 비밀번호를 입력해주세요"),
            const SizedBox(height: 48),
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
                  SizedBox(height: 3),
                  CustomTextFormField(
                    signIn: false,
                    funValidator: validateUsername(),
                    hint: "계급을",
                    controller: _classes,
                  ),
                  SizedBox(height: 5),
                  CustomTextFormField(
                    signIn: false,
                    funValidator: validateUsername(),
                    hint: "군번을",
                    controller: _d_num,
                  ),
                  SizedBox(height: 10),
                  CustomTextFormField(
                    signIn: false,
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
                title: "가입완료",
                width: 400,
                height: 50,
              ),
              onPressed: () {
                if (_formKey.currentState!.validate()) {
                  Get.to(() => SignInPage());
                  Get.snackbar("회원가입 완료", "회원가입이 완료되었습니다!");
                } else {
                  Get.snackbar("회원가입 실패", "누락된 정보를 입력해주세요!");
                }
              },
            ),
            SizedBox(height: 10),
          ],
        ),
      ),
    );
  }
}
