import 'package:http/http.dart' as http;
import 'package:get/get.dart';
import 'package:praticesig/domain/post.dart';

var host = Uri.parse(
    "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/auth/post-tests");
var host2 = Uri.parse(
    "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/img/upload");
var host3 = Uri.parse(
    "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/img/output");

//통신
class PostProvider extends GetConnect {
  Future<void> postUserNamePage(Map data) => http.post(host, body: data);
  Future<void> postImage(Map data) => http.post(host2, body: data);
  Future<Response> getImage() => get(
      "https://osamhack2021-ai-app-web-canary-canary-g4x9r75r6fq49-4000.githubpreview.dev/img/output");
}
