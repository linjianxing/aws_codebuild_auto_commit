#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# 2017.11.5

import boto3


class Aws(object):
    def __init__(self):
        self._session = boto3.Session()
        self._client = None
