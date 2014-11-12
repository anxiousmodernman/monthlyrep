

class BaseReport(object):

    def __init__(self):
        self.name = 'Hello'


class ProfileCompletion(BaseReport):

    def __init__(self):
        super(ProfileCompletion, self).__init__()


class OpenClick(BaseReport):

    def __init__(self):
        super(OpenClick, self).__init__()


class Unsubscribes(BaseReport):

    def __init__(self, data):
        super(Unsubscribes, self).__init__()
        self._data = data
