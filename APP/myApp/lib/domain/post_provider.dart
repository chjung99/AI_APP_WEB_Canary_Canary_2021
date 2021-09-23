import 'dart:html';

import 'package:http/http.dart' as http;
import 'package:get/get.dart';
import 'package:praticesig/pages/post_username_page.dart';

var host = Uri.parse("https://osam-project-testing-tkqtg.run.goorm.io/users");
var host2 =
    Uri.parse("https://osam-project-testing-tkqtg.run.goorm.io/img_upload");

//통신
class PostProvider extends GetConnect {
  // 서준 testing
  //Future<void> postUserInfo(Map data) => http.post(host2, body: data);

  Future<void> PostUserNamePage(Map data) => http.post(host, body: data);

  Future<void> postImage(Map data) => http.post(host2, body: data);
}


//content 타입! 추가해야되는지

