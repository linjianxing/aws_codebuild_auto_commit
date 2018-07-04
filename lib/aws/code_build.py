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
    _resource = "codebuild"

    def __init__(self):
        super(CodeBuild, self).__init__()

    def start_build(self, project=None, tag=None):
        """
            启动一个构建任务
        :param project:
        :return:
        """
        ret = self._client.start_build(projectName=project,
                                       environmentVariablesOverride=[
                                           {
                                               'name': "TAG",
                                               'value': tag,
                                               'type': 'PLAINTEXT'
                                           },
                                       ])

        print "Create new build %s，%s :%s" % (project, str(tag), str(ret))
        return {
            "build_id": ret["build"]["id"],
            "status": ret["build"]["buildStatus"]
        }

    def get_build_info(self, build_id=None):
        """
            查询构建任务信息
        :param build_id:
        :return:
        """
        builds = self._client.batch_get_builds(ids=[build_id])
        assert len(builds) == 1, "No build be find ! %s" % build_id
        return {
            "build_id": builds["builds"][0]["id"],
            "status": builds["builds"][0]["buildStatus"]
        }
