# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateCodingQuestionHintAPITestCase::test_case status'] = 404

snapshots['TestCase02CreateCodingQuestionHintAPITestCase::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_HINT_ID',
    'response': 'Hint id is not valid.'
}

snapshots['TestCase02CreateCodingQuestionHintAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '95',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
