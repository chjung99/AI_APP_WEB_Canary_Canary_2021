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
