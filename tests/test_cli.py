"""
command line interface tests
"""
import os
import httpretty


BOSTON_SAMPLE_HTML = 'tests/samples/boston.html'
EXPECTED_TEXT = "[Jan 13] java: JAVA Developer  (Boston near North and South Station)"


def _setup_mock_responses():
    httpretty.register_uri(httpretty.GET, 
                           "http://boston.craigslist.org/sof",
                           body=open(BOSTON_SAMPLE_HTML, 'r').read(),
                           content_type="text/html")


@httpretty.activate
def test_cli():
    _setup_mock_responses()

    text = os.popen("python xlist.py find -X sof -K java -C boston").read()
    assert(EXPECTED_TEXT in text)
