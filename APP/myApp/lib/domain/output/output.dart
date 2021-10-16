class Output {
  final String prc_img;
  final String warning_text;
  final String hashed_d_num;
  Output({
    required this.prc_img,
    required this.warning_text,
    required this.hashed_d_num,
  });

  //통신을 위해서 json처럼 생긴 문자열 : ex => {"id":1} => Dart 오브젝트
  factory Output.fromJson(Map<String, dynamic> json) {
    return Output(
        prc_img: json['prc_img'],
        warning_text: json['warning_text'],
        hashed_d_num: json['hashed_d_num']);
  }
}
