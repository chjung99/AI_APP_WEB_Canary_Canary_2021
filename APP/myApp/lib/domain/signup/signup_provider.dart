import 'dart:convert';

import 'package:get/get.dart';
import 'package:http/http.dart' as http;

var host = Uri.parse(
    "https://osam-project-testing-tkqtg.run.goorm.io/auth/create-user");

class SignUpProvider extends GetConnect {
  Future<http.Response> SignUp(String name, String d_num, String password) =>
      http.post(
        host,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          'name': name,
          'd_num': d_num,
          'password': password,
        }),
      );
}
