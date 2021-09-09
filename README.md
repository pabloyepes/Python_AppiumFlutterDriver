# Python_AppiumFlutterDriver
Basic APP with flutter and automation with AppiumFlutterDriver

# Basic APP example for automation with Appium Flutter Driver and Python

Required Appium version: v1.21.0 [v1.21.0](https://github.com/appium/appium-desktop/releases/tag/v1.21.0)
Python version 3.9.5

## Flutter Driver vs Appium Flutter Driver
Even though Flutter comes with superb integration test support, [Flutter Driver](https://flutter.dev/docs/cookbook/testing/integration/introduction), it does not fit some specific use cases, such as
- writing test in other languages than Dart
- running integration test for Flutter app with embedded webview or native view, or existing native app with embedded Flutter view
- running test on multiple devices simultaneously
- running integration test on device farms, such as Sauce Labs, AWS, Firebase

Under the hood, Appium Flutter Driver use the [Dart VM Service Protocol](https://github.com/dart-lang/sdk/blob/master/runtime/vm/service/service.md) with extension `ext.flutter.driver`, similar to Flutter Driver, to control the Flutter app-under-test (AUT).

## Installation

In order to use `appium-flutter-driver` with python we need to use `appium` version `1.21.0` or higher

```
pip install Appium-Flutter-Finder
```
or with a requirements.txt file
```
pip install -r requirements.txt
```

## Generate APK in debug mode
```
flutter run
```


## Run the test
1. Start appium server
2. Generate the APK in debug mode if this hasn't been done previously and install it in the android device
3. In a console, navigate to the path where the example.py file is located
4. Start the virtualenvironment if it's used, otherwise install the requirements file `pip install -r requirements.txt`
5. Launch the python file `python example.py`