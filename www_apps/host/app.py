import os
import platform
import pwd
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
@app.route("/host", strict_slashes=False, methods=["GET"])
def route_host():
    response = {
        'host_hostname': str(socket.gethostname()),
        'host_ip': str(socket.gethostbyname(socket.gethostname())),
        'os_distribution': str(platform.linux_distribution(full_distribution_name=1)),  # noqa:E501
        'os_platform': str(platform.platform()),
        'os_system': str(platform.system()),
        'python_version': str(platform.python_version()),
        'user_id': str(os.getuid()),
        'user_name': str(pwd.getpwuid(int(os.getuid())).pw_name),
        'pid_parent': str(os.getppid()),
        'pid_self': str(os.getpid())
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
