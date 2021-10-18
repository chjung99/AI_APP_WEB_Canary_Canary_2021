import 'dart:convert';

import 'package:myapp/domain/user/user.dart';
import 'package:myapp/domain/user/user_provider.dart';

class UserRepository {
  final UserProvider _userProvider = UserProvider();

  Future<User> login(String d_num, String password) async {
    final response = await _userProvider.login(d_num, password);
    if (response.statusCode == 200) {
      print(response.body);
      return User.fromJson(jsonDecode((response.body)));
    } else {
      throw Exception('Failed to create');
    }
  }
}
