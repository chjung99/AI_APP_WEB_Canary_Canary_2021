class LoginReqDto {
  final String? name;
  final String? d_num;

  LoginReqDto(this.name, this.d_num);

  Map<String, dynamic> toJson() => {"name": name, "d_num": d_num};
}
