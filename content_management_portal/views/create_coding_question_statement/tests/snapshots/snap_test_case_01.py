# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateCodingQuestionStatementAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateCodingQuestionStatementAPITestCase::test_case body'] = {
    'problem_description': {
        'content': 'string',
        'content_type': 'TEXT'
    },
    'question_id': 1,
    'short_text': 'string'
}

snapshots['TestCase01CreateCodingQuestionStatementAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '112',
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
