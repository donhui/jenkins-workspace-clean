# coding=utf-8
import os
import datetime
import time


if __name__ == "__main__":
    # 获得当前日期
    today = datetime.date.today()
    # 获得历史日期，本例中为15天之前
    two_weeks_ago = datetime.timedelta(days=-15)
    # least_day 保留时间
    least_day = today + two_weeks_ago

    jenkins_jobs_path = "/var/lib/jenkins/jobs/"

    for dir_path, dir_names, file_names in os.walk(jenkins_jobs_path):
        if dir_path == jenkins_jobs_path:
            for dir_name in dir_names:
                jenkins_job_name = dir_name
                jenkins_job_workspace_path = jenkins_jobs_path + jenkins_job_name + "/workspace"

                if os.path.exists(jenkins_job_workspace_path):
                    modify_time = time.localtime((os.path.getmtime(jenkins_job_workspace_path)))
                    year = modify_time[0]
                    month = modify_time[1]
                    day = modify_time[2]
                    # 将日期初始化为date对象
                    file_date = datetime.date(year, month, day)
                    # 比较日期，删除较早的目录
                    if least_day > file_date:
                        os.system("sudo rm -rf " + jenkins_job_workspace_path)
                        print("delete old dir:" + jenkins_job_workspace_path)
