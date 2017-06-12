# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


class AccessiblityRule:
    """
    A rule for designing accessible websites and web applications.

    :param json_result: Dictionary of the axe-core JSON result for this rule.
    :param fail: True if this rule is violated.
    :type json_result: dict
    :type fail: bool

    id (str): Identifier used by axe-core for this rule.
    fail (bool): True if this rule is violated.
    description (str): A brief description of the acessibility rule.
    help (str): A helpful message on why this rule failed.
    helpUrl (str): URL reference for this accessibility rule.
    nodes (list): A list of dictionaries containing relevant HTML elements.
    """
    def __init__(self, json_result):
        self.id = json_result['id']
        self.description = json_result['description']
        self.help = json_result['help']
        self.helpUrl = json_result['helpUrl']
        self.nodes = json_result['nodes']
