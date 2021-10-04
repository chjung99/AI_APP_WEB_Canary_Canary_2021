import 'package:praticesig/components/dto/login_req_dto.dart';
import 'package:praticesig/domain/user/user.dart';
import 'package:praticesig/domain/user/user_provider.dart';

class UserRepository {
  final UserProvider _userProvider = UserProvider();

  Future<int> postUserName(String name, String d_num) async {
    final response = await _userProvider.postUserNamePage(name, d_num);
    if (response.statusCode == 200) {
      return 1;
    } else {
      throw Exception('Failed to create');
    }
  }
}

//   Future<void> postUserName(String name, String d_num) async {
//     LoginReqDto loginReqDto = LoginReqDto(name, d_num);
//     await _userProvider.postUserNamePage(loginReqDto.toJson());
//   }
// }
