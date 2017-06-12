# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from accessibility_rule import AccessiblityRule


def parse_results(json):
    test_results = {}

    for item in json:
        rule = AccessiblityRule(item)
        test_results[item['id']] = rule

    return test_results
