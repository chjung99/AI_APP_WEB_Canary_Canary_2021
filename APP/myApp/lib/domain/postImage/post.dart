class Post {
  final String imd_id;

  Post({
    required this.imd_id,
  });

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(imd_id: json['imd_id'].toString());
  }
}
