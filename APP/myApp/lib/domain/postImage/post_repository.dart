import 'dart:convert';
import 'package:image_picker/image_picker.dart';

import 'package:praticesig/domain/postImage/post.dart';
import 'package:praticesig/domain/postImage/post_provider.dart';

class PostRepository {
  final PostProvider _postProvider = PostProvider();

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
