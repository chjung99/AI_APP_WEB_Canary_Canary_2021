import 'dart:convert';

import 'package:get/get.dart';
import 'package:http/http.dart' as http;

var host =
    Uri.parse("https://osam-project-testing-tkqtg.run.goorm.io/auth/login");

class UserProvider extends GetConnect {
  Future<http.Response> login(String d_num, String password) => http.post(
        host,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          'd_num': d_num,
          'password': password,
        }),
      );
}
