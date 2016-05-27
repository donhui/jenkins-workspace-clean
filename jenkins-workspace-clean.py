# -*- coding: utf-8 -*-
import os
import shutil
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

    for dirpath, dirnames, filenames in os.walk(jenkins_workspace_path):
        if dirpath == jenkins_workspace_path:
            for dirname in dirnames:
                jenkins_job_name = dirname
                # 如果job被删除，则清理相应的workspace
                if not jenkins_instance.has_job(jenkins_job_name):
                    logger.info("removing workspace dir of job:%s" % dirname)
                    shutil.rmtree(os.path.join(dirpath, dirname))


if __name__ == "__main__":
    clean_workspace()