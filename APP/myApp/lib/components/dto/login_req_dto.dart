/*
class LoginReqDto {
  final String? username;
  final String? img_binary;

  LoginReqDto(this.username, this.img_binary);

  Map<String, dynamic> toJson() =>
      {"username": username, "img_binary": img_binary};
}
*/

class LoginReqDto {
  final String? username;

  LoginReqDto(this.username);

  Map<String, dynamic> toJson() => {"username": username};
}
