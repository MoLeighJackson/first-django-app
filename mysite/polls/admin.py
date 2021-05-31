from django.contrib import admin

from .models import Question

# tell admin that question objects have an admin interface
# by registering question django knows that it should be
# displayed on the admin index page
admin.site.register(Question)
