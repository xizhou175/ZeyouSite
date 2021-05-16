from django.contrib import admin

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    fields = ["name", "gender", "identity", "date_to_add"]
