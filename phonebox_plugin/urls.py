from django.urls import path
from . import views


urlpatterns = [
    # Numbers
    path("numbers/", views.NumberListView.as_view(), name="list_view"),
    path("numbers/<int:pk>/", views.NumberView.as_view(), name="number_view"),
    path("numbers/add_number/", views.NumberEditView.as_view(), name="add_number"),
    path("numbers/<int:pk>/edit/", views.NumberEditView.as_view(), name="number_edit"),
    path("numbers/number_bulk_edit", views.NumberBulkEditView.as_view(), name="number_bulk_edit"),
    path("numbers/<int:pk>/delete/", views.NumberDeleteView.as_view(), name="number_delete"),
    path("numbers/number_bulk_delete", views.NumberBulkDeleteView.as_view(), name="number_bulk_delete"),

    # NumbersRange
    path("ranges/", views.NumbersRangeListView.as_view(), name="range_list_view"),
    path("ranges/<int:pk>/", views.NumbersRangeView.as_view(), name="range_view"),
    path("ranges/add_range/", views.NumbersRangeEditView.as_view(), name="add_range"),
    path("ranges/<int:pk>/edit/", views.NumbersRangeEditView.as_view(), name="range_edit"),
    path("ranges/range_bulk_edit", views.NumbersRangeBulkEditView.as_view(), name="range_bulk_edit"),
    path("ranges/<int:pk>/delete/", views.NumbersRangeDeleteView.as_view(), name="range_delete"),
    path("ranges/range_bulk_delete", views.NumbersRangeBulkDeleteView.as_view(), name="range_bulk_delete"),
]   
