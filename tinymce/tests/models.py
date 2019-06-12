
from django.db import models
from .. import models as tinymce_models


class TestModel(models.Model):
    foobar = tinymce_models.HTMLField()
