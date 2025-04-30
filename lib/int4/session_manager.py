# -*- coding: utf-8 -*-
import threading

class SessionManager:
    """
    Core session manager module.

    Handles active sessions, session switching, and session-specific modules.
    """

    def __init__(self, framework=None):
        """
        Initialize the session manager.

        :param framework: Optional reference to the main framework object
        """
        self.framework = framework
        self._sessions = {}
        self._active_session = None
        self._lock = threading.RLock()

    def add_session(self, session_id, session_data):
        """
        Create a new session.

        :param session_id: Unique identifier for the session
        :param session_data: Arbitrary session data (e.g., client info)
        """
        with self._lock:
            self._sessions[session_id] = {
                "data": session_data,
                "modules": {}
            }
            if self._active_session is None:
                self._active_session = session_id

    def add_msession(self, session_id, module_name, module_instance):
        """
        Register a module into a specific session.

        :param session_id: Target session identifier
        :param module_name: String name of the module
        :param module_instance: Module object (must have `start()` or `run()`)
        """
        with self._lock:
            if session_id not in self._sessions:
                raise ValueError("Session does not exist: {}".format(session_id))
            self._sessions[session_id]["modules"][module_name] = module_instance

    def get_module_from_session(self, session_id, module_name):
        """
        Retrieve a specific module from a session.

        :param session_id: Session ID
        :param module_name: Name of module
        :return: Module instance or None
        """
        with self._lock:
            session = self._sessions.get(session_id)
            if session:
                return session["modules"].get(module_name)
            return None

    def switch_session(self, session_id):
        """
        Switch to a different session and start its modules.

        :param session_id: Target session ID
        :return: True if successful, False if session not found
        """
        with self._lock:
            if session_id in self._sessions:
                self._active_session = session_id
                session = self._sessions[session_id]
                for name, module in session["modules"].items():
                    try:
                        if hasattr(module, "start"):
                            module.start()
                        elif hasattr(module, "run"):
                            module.run()
                    except Exception:
                        pass
                return True
            return False

    def get_active_session(self):
        """
        Return the currently active session object.

        :return: Session dictionary or None
        """
        with self._lock:
            if self._active_session:
                return self._sessions.get(self._active_session)
            return None

    def get_active_session_id(self):
        """
        Return the active session ID.

        :return: Session ID string or None
        """
        with self._lock:
            return self._active_session

    def list_sessions(self):
        """
        List all session IDs.

        :return: List of session IDs
        """
        with self._lock:
            return list(self._sessions.keys())

    def list_modules_in_session(self, session_id):
        """
        List all module names in a specific session.

        :param session_id: Target session ID
        :return: List of module names
        """
        with self._lock:
            if session_id in self._sessions:
                return list(self._sessions[session_id]["modules"].keys())
            return []

    def remove_session(self, session_id):
        """
        Remove a session by ID.

        :param session_id: Session ID to remove
        """
        with self._lock:
            if session_id in self._sessions:
                del self._sessions[session_id]
                if self._active_session == session_id:
                    self._active_session = next(iter(self._sessions), None)

    def clear_sessions(self):
        """
        Remove all sessions.
        """
        with self._lock:
            self._sessions.clear()
            self._active_session = None

    def has_session(self, session_id):
        """
        Check if a session exists.

        :param session_id: Session ID
        :return: True if exists, False otherwise
        """
        with self._lock:
            return session_id in self._sessions

    def count_sessions(self):
        """
        Return the number of active sessions.

        :return: Integer session count
        """
        with self._lock:
            return len(self._sessions)

    def __len__(self):
        return self.count_sessions()

    def __iter__(self):
        with self._lock:
            return iter(self._sessions.items())

    def __getitem__(self, session_id):
        with self._lock:
            return self._sessions[session_id]

    def __setitem__(self, session_id, session_data):
        with self._lock:
            self._sessions[session_id] = session_data

    def __delitem__(self, session_id):
        with self._lock:
            del self._sessions[session_id]

    def __contains__(self, session_id):
        with self._lock:
            return session_id in self._sessions