

class BaseDetector:
    def __init__(self, url_model):
        self.url_model = url_model
        self._load_model()

    def _load_model(self):
        return NotImplementedError()


class CollageDetector(BaseDetector):
    def __init__(self):
        url_model = ''
        super(CollageDetector, self).__init__(url_model=url_model)

    def _load_model(self):
        pass


class QualityClassify(BaseDetector):
    def __init__(self):
        url_model = ''
        super(QualityClassify, self).__init__(url_model=url_model)

    def _load_model(self):
        pass