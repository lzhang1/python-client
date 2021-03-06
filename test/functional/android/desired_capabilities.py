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
    #emulator setting
    # desired_caps = {
    #     'platformName': 'Android',
    #     'platformVersion': '5.1',
    #     'deviceName': '192.168.56.102:5555',
    #     'app': PATH('../../apps/' + app),
    #     'newCommandTimeout': 240
    # }
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.4.2',
        'deviceName': '127.0.0.1:62001',
        'app': PATH('../../apps/' + app),
        'newCommandTimeout': 240
    }

    # desired_caps = {
    #     'platformName': 'Android',
    #     'platformVersion': '8.1',
    #     'deviceName': 'emulator-5554',
    #     'app': PATH('../../apps/' + app),
    #     'newCommandTimeout': 240
    # }
    return desired_caps
