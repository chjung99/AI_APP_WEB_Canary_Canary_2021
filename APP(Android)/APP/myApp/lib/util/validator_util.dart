import 'package:flutter/material.dart';
import 'package:flutter_pw_validator/flutter_pw_validator.dart';
import 'package:string_validator/string_validator.dart';

Function validateUsername() {
  return (String? value) {
    if (value!.isEmpty) {
      return "공백이 들어갈 수 없습니다.";
    } else {
      return null;
    }
  };
}

Widget validatePassWord(TextEditingController _passwordController) {
  return FlutterPwValidator(
    controller: _passwordController,
    minLength: 6,
    uppercaseCharCount: 2,
    numericCharCount: 3,
    specialCharCount: 1,
    width: 400,
    height: 150,
    onSuccess: () {},
  );
}

Function validateEng() {
  return (String? value) {
    if (isAlpha(value!)) {
      return "영어, 숫자, 특수문자만을 입력해주세요.";
    } else {
      return null;
    }
  };
}

Function validateDnum() {
  return (String? value) {
    if (value!.isEmpty) {
      return "공백이 들어갈 수 없습니다.";
    } else if (value.length != 10) {
      return "군번은 10자리 숫자입니다";
    } else {
      return null;
    }
  };
}
