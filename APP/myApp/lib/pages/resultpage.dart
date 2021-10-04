import 'package:flutter/material.dart';
import 'package:praticesig/domain/postImage/post.dart';
import 'package:praticesig/domain/postImage/post_repository.dart';

class ResultPage extends StatefulWidget {
  const ResultPage({Key? key}) : super(key: key);

  @override
  _ResultPageState createState() => _ResultPageState();
}

class _ResultPageState extends State<ResultPage> {
  late Future<Post> post;
  final PostRepository p = PostRepository();
  @override
  void initState() {
    super.initState();
    post = p.getImage;
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fetch Data Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('Fetch Data Example'),
        ),
        body: Center(
          child: FutureBuilder<Post>(
            future: post,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                return Text(snapshot.data!.output);
              } else if (snapshot.hasError) {
                return Text("${snapshot.error}");
              }

              // 기본적으로 로딩 Spinner를 보여줍니다.
              return CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}
