from django.contrib import admin
from .models import User, ModelFile, StyleImage

admin.site.register(User)
admin.site.register(ModelFile)
admin.site.register(StyleImage)

