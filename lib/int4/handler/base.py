import abc

class HandlerBase(abc.ABC):
    option_schema = {}

    def __init__(self):
        self.options = {}
        self.session_manager = None
        self._running = False

    def set_session_manager(self, session_manager):
        self.session_manager = session_manager

    def set_options(self, options: dict):
        self.options = options

    def get_option(self, key):
        return self.options.get(key)

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        self._running = False