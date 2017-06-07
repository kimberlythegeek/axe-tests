# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import json
import os
import pytest
import time


class TestAccessibility:

    @pytest.mark.nondestructive
    def test_run_axe(self, base_url, selenium):
        """Run axe against base_url and verify JSON output."""

        selenium.get(base_url)

        # Include axe-core API
        selenium.execute_script(open('./src/axe.min.js').read())
        # Script to run axe API against page
        selenium.execute_script(open('./src/script.js').read())

        # Delay while JavaScript runs
        time.sleep(1)
        # Get JSON results
        result = selenium.find_element_by_id('axe-result').text
        # --- Is there a better way to pass data from JS to python? --- #

        # Create file to JSON response from axe
        file = open('result.json', 'w+')
        # Parse JSON
        parsed = json.loads(result)
        # And pretty-print to file
        file.write(json.dumps(parsed, indent=4))
        file.close

        assert os.stat("./result.json").st_size != 0, "JSON output not received."

    @pytest.mark.nondestructive
    def test_accessibility_critical_violations(self):
        """Assert that no critical violatons are found."""
        # List to hold info about critical violations
        criticalViolations = []
        data = json.load(open('./result.json'))
        # Iterate through violations
        for item in data['violations']:
            # Find all critical violations
            if item['impact'] == 'critical':
                # Add description to list
                criticalViolations.append(item)

        # Assert that no critical violations are found
        assert len(criticalViolations) == 0, 'Critical Failures found'

# --- Is there a better way to assert against a list of objects? --- #
