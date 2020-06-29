# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_mything return_value'] = 2

snapshots['test_addition_when_both_positive return_value'] = 3

snapshots['test_addition_when_both_negative return_value'] = -3

snapshots['test_addition_of_negative_and_positive return_value'] = -1
