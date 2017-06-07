from datetime import datetime
from py.xml import html
import pytest

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(0, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function)

# import pytest
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     # if report.when == 'call':
#     # always add url to report
#     xfail = hasattr(report, 'wasxfail')
#     if (report.skipped and xfail) or (report.failed and not xfail):
#         # only add additional html on failure
#         extra.append(pytest_html.extras.json({            "impact": "critical",
#                     "description": "Ensures elements with ARIA roles have all required ARIA attributes",
#                     "tags": [
#                         "cat.aria",
#                         "wcag2a",
#                         "wcag411",
#                         "wcag412"
#                     ],
#                     "helpUrl": "https://dequeuniversity.com/rules/axe/2.2/aria-required-attr?application=axeAPI",
#                     "id": "aria-required-attr",
#                     "help": "Required ARIA attributes must be provided"
#                 }))
#     report.extra = extra
