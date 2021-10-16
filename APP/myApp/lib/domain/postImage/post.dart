class Post {
  final String imd_id;
  final String d_num;

  Post({
    required this.imd_id,
    required this.d_num,
  });

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(
      imd_id: json['imd_id'].toString(),
      d_num: json['d_num'],
    );
  }
}
