from transformers import pipeline


class IntentClassifier:
    def __init__(self, task_name: str, model_name: str, candidate_labels: list[str]):
        self._pipe = pipeline(task_name, model=model_name)
        self._candidate_labels = candidate_labels

    def get_intents(self, text) -> list:
        return self._pipe(text, self._candidate_labels)
