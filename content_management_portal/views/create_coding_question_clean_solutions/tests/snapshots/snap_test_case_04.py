# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case status'] = 201

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case body'] = {
    'clean_solutions': [
        {
            'clean_solution_id': 1,
            'file_name': 'string',
            'language': 'PYTHON',
            'solution_content': 'string'
        },
        {
            'clean_solution_id': 4,
            'file_name': 'string',
            'language': 'PYTHON',
            'solution_content': 'string'
        }
    ],
    'question_id': '1'
}

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case header_params'] = {
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

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 1'] = 'PYTHON'

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 2'] = 'string'

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 3'] = 'string'

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 4'] = GenericRepr('FakeDatetime(2020, 1, 1, 0, 0)')

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 5'] = GenericRepr('<Question: Question object (1)>')

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 6'] = 'PYTHON'

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 7'] = 'string'

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 8'] = 'string'

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 9'] = GenericRepr('FakeDatetime(2020, 1, 1, 0, 0)')

snapshots['TestCase04CreateCodingQuestionCleanSolutionsAPITestCase::test_case 10'] = GenericRepr('<Question: Question object (1)>')
