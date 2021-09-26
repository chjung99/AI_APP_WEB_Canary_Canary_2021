import 'package:http/http.dart' as http;
import 'package:get/get.dart';

var host = Uri.parse("https://osam-project-testing-tkqtg.run.goorm.io/users");
var host2 =
    Uri.parse("https://osam-project-testing-tkqtg.run.goorm.io/img_upload");

//통신
class PostProvider extends GetConnect {
  // 서준 testing
  //Future<void> postUserInfo(Map data) => http.post(host2, body: data);

  Future<void> postUserNamePage(Map data) => http.post(host, body: data);

  //Response 타입으로 하면 에러나옴
  //A value of type 'Future<Response>' can't be returned from the method 'postImage' because it has a return type of 'Future<Response<dynamic>>'.

  Future<dynamic> postImage(Map data) => http.post(host2, body: data);
}
