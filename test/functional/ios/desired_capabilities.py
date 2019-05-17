#!/usr/bin/env python

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

import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_desired_capabilities(app):
    # desired_caps = {
    #     'deviceName': 'iPhone Simulator',
    #     'platformName': 'iOS',
    #     'app': PATH('../../apps/' + app),
    # }
    desired_caps = {
        "platformName": "iOS",
        "platformVersion": "12.2",
        "deviceName": "iPhone 6 ray",
        "automationName": "XCUITest",
        'app': PATH('../../apps/' + app),
        'uuid':'cede4602d5647926b9ae97e0153dd3489bfa2d82',
    }

    return desired_caps
