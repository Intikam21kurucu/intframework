import re
import json
from typing import Dict, List

class IntelligenceAnalyzer:

    def __init__(self):
        self.training_data_path = "lib/ai_module/train_data.json"
        self.special_features = [
            "option_schema", "session_manager", "hasattr", "class", "def", "import",
            "config_manager", "set_option", "validate_required_options", "show_options", "main", "run", "exploit"
        ]

    def analyze_module_code(self, code: str) -> Dict:
        features = self.extract_features(code)
        score = self.score_module(features)
        training_data = self.generate_training_data(features, score)
        self.save_training_data(training_data)
        return {
            "features": features,
            "score": score,
            "training_data": training_data
        }

    def extract_features(self, code: str) -> Dict:
        features = {
            "classes": re.findall(r"class\s+(\w+)", code),
            "functions": re.findall(r"def\s+(\w+)", code),
            "comments_tr": re.findall(r"#\s*(?!test)([^\n]*[ğüşıöçĞÜŞİÖÇ]+[^\n]*)", code, re.IGNORECASE),
            "comments_en": re.findall(r"#\s*(?!test)([^\n]*[a-zA-Z]+[^\n]*)", code),
            "uses_option_schema": "option_schema" in code,
            "uses_session_manager": "session_manager" in code or "SessionManager" in code,
            "has_config": "config_manager" in code or "load_schema_from_module" in code,
            "intikam21_compatible": any(keyword in code for keyword in ["option_schema", "set_option", "SessionManager", "load_context", "validate_required_options"]),
            "has_test_tag": "# test" in code,
        }
        return features

    def score_module(self, features: Dict) -> int:
        score = 0
        if features["uses_option_schema"]:
            score += 20
        if features["uses_session_manager"]:
            score += 20
        if features["has_config"]:
            score += 15
        if features["intikam21_compatible"]:
            score += 25
        if features["comments_tr"]:
            score += 5
        if features["comments_en"]:
            score += 5
        if features["has_test_tag"]:
            score += 2
        if features["classes"]:
            score += len(features["classes"]) * 3
        if features["functions"]:
            score += len(features["functions"]) * 2
        return min(score, 100)

    def generate_training_data(self, features: Dict, score: int) -> Dict:
        return {
            "label": "intikam21_module",
            "score": score,
            "features": features
        }

    def save_training_data(self, data: Dict):
        try:
            with open(self.training_data_path, "r") as f:
                existing = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing = []

        existing.append(data)
        with open(self.training_data_path, "w") as f:
            json.dump(existing, f, indent=4)