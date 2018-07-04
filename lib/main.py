#!/usr/bin/env python2.7
# coding=utf-8
# 林建星
# linjx@chuchujie.com
# QQ: 279370682
# 2018/7/3 20:05

from lib.github import EOS_MainnetGitHub
from lib.dict_file_db import FileDict
from aws.code_build import CodeBuild

CodeBuild_Project = "build_eos_docker"


# 'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',


def auto_build():
    """
        自动提交CodeBuild任务构建
    :return:
    """
    git_hub = EOS_MainnetGitHub()
    db = FileDict()
    builder = CodeBuild()

    releases = git_hub.get_releases()

    for release in releases:
        tag_name = release["tag_name"]
        code_build_tag = "MainnetEOS-%s" % tag_name


        # 新建构建任务
        if tag_name not in db.keys():
            build = builder.start_build(project=CodeBuild_Project, tag=code_build_tag)
            db.add_release(release=tag_name, build_id=build["build_id"])
            continue

        # 跳过已结束版本
        if db[tag_name]["the_end"]:
            continue

        build = builder.get_build_info(build_id=db[tag_name]["build_id"])
        db.update_release(release=tag_name, status=build["status"])

        # 修改构建成功的版本状态。
        if db.is_build_success(release=tag_name):
            db.update_release(release=tag_name, the_end=True)
            continue

        if db.is_need_rebuild(release=tag_name):
            print "Re build %s" % tag_name
            build = builder.start_build(project=CodeBuild_Project, tag=code_build_tag)
            db.update_release(release=tag_name, build_id=build["build_id"], status=build["status"], add_rebuild=True)
            continue

        # 联系构建n次都不成功时，执行以下操作：

        print "Release %s build failed." % tag_name

        # 结束本版本操作。
        db.update_release(release=tag_name, the_end=True)
