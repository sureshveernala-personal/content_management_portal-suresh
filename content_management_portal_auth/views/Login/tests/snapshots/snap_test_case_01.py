# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginAPITestCase::test_case status'] = 201

snapshots['TestCase01LoginAPITestCase::test_case body'] = {
    'access_token': 'PbWOleEjL99tOoUPfPY3NR2rA9mphk',
    'expires_in': '2337-04-20 02:14:03.493790',
    'refresh_token': 'sFajX39Y1Ye9AjKUd2zKn3Yf4syryD',
    'user_id': 1
}

snapshots['TestCase01LoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '159',
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

snapshots['TestCase01LoginAPITestCase::test_case 1'] = {
    'access_token': 'PbWOleEjL99tOoUPfPY3NR2rA9mphk',
    'expires_in': '2337-04-20 02:14:03.493790',
    'refresh_token': 'sFajX39Y1Ye9AjKUd2zKn3Yf4syryD',
    'user_id': 1
}
