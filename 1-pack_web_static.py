#!/usr/bin/python3
""" Script Fabric that generates a .tgz from the contents of web_static """
from datetime import datetime
from fabric.api import local


def do_pack():
    """
        Return the archive path if archive has been correctly
        gernerated.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = local("tar -czvf version/web_static_{}.tgz /web_static"
                    .format(date))

    if archive.succeeded:
        return archive
    else:
        return None
