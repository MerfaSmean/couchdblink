import pycouchdb
from pycouchdb.exceptions import NotFound

from .config import CRED_URL


def get_couchdb_connection(cred_url=""):
    if not cred_url:
        # print("using default CRED_URL")
        cred_url = CRED_URL
    return pycouchdb.Server(cred_url, authmethod="session")


def close(server):
    """
    Shortcut for closing a server's resource session -
    added after finding that unittests on
    get_couchdb_connection() were raising
    `ResourceWarning: unclosed <ssl.SSLSocket ...` warnings
    :param server: pycouchdb.Server
    :return:
    """
    server.resource.session.close()


def get_make_db(server, db_name):
    try:
        return server.database(db_name)
    except NotFound:
        server.create(db_name)
        return get_make_db(server, db_name)
