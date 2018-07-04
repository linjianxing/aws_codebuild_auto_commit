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
        self._db_file = "/".join([self._path, self._name])
        self._read()

    def __backup_db(self):
        """
            备份数据文件。
        :return:
        """
        import shutil
        shutil.copyfile(self._db_file, ".".join([self._db_file, "bak"]))

    def _read(self):
        """
            加载数据文件
        :return:
        """
        with open(self._db_file, "r") as df:
            _d = json.load(df)
            assert isinstance(_d, dict), u"db文件(%s)数据格式不正确" % self._db_file
            self.update(_d)

    def save(self):
        """
            保存到数据文件
        :return:
        """
        self.__backup_db()
        with open("%s/%s" % (self._path, self._name), "w") as df:
            _d_text = json.dumps(self)
            df.write(_d_text)

    def add_release(self, release=None, build_id=None):
        """
            添加一个release
        :param build_id:
        :param release:
        :return:
        """
        self[release] = {
            "build_id": build_id,
            "status": "IN_PROGRESS",
            "rebuild": 0,
            "the_end": False
        }
        print "Add release %s" % release
        self.save()

    def update_release(self, release=None, build_id=None, status=None, add_rebuild=False, the_end=False):
        """
            更新release信息。
        :param release:
        :param build_id:
        :param status:
        :param add_rebuild:
        :return:
        """
        print "Update release %s,%s,%s,%s,%s" % (release, build_id, status, add_rebuild, the_end)

        if build_id is not None:
            self[release]["build_id"] = build_id
        if status is not None:
            self[release]["status"] = status
        if add_rebuild:
            self[release]["rebuild"] += 1
        self[release]["the_end"] = the_end

        self.save()

    def is_build_success(self, release=None):
        """
            检查release是否构建成功。
        :param release:
        :return:
        """
        # 'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',

        return self[release]["status"] == "SUCCEEDED"

    def is_need_rebuild(self, release=None):
        """
            是否需要重新构建
        :param release:
        :return:
        """
        return self[release]["status"] in ("FAILED", "FAULT", "TIMED_OUT") and self[release]["retry"] < 3
