import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/components/logo.dart';

import 'package:praticesig/pages/post_username_page.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const Text(
              "카나리아",
              style: TextStyle(
                fontSize: 40,
                fontWeight: FontWeight.bold,
                color: Colors.indigo,
              ),
            ),
            const Text("모두를 위한 군사보안 경보기"),
            const SizedBox(height: 48.0),
            Logo(
              image: "OSAM.jpg",
              width: 70,
              height: 70,
            ),
            TextButton(
              child: const GradationButton(title: "go"),
              onPressed: () {
                Get.to(() => PostUserNamePage());
              },
            ),
            const SizedBox(height: 8.0),
            TextButton(
              child: const GradationButton(title: "help"),
              onPressed: () {
                Get.to(() => PostUserNamePage());
              },
            ),
            const SizedBox(height: 60.0),
          ],
        ),
      ),
    );
  }
}
