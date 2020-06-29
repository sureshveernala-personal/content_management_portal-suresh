# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01SwapCodingQuestionHintsAPITestCase::test_case status'] = 400

snapshots['TestCase01SwapCodingQuestionHintsAPITestCase::test_case body'] = {
    'first_hint': [
        'This field is required.'
    ],
    'second_hint': [
        'This field is required.'
    ]
}

snapshots['TestCase01SwapCodingQuestionHintsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '84',
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
