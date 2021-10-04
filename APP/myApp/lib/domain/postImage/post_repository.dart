import 'dart:convert';
import 'package:image_picker/image_picker.dart';
import 'package:praticesig/components/dto/image_req_dto.dart';
import 'package:praticesig/domain/postImage/post.dart';
import 'package:praticesig/domain/postImage/post_provider.dart';

class PostRepository {
  final PostProvider _postProvider = PostProvider();

  // XFile 변환 및 연결 확인용
  // https://codesearchonline.com/flutter-convert-image-base64/
  //https://stackoverflow.com/questions/46145472/how-to-convert-base64-string-into-image-with-flutter

  Future<void> postImage(XFile image) async {
    final bytes = await image.readAsBytes();
    String _img64 = base64Encode(bytes);
    ImageReqDto imageReqDto = ImageReqDto(_img64);
    await _postProvider.postImage(imageReqDto.toJson());
  }

  Future<Post> get getImage async {
    final response = await _postProvider.getImage();
    dynamic body = response.bodyBytes;
    if (response.statusCode == 200) {
      Post post = Post.fromJson(body);
      return post;
    } else {
      return Post(output: "error");
    }
  }
}
