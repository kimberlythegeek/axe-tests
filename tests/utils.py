from accessibility_rule import AccessiblityRule


def parse_results(json):
    test_results = {}

    for item in json:
        rule = AccessiblityRule(item)
        test_results[item['id']] = rule

    return test_results
