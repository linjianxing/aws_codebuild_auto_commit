#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# linjx@chuchujie.com
# QQ: 279370682
# 2018/7/4 18:11

from aws import Aws


class CodeBuild(Aws):
    """
        CodeBuild
    """

    def __init__(self):
        super(CodeBuild, self).__init__()
        self._client = self._session("codebuild")



