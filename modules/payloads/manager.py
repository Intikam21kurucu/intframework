import os
import importlib.util
import base64
import inspect
from lib.int4.handler.base import HandlerBase  # Handler sınıf kontrolü için

class PayloadManager:
    def __init__(self, payload_dir="modules/payloads"):
        self.payload_dir = os.path.abspath(payload_dir)
        self.payloads = {}   # klasik generate() payloadları
        self.handlers = {}   # nesne tabanlı handler'lar

    def load_payloads(self):
        for root, _, files in os.walk(self.payload_dir):
            for file in files:
                if file.endswith(".py") and file != "manager.py" and not file.startswith("__"):
                    name = file[:-3]
                    path = os.path.join(root, file)
                    module = self._load_module(name, path)
                    if not module:
                        continue

                    # Klasik payload mu? (generate fonksiyonu içeriyor mu)
                    if hasattr(module, "generate"):
                        self.payloads[name] = module

                    # Handler tabanlı payload mı? (HandlerBase subclass içeriyor mu)
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if inspect.isclass(attr) and issubclass(attr, HandlerBase) and attr is not HandlerBase:
                            self.handlers[name] = attr
                            break  # Bir handler sınıfı yeterli

    def _load_module(self, name, path):
        try:
            spec = importlib.util.spec_from_file_location(name, path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None  # Hatalı modül sessizce geçilir

    def list_payloads(self):
        return list(self.payloads.keys()) + list(self.handlers.keys())

    def generate(self, name, **kwargs):
        module = self.payloads.get(name)
        if not module:
            return None
        return module.generate(**kwargs)

    def has_handler(self, name):
        return name in self.handlers

    def get_handler(self, name):
        return self.handlers.get(name)

    def encode(self, code, method="base64"):
        if method == "base64":
            encoded = base64.b64encode(code.encode()).decode()
            return f"import base64\nexec(base64.b64decode('{encoded}').decode())"
        return code

    def save(self, code, filename="intpayload.py"):
        with open(filename, "w") as f:
            f.write(code)
        return filename