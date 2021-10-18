import 'dart:convert';
import 'package:image_picker/image_picker.dart';

import 'package:myapp/domain/postImage/post.dart';
import 'package:myapp/domain/postImage/post_provider.dart';

class PostRepository {
  final PostProvider _postProvider = PostProvider();

  Future<Post> postImage(XFile image, String d_num) async {
    final bytes = await image.readAsBytes();
    String _img64 = base64Encode(bytes);
    final response = await _postProvider.postImage(_img64, d_num);
    if (response.statusCode == 200) {
      return Post.fromJson(jsonDecode((response.body)));
    } else {
      throw Exception('Failed to create');
    }
  }
}
