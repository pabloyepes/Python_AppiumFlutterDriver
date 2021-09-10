from selenium.common.exceptions import NoSuchElementException
from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.common.touch_action import TouchAction


waits = {
    "XS": 1,
    "M": 5,
    "L": 10
}

# https://gitmemory.com/issue/truongsinh/appium-flutter-driver/113/762621944


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
    'entry_g': finder.by_text('Entry G'),
    'entry_o': finder.by_text('Entry O')
}
# Wait for screen to load
find_element(finders['entry_g'], waits['L'])

# scroll until element is visible from_item, opts={item, dx, dy}
driver.execute_script('flutter:scrollUntilVisible', finders['entry_g'], {
                      "item": finders['entry_o'], "dxScroll": 10, "dyScroll": -30})
print(find_element(finders['entry_o']).text)

# https://github.com/appium-userland/appium-flutter-driver/blob/ce2315acf28a3b92386779ecb9e7a45d62a3eca9/example/nodejs/src/index.js
# scroll up
driver.execute_script('flutter:scroll',finders['entry_o'], {"dx": 10, "dy": 300, "durationMilliseconds": 200, "frequency": 30})

# scroll down
driver.execute_script('flutter:scroll',finders['entry_g'], {"dx": 10, "dy": -100, "durationMilliseconds": 200, "frequency": 30})

print('Test Passed')
driver.quit()
