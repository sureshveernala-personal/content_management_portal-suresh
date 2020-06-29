# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04CreateCodingQuestionRoughSolutionsAPITestCase::test_case status'] = 201

snapshots['TestCase04CreateCodingQuestionRoughSolutionsAPITestCase::test_case body'] = {
    'question_id': '1',
    'rough_solutions': [
        {
            'file_name': 'string',
            'language': 'PYTHON',
            'rough_solution_id': 1,
            'solution_content': 'string'
        },
        {
            'file_name': 'string',
            'language': 'PYTHON',
            'rough_solution_id': 4,
            'solution_content': 'string'
        }
    ]
}

snapshots['TestCase04CreateCodingQuestionRoughSolutionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '243',
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
