#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import HtmlTestRunner
from zipfile import ZipFile
import json
import os
import random
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

        # remove zipped file from `test_pull_folder`
        if hasattr(self, 'zipfilename') and os.path.isfile(self.zipfilename):
            os.remove(self.zipfilename)



    def test_background_app(self):
        self.driver.background_app(1)
        el = self.driver.find_elements_by_accessibility_id('Animation')
        self.assertIsNotNone(el)

    def test_is_app_installed(self):
        self.assertFalse(self.driver.is_app_installed('sdfsdf'))
        self.assertTrue(self.driver.is_app_installed('com.example.android.apis'))

    def test_install_app(self):
        self.skipTest('This causes the server to crash. no idea why')
        self.assertFalse(self.driver.is_app_installed('io.selendroid.testapp'))
        self.driver.install_app('/Users/isaac/code/python-client/test/apps/selendroid-test-app.apk')
        self.assertTrue(self.driver.is_app_installed('io.selendroid.testapp'))

    def test_remove_app(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.apis'))
        self.driver.remove_app('com.example.android.apis')
        self.assertFalse(self.driver.is_app_installed('com.example.android.apis'))

    def test_close__and_launch_app(self):
        el = self.driver.find_elements_by_accessibility_id('Animation')
        self.assertIsNotNone(el)

        self.driver.close_app()
        self.driver.launch_app()

        el = self.driver.find_elements_by_accessibility_id('Animation')
        self.assertIsNotNone(el)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    testRunner=HtmlTestRunner.HTMLTestRunner(output='result',report_title='测试报告')
    testRunner.run(suite)
