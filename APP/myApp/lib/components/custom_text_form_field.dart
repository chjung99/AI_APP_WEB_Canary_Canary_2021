import 'package:flutter/material.dart';
import 'package:flutter/src/material/text_form_field.dart';
import 'package:flutter/src/material/input_border.dart';
import '../size.dart';
//로그인에서 validators 라이브러리 함수들 사용해보기!
import 'package:validators/validators.dart';

class CustomTextFormField extends StatelessWidget {
  final String text;

  const CustomTextFormField({required this.text});
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text("$text"),
        SizedBox(height: small_gap),
        TextFormField(
          validator: (value) =>
              value!.isEmpty ? "Please enter some Text" : null,
          decoration: InputDecoration(
            hintText: "Enter $text",
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(20),
            ), //enableBorder
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(20),
            ),
            errorBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(20),
            ),
            focusedErrorBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(20),
            ),
          ), //InputDecoration
        ), //TextFormField
      ],
    );
  }
}
