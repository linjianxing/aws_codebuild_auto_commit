#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# 2017.11.5

import boto3


class Aws(object):
    _resource = None

    def __init__(self):
        self._client = boto3.client(self._resource)
