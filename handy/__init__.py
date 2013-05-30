import urlparse


class Environment(dict):

    def set(self, name, val):
        self[name] = val

    def get_uri(self, name):
        obj = urlparse.urlparse(self[name])

        # Our internal aliases
        obj.host = obj.hostname
        obj.user = obj.username
        obj.relative_path = obj.path

        # Cleaning up the relative_path variable
        while obj.relative_path[0] == '/':
            obj.relative_path = obj.relative_path[1:]
        return obj
