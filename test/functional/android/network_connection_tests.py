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

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
import desired_capabilities
import pdb


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1

import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings(record=True) as w:
    # Cause all warnings to always be triggered.
    warnings.simplefilter("always")
    # Trigger a warning.
    fxn()
    # Verify some things
    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)
    assert "deprecated" in str(w[-1].message)

class NetworkConnectionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_get_network_connection(self):
        nc = self.driver.network_connection
        self.assertIsInstance(nc, int)

    @unittest.skip('done')
    def test_set_network_connection(self):
        nc = self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        self.assertIsInstance(nc, int)
        self.assertEqual(nc, ConnectionType.ALL_NETWORK_ON.value)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(NetworkConnectionTests)
    testRunner=HtmlTestRunner.HTMLTestRunner(output='result',report_title='测试报告')
    testRunner.run(suite)
