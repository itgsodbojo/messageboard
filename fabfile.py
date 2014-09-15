 # coding=utf-8
from fabric.api import task,sudo, warn_only, local
from fabric.colors import green,red
from fabtools.vagrant import vagrant_settings


@task
def install_couchdb():
    """install's and setup couchdb"""

    #ensure vagrant is up
    local("vagrant  up")

    with vagrant_settings():

        #install couchdb
        sudo('apt-get -y install couchdb')

        with warn_only():
            #stop couchdb
            sudo('stop couchdb')
            #set bind_address to 0.0.0.0
            sudo('sed -i "s/^bind_address = 127.0.0.1/bind_address = 0.0.0.0/g" /etc/couchdb/default.ini ')
            #start couchdb
            sudo('start couchdb')

        print red("\t⌘ + double click the link below")
        print green('\t "http://localhost:5984/_utils"')


