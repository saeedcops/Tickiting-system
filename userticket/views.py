import datetime
import json

from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .models import Category, UserTicket
from userpreferences.models import UserPreferences
from django.core.paginator import Paginator
import csv
import json


# @login_required(login_url='/oauth2/login')
def index(request):
    print("User: ",str(request.user))
    # print("META: ",str(request.META))
    print("body: ",str(request.body))
    # print("Json: ",json.loads(request.body))
    

    # tickets = UserTicket.objects.filter(user=request.user)
    # exists = UserPreferences.objects.filter(user=request.user).exists()
    # currency = "USD"
    # if exists:
    #     currency = UserPreferences.objects.get(user=request.user).currency

    # print(str(list(currency))) , 'currency': currency
    # paginator = Paginator(tickets, 6)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number), {'tickets': tickets, 'page_obj': page_obj}
    return render(request, 'tickets/home.html')


# @login_required(login_url='/auth/login')
# def search_expenses(request):
#     if request.method == 'POST':
#         search_str = json.loads(request.body).get('searchText')
#         expenses = Expense.objects.filter(amount__istartswith=search_str, owner=request.user) | \
#                    Expense.objects.filter(category__istartswith=search_str, owner=request.user) | \
#                    Expense.objects.filter(description__icontains=search_str, owner=request.user) | \
#                    Expense.objects.filter(date__istartswith=search_str, owner=request.user)
#         data = expenses.values()
#         return JsonResponse(list(data), safe=False)


# @login_required(login_url='/auth/login')
# def delete_expenses(request, id):
#     Expense.objects.get(pk=id).delete()
#     messages.error(request, "Expense, Deleted")
#     return redirect('expenses')


# @login_required(login_url='/auth/login')
# def edit_expenses(request, id):
#     expense = Expense.objects.get(pk=id)
#     category = Category.objects.all()
#     if request.method == 'GET':
#         return render(request, 'expenses/edit_expenses.html', {'expenses': expense, 'category': category})

#     if request.method == 'POST':
#         amount = request.POST['amount']
#         description = request.POST['description']
#         cat = request.POST['category']
#         date = request.POST['date']
#         if not amount:
#             messages.error(request, "Please, enter amount")
#             return render(request, 'expenses/edit_expenses.html', {'category': category, 'expenses': request.POST})
#         if not description:
#             messages.error(request, "Please, enter description")
#             return render(request, 'expenses/edit_expenses.html', {'category': category, 'expenses': request.POST})

#         if not date:
#             date = now()

#         expense.amount = amount
#         expense.description = description
#         expense.category = cat
#         expense.date = date
#         expense.save()

#         messages.success(request, "Expenses Edited Successfully")
#         return redirect('expenses')
#     return render(request, 'expenses/edit_expenses.html', {'category': category, 'expenses': request.POST})


# @login_required(login_url='/auth/login')
# def add_expenses(request):
#     category = Category.objects.all()

#     if request.method == 'POST':
#         amount = request.POST['amount']
#         description = request.POST['description']
#         cat = request.POST['category']
#         date = request.POST['date']
#         if not amount:
#             messages.error(request, "Please, enter amount")
#             return render(request, 'expenses/add_expenses.html', {'category': category, 'values': request.POST})
#         if not description:
#             messages.error(request, "Please, enter description")
#             return render(request, 'expenses/add_expenses.html', {'category': category, 'values': request.POST})

#         if not date:
#             date = now()
#         Expense.objects.create(amount=amount, description=description, category=cat,
#                                date=date, owner=request.user)

#         messages.success(request, "Expenses Added Successfully")
#         return redirect('expenses')
#     return render(request, 'expenses/add_expenses.html', {'category': category})


# @login_required(login_url='/auth/login')
# def expenses_summary(request):
#     return render(request, 'expenses/summary_expenses.html')


# @login_required(login_url='/auth/login')
# def summary_status(request):
#     month_ago = now() - datetime.timedelta(days=30)
#     data = {}
#     expenses = Expense.objects.filter(owner=request.user, date__gte=month_ago, date__lte=now())

#     def get_category(expense):
#         return expense.category

#     category_list = list(set(map(get_category, expenses)))

#     def get_amount(filter_expenses):
#         amount = 0
#         for ex in filter_expenses:
#             amount += ex.amount
#         return amount

#     for category in category_list:
#         filter_expenses = expenses.filter(category=category)
#         data[category] = get_amount(filter_expenses)

#     return JsonResponse(data, safe=False)


# @login_required(login_url='/auth/login')
# def expenses_csv(request):
#     expenses = Expense.objects.filter(owner=request.user)
#     response = HttpResponse(content_type="text/csv")
#     response['Content-Disposition'] = 'attachment; filename=Expenses' + str(now()) + '.csv'
#     writer = csv.writer(response)
#     writer.writerow(['Amount', 'Description', 'Category', 'Date'])

#     for ex in expenses:
#         writer.writerow([ex.amount, ex.description, ex.category, ex.date])

#     return response
