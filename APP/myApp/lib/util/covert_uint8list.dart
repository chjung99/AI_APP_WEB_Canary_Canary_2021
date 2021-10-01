import 'dart:convert';

Map<String, dynamic> convertUint8List(dynamic body, int success) {
  String responseBody = body; //json 데이터로 변경
  dynamic convertBody = base64Decode(responseBody);

  Map<String, dynamic> result = {
    "convertBody": convertBody,
    "success": success
  };
  return result;
}
