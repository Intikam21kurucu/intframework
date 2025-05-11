import os
import importlib.util
import base64

class PayloadManager:
    def __init__(self, payload_dir="modules/payloads"):
        self.payload_dir = payload_dir
        self.payloads = {}

    def load_payloads(self):
        for file in os.listdir(self.payload_dir):
            if file.endswith(".py") and file != "manager.py" and not file.startswith("__"):
                name = file[:-3]
                module = self._load_module(name)
                if hasattr(module, "generate"):
                    self.payloads[name] = module

    def _load_module(self, name):
        path = os.path.join(self.payload_dir, f"{name}.py")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception:
            pass
        return module

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