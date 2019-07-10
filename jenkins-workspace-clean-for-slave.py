# -*- coding: utf-8 -*-
import os
import datetime
import time
import logging

from jenkinsapi.jenkins import Jenkins

from settings import JENKINS_SETTINGS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


def get_jenkins_instance():
    jenkins_url = JENKINS_SETTINGS.get('jenkins_url')
    jenkins_username = JENKINS_SETTINGS.get('jenkins_username')
    jenkins_password = JENKINS_SETTINGS.get('jenkins_password')
    return Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)


def clean_workspace():
    jenkins_instance = get_jenkins_instance()

    jenkins_workspace_path = JENKINS_SETTINGS.get('jenkins_workspace_path')

    for dir_path, dir_names, file_names in os.walk(jenkins_workspace_path):
        if dir_path == jenkins_workspace_path:
            for dir_name in dir_names:
                jenkins_job_name = dir_name
                jenkins_job_workspace_path = os.path.join(dir_path, dir_name)
                # 如果 job 被删除，则清理相应的 workspace
                if not jenkins_instance.has_job(jenkins_job_name):
                    logger.info("removing workspace dir of deleted job:%s" % dir_name)
                    os.system("sudo rm -rf " + jenkins_job_workspace_path)
                # 如果 job 存在，最多保留 workspace 10天
                else:
                    # 获得当前日期
                    today = datetime.date.today()
                    # 获得历史日期，本例中为10天之前
                    ten_days_ago = datetime.timedelta(days=-10)
                    # least_day 保留时间
                    least_day = today + ten_days_ago
                    modify_time = time.localtime((os.path.getmtime(jenkins_job_workspace_path)))
                    year = modify_time[0]
                    month = modify_time[1]
                    day = modify_time[2]
                    # 将日期初始化为 date 对象
                    file_date = datetime.date(year, month, day)
                    # 比较日期，删除较早的目录
                    if least_day > file_date:
                        logger.info("removing workspace dir of existed job:%s" % dir_name)
                        os.system("sudo rm -rf " + jenkins_job_workspace_path)


if __name__ == "__main__":
    clean_workspace()
