class User {
  final String? msg;
  final int? status;

  User(this.msg, this.status);

  User.fromJson(Map<String, dynamic> json)
      : status = json["status"],
        msg = json["msg"];
}
