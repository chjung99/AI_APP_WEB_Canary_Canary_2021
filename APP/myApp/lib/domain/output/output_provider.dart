import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:get/get.dart';
import 'package:praticesig/domain/postImage/post.dart';

//통신
class OutputProvider extends GetConnect {
  Future<http.Response> getImage(String uri) => http.get(
        Uri.parse(uri),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
      );
}
