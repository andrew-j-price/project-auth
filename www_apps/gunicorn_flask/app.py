from flask import Flask, jsonify
import os
import platform
import pwd
import socket

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello from Flask via Gunicorn!</h1>"


@application.route("/host", strict_slashes=False, methods=["GET"])
def host():
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


if __name__ == "__main__":
    application.run(host='0.0.0.0')
