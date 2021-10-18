import 'dart:typed_data';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:qr_flutter/qr_flutter.dart';

Future<Uint8List> toQrImageData(String text) async {
  try {
    final image = await QrPainter(
      data: text,
      version: QrVersions.auto,
      gapless: false,
      emptyColor: Colors.white,
    ).toImage(50);
    final a = await image.toByteData(format: ui.ImageByteFormat.png);
    return a!.buffer.asUint8List();
  } catch (e) {
    throw e;
  }
}
