import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/button_style.dart';
import 'package:praticesig/components/logo.dart';
import 'package:praticesig/pages/pick_image_page.dart';

import 'package:praticesig/pages/post_username_page.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xff6E9FED),
      ),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            SizedBox(height: 50),
            Padding(
              padding: const EdgeInsets.only(left: 20.0),
              child: Row(
                children: [
                  const Text(
                    "카나리아",
                    style: TextStyle(
                      fontSize: 60,
                      fontWeight: FontWeight.bold,
                      color: Colors.indigo,
                      fontFamily: "BlackHanSans",
                    ),
                  ),
                  SizedBox(width: 5),
                  Logo(
                    image: "CANARY.png",
                    width: 55,
                    height: 55,
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(right: 20.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  const Text(
                    "모두를 위한 군사보안 경보기",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.indigo,
                      fontFamily: "BlackHanSans",
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 48.0),
            Logo(
              image: "OSAM.jpg",
              width: 150,
              height: 150,
            ),
            SizedBox(height: 50),
            TextButton(
              child: const GradationButton(title: "go"),
              onPressed: () {
                Get.to(() => PickImagePage());
              },
            ),
            const SizedBox(height: 8.0),
            TextButton(
              child: const GradationButton(title: "help"),
              onPressed: () {
                Get.to(() => PostUserNamePage());
              },
            ),
          ],
        ),
      ),
    );
  }
}
