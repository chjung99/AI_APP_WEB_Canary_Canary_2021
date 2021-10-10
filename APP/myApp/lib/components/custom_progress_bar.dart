import 'package:flutter/material.dart';

Column buildBar() {
  return Column(
    children: [
      Container(
        height: 1,
        width: 180,
        color: Colors.black,
      ),
      const SizedBox(height: 20),
    ],
  );
}

Container buildIcon(int iconColor, IconData numIcon, String page) {
  return Container(
    height: 40,
    width: 40,
    child: Column(
      children: [
        Icon(
          numIcon,
          color: (iconColor == 1) ? Colors.green : Colors.grey,
        ),
        Text(
          page,
          style: const TextStyle(fontSize: 7, color: Colors.black),
        ),
      ],
    ),
  );
}

Container buildCheckIcon(String page) {
  return Container(
    height: 40,
    width: 40,
    child: Column(
      children: [
        const Icon(
          Icons.check_circle,
          color: Colors.blue,
        ),
        Text(
          page,
          style: const TextStyle(fontSize: 7, color: Colors.black),
        ),
      ],
    ),
  );
}

Widget createProgressBar(bool chooseImage, bool resultImage, bool saveImage) {
  int green = 1;
  int grey = 0;
  List<IconData> icon = [Icons.looks_one, Icons.looks_two, Icons.looks_3];
  List<String> page = ["이미지 선택", "결과 선택", "저장"];
  if (!chooseImage) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        buildIcon(green, icon[0], page[0]),
        buildBar(),
        buildIcon(grey, icon[1], page[1]),
        buildBar(),
        buildIcon(grey, icon[2], page[2]),
      ],
    );
  } else {
    if (!resultImage) {
      return Row(
        //resultPage
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          buildCheckIcon(page[1]),
          buildBar(),
          buildIcon(green, icon[1], page[1]),
          buildBar(),
          buildIcon(grey, icon[2], page[2]),
        ],
      );
    } else {
      //savePage
      return Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          buildCheckIcon(page[0]),
          buildBar(),
          buildCheckIcon(page[1]),
          buildBar(),
          buildIcon(green, icon[2], page[2]),
        ],
      );
    }
  }
}
