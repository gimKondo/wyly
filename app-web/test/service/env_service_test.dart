import 'dart:io';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:wyly_app/service/env_service.dart';

void main() {
  setUp(() async {
    dotenv.testLoad(fileInput: File('test/.env').readAsStringSync());
  });

  group('getEnv', () {
    test('env in dotenv', () {
      expect(getEnv('FOO'), 'foo');
    });
    test('env not exist', () {
      expect(getEnv('NOT_EXIST_KEY'), '');
    });
    test('env not exist with default value', () {
      expect(getEnv('NOT_EXIST_KEY', defaultValue: 'my-default'), 'my-default');
    });
  });
}
