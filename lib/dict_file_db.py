#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# linjx@chuchujie.com
# QQ: 279370682
# 2018/7/4 17:56
import json


class FileDict(dict):
    """
        文件db
    """

    def __init__(self, path=None, name=None, **kwargs):
        super(FileDict, self).__init__(**kwargs)
        self._path = "/tmp" if path is None else path
        self._name = ".file.db" if name is None else "%s.db" % name
        self._read()

    def _read(self):
        """
            加载数据文件
        :return:
        """
        with open("%s/%s" % (self._path, self._name), "r") as df:
            _d = json.load(df)
            assert isinstance(_d, dict), u"db文件(%s/%s)数据格式不正确" % (self._path, self._name)
            self.update(_d)

    def save(self):
        """
            保存到数据文件
        :return:
        """
        with open("%s/%s" % (self._path, self._name), "w") as df:
            _d_text = json.dumps(self)
            df.write(_d_text)
