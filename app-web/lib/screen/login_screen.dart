import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:flutter_signin_button/flutter_signin_button.dart';
import 'package:wyly_app/service/env_service.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  static final _googleLogin = GoogleSignIn(
    scopes: [
      'email',
      'https://www.googleapis.com/auth/contacts.readonly',
    ],
    clientId: getEnv('GOOGLE_AUTH_CLIENT_ID'),
  );

  final FirebaseAuth _auth = FirebaseAuth.instance;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const Text('ログインしてください'),
            const SizedBox(height: 16),
            SignInButton(
              Buttons.Google,
              text: 'Sign up with Google',
              onPressed: () async {
                await _login();
              },
            ),
          ],
        ),
      ),
    );
  }

  Future _login() async {
    final signInAccount = await _googleLogin.signIn();
    if (signInAccount == null) {
      return;
    }

    final auth = await signInAccount.authentication;
    final credential = GoogleAuthProvider.credential(
      idToken: auth.idToken,
      accessToken: auth.accessToken,
    );
    final result = await _auth.signInWithCredential(credential);

    print(result.user!.uid.toString()); // ignore: avoid_print
    print(result.user!.email.toString()); // ignore: avoid_print
    print(result.user!.displayName.toString()); // ignore: avoid_print
  }
}
