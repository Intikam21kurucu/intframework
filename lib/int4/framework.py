# -*- coding: utf-8 -*-

import threading
import hashlib
import os
import time

class RexSocketSsl:
    cert_provider = None

class CertProvider:
    def __init__(self):
        self.cert = "DefaultSSL"

class FeatureManager:
    _instance = None

    def __init__(self):
        self.features = {}

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = FeatureManager()
        return cls._instance

    def load_config(self):
        self.features = {
            'DNS': False
        }

    def enabled(self, feature_name):
        return self.features.get(feature_name, False)

class EventDispatcher:
    def __init__(self, framework):
        self.framework = framework
        self.subscribers = {
            'exploit': [],
            'session': [],
            'general': [],
            'db': [],
            'ui': []
        }

    def add_exploit_subscriber(self, subscriber):
        self.subscribers['exploit'].append(subscriber)

    def add_session_subscriber(self, subscriber):
        self.subscribers['session'].append(subscriber)

    def add_general_subscriber(self, subscriber):
        self.subscribers['general'].append(subscriber)

    def add_db_subscriber(self, subscriber):
        self.subscribers['db'].append(subscriber)

    def add_ui_subscriber(self, subscriber):
        self.subscribers['ui'].append(subscriber)

    def notify(self, category, event_data):
        for subscriber in self.subscribers.get(category, []):
            subscriber.report_event(event_data)

class DataStore(dict):
    pass

class JobContainer(dict):
    def add_job(self, job_id, job_func):
        self[job_id] = job_func

    def remove_job(self, job_id):
        if job_id in self:
            del self[job_id]

class Analyze:
    def __init__(self, framework):
        self.framework = framework

    def basic_scan(self):
        return "Analyze complete: No issues detected."

class PluginManager(dict):
    def __init__(self, framework):
        super().__init__()
        self.framework = framework

    def load_plugin(self, name, plugin):
        self[name] = plugin

    def unload_plugin(self, name):
        if name in self:
            del self[name]

class SessionManager(dict):
    def __init__(self, framework):
        super().__init__()
        self.framework = framework

    def add_session(self, session_id, session_info):
        self[session_id] = session_info

    def remove_session(self, session_id):
        if session_id in self:
            del self[session_id]

class ThreadManager(dict):
    def __init__(self, framework):
        super().__init__()
        self.framework = framework

    def start_thread(self, target, name=None):
        thread = threading.Thread(target=target, name=name)
        thread.start()
        self[thread.ident] = thread
        return thread

    def kill_thread(self, thread_id):
        if thread_id in self:
            # Python'da thread öldürme desteklenmez. İsimden çıkarılması yeterli.
            del self[thread_id]

class DBManager:
    def __init__(self, framework):
        self.framework = framework
        self.database = {}

    def init_db(self, options=None):
        self.database['initialized'] = True

class DataProxy:
    def __init__(self, options):
        self.options = options
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def query(self, key):
        return self.data.get(key)

class Framework:
    MAJOR = 6
    MINOR = 3
    PATCH = 46
    PRERELEASE = ''
    VERSION = f"{MAJOR}.{MINOR}.{PATCH}{PRERELEASE}"
    REVISION = "$Revision$"

    class Offspring:
        def __init__(self):
            self.framework = None

    def __init__(self, options=None):
        if options is None:
            options = {}
        self.options = options
        self.lock = threading.RLock()

        self.features = FeatureManager.instance()
        self.features.load_config()

        self.events = EventDispatcher(self)
        self.datastore = DataStore()
        self.jobs = JobContainer()
        self.analyze = Analyze(self)
        self.plugins = PluginManager(self)

        self._sessions = None
        self._threads = None
        self._db = None

        RexSocketSsl.cert_provider = CertProvider()

        subscriber = FrameworkEventSubscriber(self)
        self.events.add_exploit_subscriber(subscriber)
        self.events.add_session_subscriber(subscriber)
        self.events.add_general_subscriber(subscriber)
        self.events.add_db_subscriber(subscriber)
        self.events.add_ui_subscriber(subscriber)

    def inspect(self):
        return f"<Framework ({len(self.sessions)} sessions, {len(self.jobs)} jobs, {len(self.plugins)} plugins)>"

    @property
    def version(self):
        return self.VERSION

    @property
    def db(self):
        with self.lock:
            if self._db is None:
                self._db = self.get_db()
            return self._db

    @property
    def sessions(self):
        with self.lock:
            if self._sessions is None:
                self._sessions = SessionManager(self)
            return self._sessions

    @property
    def threads(self):
        with self.lock:
            if self._threads is None:
                self._threads = ThreadManager(self)
            return self._threads

    def threads_initialized(self):
        return self._threads is not None

    def search(self, search_string):
        result = []
        for sid, session in self.sessions.items():
            if search_string in str(session):
                result.append((sid, session))
        return result

    def eicar_corrupted(self):
        try:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "eicar.com"))
            if not os.path.exists(path):
                return True
            with open(path, "rb") as f:
                data = f.read()
            return hashlib.sha1(data).hexdigest() != "3395856ce81f2b7382dee72602f798b642f14140"
        except Exception:
            return True

    def get_db(self):
        if not self.options.get('DisableDatabase', False):
            db_manager = DBManager(self)
            self.options['db_manager'] = db_manager
            if not self.options.get('SkipDatabaseInit', False):
                db_manager.init_db(self.options)
        return DataProxy(self.options)

class FrameworkEventSubscriber(Framework.Offspring):
    def __init__(self, framework):
        super().__init__()
        self.framework = framework

    def report_event(self, data):
        if self.framework.db:
            self.framework.db.insert(str(time.time()), data)

    def module_event(self, name, instance, opts=None):
        if opts is None:
            opts = {}
        if self.framework.db:
            event = {
                'workspace': self.framework.db,
                'name': name,
                'username': getattr(instance, 'owner', None),
                'info': {
                    'module_name': getattr(instance, 'fullname', None),
                    'module_uuid': getattr(instance, 'uuid', None)
                }
            }
            event['info'].update(opts)
            self.report_event(event)

    def on_module_run(self, instance):
        opts = {'datastore': getattr(instance, 'datastore', {})}
        self.module_event('module_run', instance, opts)