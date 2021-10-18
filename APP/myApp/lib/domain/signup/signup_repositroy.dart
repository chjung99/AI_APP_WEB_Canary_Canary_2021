import 'package:myapp/domain/signup/signup_provider.dart';

class SignUpRepository {
  final SignUpProvider _signUpProvider = SignUpProvider();

  Future<int> signup(String name, String d_num, String password) async {
    final response = await _signUpProvider.SignUp(name, d_num, password);
    if (response.statusCode == 200) {
      return 1;
    } else {
      throw Exception('Failed to create');
    }
  }
}
