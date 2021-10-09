class Output {
  final String output;

  Output({
    required this.output,
  });

  //통신을 위해서 json처럼 생긴 문자열 : ex => {"id":1} => Dart 오브젝트
  factory Output.fromJson(Map<String, dynamic> json) {
    return Output(output: json['output']);
  }
}

// class Output {
//   final String img_binary;
//   final String warning;

//   Output({
//     required this.img_binary,
//     required this.warning,
//   });

//   //통신을 위해서 json처럼 생긴 문자열 : ex => {"id":1} => Dart 오브젝트
//   factory Output.fromJson(Map<String, dynamic> json) {
//     return Output(img_binary : json['img_binary'], warning : json[warning],);
//   }
// }
