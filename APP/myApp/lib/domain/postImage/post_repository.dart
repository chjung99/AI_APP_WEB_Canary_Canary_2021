import 'dart:convert';
import 'package:image_picker/image_picker.dart';

import 'package:praticesig/domain/postImage/post.dart';
import 'package:praticesig/domain/postImage/post_provider.dart';

class PostRepository {
  final PostProvider _postProvider = PostProvider();

  // XFile 변환 및 연결 확인용
  // https://codesearchonline.com/flutter-convert-image-base64/
  //https://stackoverflow.com/questions/46145472/how-to-convert-base64-string-into-image-with-flutter

  Future<Post> postImage(XFile image) async {
    final bytes = await image.readAsBytes();
    String _img64 = base64Encode(bytes);
    final response = await _postProvider.postImage(_img64);
    if (response.statusCode == 200) {
      return Post.fromJson(jsonDecode((response.body)));
    } else {
      throw Exception('Failed to create');
    }
  }
}
