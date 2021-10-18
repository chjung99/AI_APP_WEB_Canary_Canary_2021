import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:myapp/components/app_bar_maker.dart';
import 'package:myapp/components/custom_button.dart';
import 'package:myapp/components/custom_text.dart';
import 'package:myapp/components/logo.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:myapp/screens/signinpage.dart';
import 'package:myapp/size.dart';

import 'loadingpage.dart';
import 'optionpage.dart';

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
                  Text(
                    "카나리아",
                    style: CustomText(size: 60),
                  ),
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
                  Text(
                    "모두를 위한 군사 경보기",
                    style: CustomText(size: 20),
                  ),
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
              onPressed: () async {
                const url =
                    "https://github.com/osamhack2021/AI_APP_WEB_Canary_Canary";
                if (await canLaunch(url)) {
                  await launch(url);
                } else {
                  throw "Could not launch $url";
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
