class ImageReqDto {
  final String? imageFile;

  ImageReqDto(this.imageFile);

  Map<String, dynamic> toJson() => {
        "img_binary": imageFile,
      };
}
