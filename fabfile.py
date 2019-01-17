from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/seekun/LawOffice.git"
# GIT_REPO = "https://gitee.com/seekun/ahu.git"

env.user = 'ubuntu'
env.password = '7bRnLy^$^!sYSRMK'
env.hosts = ['www.tmsshikun.xyz']
# env.hosts = ['193.112.97.157']
env.port = '22'

def deploy():
    source_folder = '/home/ubuntu/sites/demo.tmsshikun.xyz/LawOffice'

    run('cd %s && git pull' % source_folder )
    run("""
        cd {} &&
        ../env/bin/python manage.py collectstatic --noinput &&
        ../env/bin/python manage.py makemigrations&&
        ../env/bin/python manage.py migrate --run-syncdb
        """.format(source_folder))
    sudo('restart gunicorn-demo.tmsshikun.xyz')
    sudo('service nginx reload')


def restart():
    sudo('restart gunicorn-demo.tmsshikun.xyz')
    sudo('service nginx reload')

# python3 users/compressImage.py
# 启动图片压缩脚本
#         ../env/bin/python3 users/compressImage.py &&