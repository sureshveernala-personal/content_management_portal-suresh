# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateCodingQuestionStatementAPITestCase::test_case status'] = 400

snapshots['TestCase01CreateCodingQuestionStatementAPITestCase::test_case body'] = {
    'problem_description': {
        'content_type': [
            '"Text" is not a valid choice.'
        ]
    }
}

snapshots['TestCase01CreateCodingQuestionStatementAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '76',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
