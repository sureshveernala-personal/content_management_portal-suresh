# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05CreateCodingQuestionSolutionApproachAPITestCase::test_case status'] = 201

snapshots['TestCase05CreateCodingQuestionSolutionApproachAPITestCase::test_case body'] = {
    'question_id': '1',
    'solution_approach': {
        'complexity_analysis': {
            'content': 'string',
            'content_type': 'TEXT'
        },
        'description': {
            'content': 'string',
            'content_type': 'TEXT'
        },
        'solution_approach_id': 1,
        'title': 'string'
    }
}

snapshots['TestCase05CreateCodingQuestionSolutionApproachAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '221',
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
