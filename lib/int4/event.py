import threading  
import time  
import logging  
import traceback  
import sys  
from collections import defaultdict  
  
# Loglama yapılandırması  
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[logging.StreamHandler()])  
  
class EventDispatcher:  
    def __init__(self):  
        self.listeners = defaultdict(list)  # Dinleyiciler  
        self.event_log = []  # Olay geçmişi  
        self.event_data = defaultdict(list)  # Olaylara ait veriler  
        self.lock = threading.Lock()  # Eş zamanlılık için kilit  
  
    def add_listener(self, event, listener, priority=0):  
        """Dinleyiciyi ekler ve sıralar."""  
        if not callable(listener):  
            raise TypeError(f"Listener must be a callable function or method, got {type(listener)}")  
          
        with self.lock:  # Kilit kullanarak veri yarışını engelle  
            self.listeners[event].append({'listener': listener, 'priority': priority})  
            # Dinleyicileri önceliğe göre sıralama  
            self.listeners[event] = sorted(self.listeners[event], key=lambda x: x['priority'], reverse=True)  
          
        logging.info(f"Listener added for event: {event} with priority {priority}")  
  
    def remove_listener(self, event, listener):  
        """Dinleyiciyi kaldırır."""  
        with self.lock:  
            if event in self.listeners:  
                self.listeners[event] = [l for l in self.listeners[event] if l['listener'] != listener]  
                logging.info(f"Listener removed for event: {event}")  
  
    def dispatch(self, event, data=None):  
        """Olayı tetikler ve dinleyicileri çalıştırır."""  
        if event not in self.listeners:  
            logging.warning(f"No listeners for event: {event}")  
            return  
          
        # Olay verisini kaydet  
        timestamp = time.time()  
        self.event_log.append({'event': event, 'data': data, 'timestamp': timestamp})  
        self.event_data[event].append({'data': data, 'timestamp': timestamp})  
  
        logging.info(f"Dispatching event: {event} with data: {data}")  
  
        # Dinleyicileri sırayla çalıştır  
        threads = []  
        for listener_data in self.listeners[event]:  
            listener = listener_data['listener']  
            thread = threading.Thread(target=self._safe_listener_call, args=(listener, event, data))  
            threads.append(thread)  
            thread.start()  
  
        # Tüm thread'lerin bitmesini bekle  
        for thread in threads:  
            thread.join()  
  
    def _safe_listener_call(self, listener, event, data):  
        """Dinleyici çağırırken hata yönetimi ekleyelim."""  
        try:  
            listener(event, data)  
        except Exception as e:  
            logging.error(f"Error while executing listener for event: {event} - {e}")  
            logging.error(traceback.format_exc())  
            self.dispatch("error_occurred", {"event": event, "error": str(e)})  
  
    def get_event_log(self):  
        """Olay geçmişini döndürür."""  
        return self.event_log  
  
    def get_event_data(self, event):  
        """Belirli bir olayın verilerini döndürür."""  
        return self.event_data.get(event, [])  
  
    def clear_event_log(self):  
        """Olay geçmişini temizler."""  
        self.event_log.clear()  
  
    def notify_error(self, error_message):  
        """Hata bildirimi gönderir."""  
        logging.error(f"Critical error: {error_message}")  
        # Burada ayrıca bir bildirim sistemi entegre edilebilir (e-posta, SMS, vb.)  
  
    def event_summary(self):  
        """Olayların kısa bir özetini döndürür."""  
        summary = {}  
        for event, data_list in self.event_data.items():  
            summary[event] = len(data_list)  
        return summary  
  
  
# Dinleyiciler  
def log_event(event, data):  
    """Olayı loglar."""  
    logging.info(f"Event Triggered: {event} | Data: {data}")  
  
def send_notification(event, data):  
    """Bildirim gönderir."""  
    logging.info(f"Sending notification for event: {event} with data: {data}")  
  
def log_error(event, data):  
    """Hataları loglar."""  
    logging.error(f"Error occurred during {event} with data: {data}")  
  
"""  
# Event dispatcher'ı oluştur  
dispatcher = EventDispatcher()  
  
# Dinleyicileri ekle  
dispatcher.add_listener("module_execution", log_event, priority=1)  
dispatcher.add_listener("module_execution", send_notification, priority=2)  
dispatcher.add_listener("error_occurred", log_error, priority=1)  
  
# Modül çalıştırma fonksiyonu  
def run_module():  
    
    logging.info("Module started...")  
    try:  
        time.sleep(2)  # Modül çalışması simülasyonu  
        logging.info("Module completed.")  
        event_data = {"module_name": "exploit1", "status": "success"}  
        dispatcher.dispatch("module_execution", event_data)  
    except Exception as e:  
        dispatcher.dispatch("error_occurred", {"module_name": "exploit1", "error": str(e)})  
  
# Modülü çalıştır  
run_module()  
  
# Olay geçmişini al  
event_log = dispatcher.get_event_log()  
logging.info(f"Event Log: {event_log}")  
  
# Özet al  
summary = dispatcher.event_summary()  
logging.info(f"Event Summary: {summary}")  
"""