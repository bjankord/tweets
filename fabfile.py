"""
Script for deploying code from my local laptop to a remote server.

Author: Kevin Burke <kev@inburke.com>

Usage:

    fab deploy
"""
from fabric.api import env, run, cd, local

env.hosts = ['kevinburke@kevinburke.webfactional.com']
env.user = 'kevinburke'
env.key_filename = '/Users/kevin/.ssh/webfaction_rsa'

def deploy():
    local("git checkout master; git push origin master")
    code_dir = '~/webapps/b/twitter'
    with cd(code_dir):
        run("git pull https://github.com/kevinburke/tweets.git")
