import 'dart:convert';
import 'dart:html';
import 'dart:typed_data';
import 'dart:io' as Io;

import 'package:image_picker/image_picker.dart';
import 'package:praticesig/components/dto/image_req_dto.dart';
import 'package:praticesig/domain/post_provider.dart';
import 'package:praticesig/components/dto/login_req_dto.dart';

class PostRepository {
  final PostProvider _postProvider = PostProvider();

  /*두개 같이 보내는 코드(근데 Image임) => 저번에 원하신거?
  Future<void> postUserInfo(String username, var imageFile) async {
    List<int> bytes = imageFile.readAsBytesSync();
    String _img64 = base64Encode(bytes);
    LoginReqDto loginReqDto = LoginReqDto(username, _img64);
    await _postProvider.postUserInfo(loginReqDto.toJson());
  }
  */

  Future<void> postUserName(String username) async {
    LoginReqDto loginReqDto = LoginReqDto(username);
    await _postProvider.PostUserNamePage(loginReqDto.toJson());
  }

  // XFile 변환 및 연결 확인용
  // https://codesearchonline.com/flutter-convert-image-base64/
  Future<void> postImage(XFile image) async {
    final bytes = await image.readAsBytes();
    String _img64 = base64Encode(bytes);
    ImageReqDto imageReqDto = ImageReqDto(_img64);
    await _postProvider.postImage(imageReqDto.toJson());
  }
}
