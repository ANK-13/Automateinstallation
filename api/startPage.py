import flask


def getFile(path):
    return flask.send_from_directory('angular',path)