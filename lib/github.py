#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# linjx@chuchujie.com
# QQ: 279370682
# 2018/7/3 20:12

import requests


class GitHub(object):
    """
        github 操作类
    """
    _owner = None
    _repo = None

    def __init__(self):
        pass

    def get_releases(self):
        """
            获取最新发布版本号
        :return:
        """
        ret = []
        latest_release_api_url = "https://api.github.com/repos/%s/%s/releases" % (self._owner, self._repo)
        result = requests.get(url=latest_release_api_url)
        data = result.json()
        for r in data:
            ret.append(
                {
                    "tag_name": r["tag_name"],
                    "created_at": r["created_at"]
                }
            )
        return ret

    def get_latest_release(self):
        """
            查询最新发布版本
        """
        releases = self.get_releases()
        latest_release = releases[0]

        for r in releases:
            if r["created_at"] > latest_release["created_at"]:
                latest_release = r

        return latest_release


class EOS_MainnetGitHub(GitHub):
    _owner = "EOS-Mainnet"
    _repo = "eos"

    def __init__(self):
        super(EOS_MainnetGitHub, self).__init__()
