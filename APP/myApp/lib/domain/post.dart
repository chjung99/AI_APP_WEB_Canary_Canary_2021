class Post {
  final String? username;

  Post({
    this.username,
  });

  //통신을 위해서 json처럼 생긴 문자열 : ex => {"id":1} => Dart 오브젝트
  Post.fromJson(Map<String, dynamic> json) : username = json["username"];
}
