import sys
import os

from dulwich import log_utils
from dulwich.server import DictBackend, TCPGitServer
from dulwich.mysqlrepo import MysqlRepo


def main(argv=sys.argv):
    """Entry point for starting a TCP git server."""
    MysqlRepo.setup(os.environ['DB_URL'])
    log_utils.default_logging_config()
    repos = MysqlRepo.list_repos()
    backendDict = { '/%s' % repo: MysqlRepo.open(repo) for repo in repos }
    backend = DictBackend(backendDict)
    server = TCPGitServer(backend, '0.0.0.0')
    server.serve_forever()


if __name__ == '__main__':
    main()