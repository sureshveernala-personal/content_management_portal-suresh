# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCodingQuestionsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetCodingQuestionsAPITestCase::test_case body'] = {
    'limit': 846,
    'offset': 960,
    'questions_list': [
    ],
    'total_questions': 0
}

snapshots['TestCase01GetCodingQuestionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '73',
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
