import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:praticesig/components/app_bar_maker.dart';
import 'package:praticesig/components/custom_button.dart';
import 'package:praticesig/components/custom_text.dart';
import 'package:praticesig/components/logo.dart';

import 'package:praticesig/pages/signin.dart';
import 'package:praticesig/size.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appbarmaker(),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(height: marginVerticalSize),
            Padding(
              padding: const EdgeInsets.only(left: marginHorizontalSize),
              child: Row(
                children: [
                  customText(text: "카나리아", size: 60),
                  const SizedBox(width: 5),
                  const Logo(
                    image: "CANARY.png",
                    width: 55,
                    height: 55,
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(right: marginHorizontalSize),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  customText(text: "모두를 위한 군사보안 경보기", size: 20),
                ],
              ),
            ),
            const SizedBox(height: marginVerticalSize),
            const Logo(
              image: "OSAM.jpg",
              width: 150,
              height: 150,
            ),
            const SizedBox(height: marginVerticalSize),
            TextButton(
              child: const GradationButton(
                title: "go",
                width: 340,
              ),
              onPressed: () {
                Get.to(() => SignInPage(), transition: Transition.rightToLeft);
              },
            ),
            const SizedBox(height: 8.0),
            TextButton(
              child: const GradationButton(
                title: "help",
                width: 340,
              ),
              onPressed: () {},
            ),
          ],
        ),
      ),
    );
  }
}
