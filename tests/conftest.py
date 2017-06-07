from datetime import datetime
from py.xml import html
import pytest
import json


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(0, html.th('Time', class_='sortable time', col='time'))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    # load pytest-html plguin
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    # add docstring to 'description' column
    report.description = str(item.function.__doc__)

    extra = getattr(report, 'extra', [])
    xfail = hasattr(report, 'wasxfail')
    if (report.skipped and xfail) or (report.failed and not xfail):
        # only add additional html on failure
        data = json.load(open('result.json'))
        # add the violations JSON object to h
        extra.append(pytest_html.extras.text(json.dumps(data['violations'], indent=4)))
    report.extra = extra
