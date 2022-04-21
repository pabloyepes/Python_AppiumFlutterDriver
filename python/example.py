from selenium.common.exceptions import NoSuchElementException
from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

waits = {
    "XS": 1,
    "M": 5,
    "L": 10
}


def find_element(finder_, wait=waits['L']):
    try:
        driver.execute_script('flutter:waitFor', finder_, wait)
        return FlutterElement(driver, finder_)
    except:
        raise NoSuchElementException(
            f'The element was not found after waiting for {wait} seconds')


driver = Remote('http://localhost:4723/wd/hub', dict(
    platformName='android',
    automationName='flutter',
    deviceName='4756cdb70804',
    unicodeKeyboard=True,
    resetKeyboard=True,
    newCommandTimeout=60,
    waitForIdleTimeout=60,
    retryBackoffTime=10,
    appPackage="com.example.my_flutter_app",
    appActivity="com.example.my_flutter_app.MainActivity",
))

print('Appium session started')
finder = FlutterFinder()


finders = {
    'total_push_label': finder.by_text('You have pushed the button this many times:'),
    'counter_label': finder.by_value_key('counter'),
    'increment_button': finder.by_tooltip('Increment')
}

print(find_element(finders['total_push_label']))

counter_label = find_element(finders['counter_label'])
print("Test 1")
increment_button = find_element(finders['increment_button'])
print("Test 2")
print(counter_label.text)
increment_button.click()
print(counter_label.text)
increment_button.click()
print(counter_label.text)
print('Test Passed')
driver.quit()
