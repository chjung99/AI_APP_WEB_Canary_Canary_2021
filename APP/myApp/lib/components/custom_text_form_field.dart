import 'package:flutter/material.dart';

class CustomTextFormField extends StatelessWidget {
  final String hint;
  final funValidator;
  final controller;
  final bool signIn;
  const CustomTextFormField(
      {required this.funValidator,
      this.controller,
      required this.hint,
      required this.signIn});

  @override
  Widget build(BuildContext context) {
    ThemeData _theme = Theme.of(context);
    return Container(
      width: 400,
      child: TextFormField(
        controller: controller,
        validator: funValidator,
        decoration: InputDecoration(
          hintText: "$hint 입력하세요",
          suffixIcon: (signIn) ? Icon(Icons.account_box_outlined) : Icon(null),
          border: (signIn)
              ? null
              : OutlineInputBorder(
                  borderRadius: BorderRadius.circular(20),
                ),
        ),
        style: _theme.inputDecorationTheme.labelStyle,
      ),
    );
  }
}
