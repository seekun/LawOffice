from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/seekun/LawOffice.git"
# GIT_REPO = "https://gitee.com/seekun/ahu.git"

env.user = 'ubuntu'
env.password = 'sk13008587515'
env.hosts = ['www.seekun.cn']
# env.hosts = ['193.112.97.157']
env.port = '22'

def deploy():
    source_folder = '/home/ubuntu/sites/demo.seekun.cn/LawOffice'

    run('cd %s && git pull' % source_folder )
    run("""
        cd {} &&
        ../env/bin/python manage.py collectstatic --noinput &&
        ../env/bin/python manage.py makemigrations&&
        ../env/bin/python manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.seekun.cn')
    sudo('service nginx reload')


def restart():
    sudo('restart gunicorn-demo.seekun.cn')
    sudo('service nginx reload')

# python3 users/compressImage.py
# 启动图片压缩脚本
#         ../env/bin/python3 users/compressImage.py &&