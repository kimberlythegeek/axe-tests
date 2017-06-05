# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.firefox.com')
driver.execute_script(open("./src/aria-highlighter.js").read())
