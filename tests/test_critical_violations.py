# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import json
import pytest
# import conftest


class TestCriticalViolations:

    @pytest.mark.nondestructive
    def test_accessibility_critical_violations(self):
        """ Assert that no critical violations are found. """
        # List to hold info about critical violations
        criticalViolations = []
        data = json.load(open('./result.json'))
        # Iterate through violations
        for item in data['violations']:
            # Find all critical violations
            if item['impact'] == 'critical':
                # Add description to list
                criticalViolations.append(item['help'])

        # Assert that no critical violations are found
        assert len(criticalViolations) == 0, 'Critical Failures found'

# --- Is there a better way to assert against a list of objects? --- #
