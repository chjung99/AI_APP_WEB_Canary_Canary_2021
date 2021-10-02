Function validateUsername() {
  return (String? value) {
    if (value!.isEmpty) {
      return "공백이 들어갈 수 없습니다.";
    } else {
      return null;
    }
  };
}

Function validateDnum() {
  return (String? value) {
    if (value!.isEmpty) {
      return "공백이 들어갈 수 없습니다.";
    } else if (value.length > 30) {
      return "제목의 길이를 초과할 수 없습니다.";
    } else {
      return null;
    }
  };
}
