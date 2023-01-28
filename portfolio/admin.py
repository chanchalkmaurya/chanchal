from django.contrib import admin
from portfolio.models import send_a_query, newsletteremail, project_details


# Register your models here.
admin.site.register(send_a_query)
admin.site.register(newsletteremail)
admin.site.register(project_details)


