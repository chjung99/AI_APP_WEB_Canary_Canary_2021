import 'dart:convert';
import 'package:get/get_connect/connect.dart';
import 'package:image_picker/image_picker.dart';
import 'package:praticesig/components/dto/image_req_dto.dart';
import 'package:praticesig/domain/post_provider.dart';
import 'package:praticesig/components/dto/login_req_dto.dart';
import 'package:praticesig/util/covert_uint8list.dart';

class PostRepository {
  final PostProvider _postProvider = PostProvider();

  Future<void> postUserName(String name, String d_num) async {
    LoginReqDto loginReqDto = LoginReqDto(name, d_num);
    await _postProvider.postUserNamePage(loginReqDto.toJson());
  }

  // XFile 변환 및 연결 확인용
  // https://codesearchonline.com/flutter-convert-image-base64/
  //https://stackoverflow.com/questions/46145472/how-to-convert-base64-string-into-image-with-flutter

  Future<Map<String, dynamic>> postImage(XFile image) async {
    final bytes = await image.readAsBytes();
    int success = 0;
    String _img64 = base64Encode(bytes);
    ImageReqDto imageReqDto = ImageReqDto(_img64);
    Response response = await _postProvider.postImage(imageReqDto.toJson());

    if (response.statusCode == 200) {
      success = 1;
    }
    dynamic bodyBytes = response.bodyBytes;
    dynamic convertBodyBytes = convertUint8List(bodyBytes, success);
    return convertBodyBytes;
  }
}
