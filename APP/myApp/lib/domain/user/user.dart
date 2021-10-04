class User {
  final String? name;
  final String? d_num;
  final int? status;

  User(this.name, this.d_num, this.status);

  User.fromJson(Map<String, dynamic> json)
      : name = json["name"],
        d_num = json["d_num"],
        status = json["status"];
}
