
from django.urls import path
from . views import index 
# ,add_expenses,edit_expenses,delete_expenses,search_expenses,expenses_summary,summary_status,expenses_csv
# ,add_expenses,edit_expenses,delete_expenses,search_expenses,expenses_summary,summary_status,expenses_csv
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', index,name='admins'),
    # path('add-ticket/', add_ticket,name='add-ticket'),
    # path('edit-ticket/<int:id>', edit_ticket,name='edit-ticket'),
    # path('delete-expenses/<int:id>', delete_expenses,name='delete-expenses'),
    # path('search-expenses/',csrf_exempt( search_expenses),name='search-expenses'),
    # path('summary-expenses/', expenses_summary,name='summary-expenses'),
    # path('summary_status-expenses/',csrf_exempt( summary_status),name='summary_status'),
    # path('csv-tickets/', tickets_csv,name='csv-tickets'),
]