import 'dart:convert';

import 'package:get/get.dart';
import 'package:http/http.dart' as http;

var host = Uri.parse(
    "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/auth/post-test");

// class UserProvider extends GetConnect {
//   Future<http.Response> postUserNamePage(Map data) =>
//       http.post(host, body: data);
// }

class UserProvider extends GetConnect {
  Future<http.Response> postUserNamePage(String name, String d_num) =>
      http.post(
        host,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          'name': name,
          'd_num': d_num,
        }),
      );
}
