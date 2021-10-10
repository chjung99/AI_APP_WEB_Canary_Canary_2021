class Post {
  final String imd_id;

  Post({
    required this.imd_id,
  });

  //통신을 위해서 json처럼 생긴 문자열 : ex => {"id":1} => Dart 오브젝트
  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(imd_id: json['imd_id'].toString());
  }
}
