# -*- coding: utf-8 -*-

import threading

class SessionManager:
    """
    SessionManager, aktif oturumları yönetir. 
    Oturum ekleme, kaldırma, listeleme gibi temel işlevler sunar.
    """

    def __init__(self, framework=None):
        """
        SessionManager başlatılırken framework parametresi alabilir.
        Args:
            framework (object): Framework referansı (isteğe bağlıdır).
        """
        self.framework = framework
        self._sessions = {}
        self._lock = threading.RLock()

    def add_session(self, session_id, session_data):
        """
        Yeni bir oturum ekler.
        Args:
            session_id (str or int): Oturumun benzersiz kimliği.
            session_data (dict or object): Oturumla ilgili veriler.
        """
        with self._lock:
            self._sessions[session_id] = session_data

    def remove_session(self, session_id):
        """
        Var olan bir oturumu kaldırır.
        Args:
            session_id (str or int): Kaldırılacak oturumun kimliği.
        """
        with self._lock:
            if session_id in self._sessions:
                del self._sessions[session_id]

    def get_session(self, session_id):
        """
        Belirli bir oturumu getirir.
        Args:
            session_id (str or int): İstenen oturum kimliği.
        Returns:
            dict or object: İlgili oturum verisi veya None.
        """
        with self._lock:
            return self._sessions.get(session_id)

    def list_sessions(self):
        """
        Mevcut tüm oturumları listeler.
        Returns:
            list: Tüm oturum kimliklerinin listesi.
        """
        with self._lock:
            return list(self._sessions.keys())

    def count_sessions(self):
        """
        Aktif oturum sayısını döndürür.
        Returns:
            int: Oturum sayısı.
        """
        with self._lock:
            return len(self._sessions)

    def clear_sessions(self):
        """
        Tüm oturumları temizler.
        """
        with self._lock:
            self._sessions.clear()

    def has_session(self, session_id):
        """
        Belirli bir oturumun var olup olmadığını kontrol eder.
        Args:
            session_id (str or int): Kontrol edilecek oturum kimliği.
        Returns:
            bool: True -> Varsa, False -> Yoksa
        """
        with self._lock:
            return session_id in self._sessions

    def __len__(self):
        """
        SessionManager içindeki oturum sayısını döndürür.
        Returns:
            int: Oturum sayısı.
        """
        return self.count_sessions()

    def __iter__(self):
        """
        SessionManager içindeki oturumlar üzerinde iterasyon yapılmasını sağlar.
        """
        with self._lock:
            return iter(self._sessions.items())

    def __getitem__(self, session_id):
        """
        Bir oturuma doğrudan erişim sağlar. 
        Örnek: manager[session_id]
        """
        with self._lock:
            return self._sessions[session_id]

    def __setitem__(self, session_id, session_data):
        """
        Bir oturumu doğrudan ekler veya günceller.
        """
        with self._lock:
            self._sessions[session_id] = session_data

    def __delitem__(self, session_id):
        """
        Bir oturumu doğrudan siler.
        """
        with self._lock:
            del self._sessions[session_id]

    def __contains__(self, session_id):
        """
        Belirli bir oturumun SessionManager içinde olup olmadığını kontrol eder.
        """
        with self._lock:
            return session_id in self._sessions