#coding=utf-8
import os
import shutil
import datetime
import time
#获得当前日期
today = datetime.date.today()
#获得历史日期，本例中为15天之前
twoweek= datetime.timedelta(days=-15)
leastday = today + twoweek


jenkins_jobs_path = "/var/lib/jenkins/jobs/"

for dirpath, dirnames, filenames in os.walk(jenkins_jobs_path):
    if dirpath == jenkins_jobs_path:
        for dirname in dirnames:
            jenkins_job_name = dirname
            jenkins_job_workspace_path = jenkins_jobs_path + jenkins_job_name + "/workspace"

            if os.path.exists(jenkins_job_workspace_path):
                modifytime = time.localtime((os.path.getmtime(jenkins_job_workspace_path)))
                year = modifytime[0]
                month = modifytime[1]
                day = modifytime[2]
                #将日期初始化为date对象
                filedate = datetime.date(year, month, day)
                #比较日期，删除较早的目录
                if (leastday > filedate):
                        shutil.rmtree(jenkins_job_workspace_path)
                        print("delete old dir:" + jenkins_job_workspace_path)
