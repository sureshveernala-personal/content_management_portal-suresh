# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04CreateCodingQuestionHintAPITestCase::test_case status'] = 201

snapshots['TestCase04CreateCodingQuestionHintAPITestCase::test_case body'] = {
    'hint': {
        'description': {
            'content': 'string',
            'content_type': 'TEXT'
        },
        'hint_id': 1,
        'hint_number': 1,
        'title': 'string'
    },
    'question_id': '1'
}

snapshots['TestCase04CreateCodingQuestionHintAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '143',
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
