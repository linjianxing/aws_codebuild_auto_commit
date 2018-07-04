#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# linjx@chuchujie.com
# QQ: 279370682
# 2018/7/3 20:05

from lib.github import GitHub


def auto_build():
    """
        自动提交CodeBuild任务构建
    :return:
    """
    eos_github = GitHub()
