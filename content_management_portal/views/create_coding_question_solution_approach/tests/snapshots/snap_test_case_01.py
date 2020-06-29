# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateCodingQuestionSolutionApproachAPITestCase::test_case status'] = 404

snapshots['TestCase01CreateCodingQuestionSolutionApproachAPITestCase::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_QUESTION_ID',
    'response': 'Question id is not valid.'
}

snapshots['TestCase01CreateCodingQuestionSolutionApproachAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '103',
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
