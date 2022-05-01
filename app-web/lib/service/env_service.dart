import 'package:flutter_dotenv/flutter_dotenv.dart';

/// Get environment value
///
/// ## Pre-requirement
///
/// initialized dotenv
///
/// ## Priority
///
/// 1. dart-define value
/// 2. dotenv value
/// 3. default value
String getEnv(String key, {String defaultValue = ''}) {
  if (bool.hasEnvironment(key)) {
    return String.fromEnvironment(key);
  }
  return dotenv.env[key] ?? defaultValue;
}
