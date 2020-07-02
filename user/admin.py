from django.contrib import admin
from .models import (
    User, Department
)

models = [
      User
    , Department
]

for model in models:
    admin.site.register(model)

