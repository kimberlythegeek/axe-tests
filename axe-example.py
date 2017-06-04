# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

# Runs axe-core API against a page, and outputs JSON results to a file.

from selenium import webdriver
import time
import json

# Create new instance of Firefox driver
driver = webdriver.Firefox()

# Go to a page
driver.get('http://www.google.com')

# Include axe-core API
driver.execute_script(open('./src/axe.min.js').read())
# Script to run axe API against page
driver.execute_script(open('./src/script.js').read())

# Delay while JavaScript runs
time.sleep(1)
# Get JSON results
# --- Is there a better way to pass data from JS to python? --- #
result = driver.find_element_by_id('axe-result').text

# Create file to hold results
file = open('result.json', 'w+')
# Parse JSON
parsed = json.loads(result)
# And pretty-print to file
file.write(json.dumps(parsed, indent=4))
file.close

# Close Firefox
driver.quit()
