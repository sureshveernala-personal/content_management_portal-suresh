# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateCodingQuestionCleanSolutionsAPITestCase::test_case status'] = 400

snapshots['TestCase03CreateCodingQuestionCleanSolutionsAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'CLEAN_SOLUTION_NOT_BELONG_TO_QUESTION',
    'response': 'Clean Solution id not belong to question.'
}

snapshots['TestCase03CreateCodingQuestionCleanSolutionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '137',
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
