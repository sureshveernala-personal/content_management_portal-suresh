# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04CreateCodingQuestionTestCaseAPITestCase::test_case status'] = 201

snapshots['TestCase04CreateCodingQuestionTestCaseAPITestCase::test_case body'] = {
    'question_id': '1',
    'test_case': {
        'input': 'string',
        'is_hidden': True,
        'output': 'string',
        'score': 1,
        'test_case_id': 1,
        'test_case_number': 1
    }
}

snapshots['TestCase04CreateCodingQuestionTestCaseAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '147',
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