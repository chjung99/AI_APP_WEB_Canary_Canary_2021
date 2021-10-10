import 'dart:convert';

import 'package:get/get.dart';
import 'package:http/http.dart' as http;

var host2 = Uri.parse("https://osam-project-testing-tkqtg.run.goorm.io/img/upload");
//"https://osam-project-testing-tkqtg.run.goorm.io/"

//통신
class PostProvider extends GetConnect {
  Future<http.Response> postImage(String img_binary) => http.post(
        host2,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          "img_binary": img_binary,
        }),
      );
}
