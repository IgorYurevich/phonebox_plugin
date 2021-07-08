from django.contrib import admin
from .models import Number, NumbersRange


@admin.register(Number)
class NumPlanAdmin(admin.ModelAdmin):
    list_display = ("number", "tenant", "description", "provider", "forward_to")

@admin.register(NumbersRange)
class RangesAdmin(admin.ModelAdmin):
    list_display = ("start", "end", "tenant", "description", "provider")
