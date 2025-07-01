import os
import importlib.util
import base64

class PayloadManager:
    def __init__(self, payload_dir="modules/payloads"):
        self.payload_dir = os.path.abspath(payload_dir)
        self.payloads = {}

    def load_payloads(self):
        for root, _, files in os.walk(self.payload_dir):
            for file in files:
                if file.endswith(".py") and file != "manager.py" and not file.startswith("__"):
                    name = file[:-3]
                    path = os.path.join(root, file)
                    module = self._load_module(name, path)
                    if module and hasattr(module, "generate"):
                        self.payloads[name] = module

    def _load_module(self, name, path):
        try:
            spec = importlib.util.spec_from_file_location(name, path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            # Minimal hata yakalama, sessiz geç
            return None

    def list_payloads(self):
        return list(self.payloads.keys())

    def generate(self, name, **kwargs):
        module = self.payloads.get(name)
        if not module:
            return None
        return module.generate(**kwargs)

    def encode(self, code, method="base64"):
        if method == "base64":
            encoded = base64.b64encode(code.encode()).decode()
            return f"import base64\nexec(base64.b64decode('{encoded}').decode())"
        return code

    def save(self, code, filename="intpayload.py"):
        with open(filename, "w") as f:
            f.write(code)
        return filename