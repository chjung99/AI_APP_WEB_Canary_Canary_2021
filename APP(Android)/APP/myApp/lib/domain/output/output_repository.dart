import 'dart:convert';

import 'package:myapp/domain/output/output_provider.dart';

import 'output.dart';

class OutputRepository {
  final OutputProvider _outputProvider = OutputProvider();

  Future<Output> getImage(String uri) async {
    final response = await _outputProvider.getImage(uri);
    if (response.statusCode == 200) {
      return Output.fromJson(jsonDecode((response.body)));
    } else {
      throw Exception('Failed to create');
    }
  }
}
