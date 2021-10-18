class SignUp {
  final String? name;
  final String? d_num;
  final String? password;

  SignUp(this.name, this.d_num, this.password);

  SignUp.fromJson(Map<String, dynamic> json)
      : name = json["name"],
        d_num = json["d_num"],
        password = json["password"];
}
