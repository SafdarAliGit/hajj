import math
from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Count
from django.shortcuts import render, redirect

# from companies.models import Till
# from customers.models import Customer
# from pos.middleware.GlobalUserMiddleware import get_company
# from products.models import Product, Stock
# from purchases.models import Purchasem
# from sales.models import Salem
# from sorders.models import Sorderm
# from suppliers.models import Supplier

#
# def create_company(f):
#     def wrap(request, *args, **kwargs):
#         try:
#             if request.user.role == 0 and request.user.company is not None:
#                 pass
#         except ObjectDoesNotExist:
#             return redirect("/company/add_company_starter/")
#         return f(request, *args, **kwargs)
#
#     wrap.__doc__ = f.__doc__
#     wrap.__name__ = f.__name__
#     return wrap


# @create_company
def dashboard(request):
    # c = get_company()
    # context = {}
    # try:
    #     till = Till.objects.filter(company=c, assigned_to=request.user.pk).values('id')[0]['id']
    # except:
    #     till = None
    # if till is not None:
    #     context['totsinvoices_unpaid'] = Salem.objects.filter(company=c, till_id=till,
    #                                                           status=0).count()
    #     context['totsamount_unpaid'] = Salem.objects.filter(company=c, till_id=till,
    #                                                         status=0).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_partial'] = Salem.objects.filter(company=c, till_id=till,
    #                                                            status=1).count()
    #     context['totsamount_partial'] = Salem.objects.filter(company=c, till_id=till,
    #                                                          status=1).aggregate(totamount=Sum('invoice_balance'))
    #     context['totsinvoices_paid'] = Salem.objects.filter(company=c, till_id=till,
    #                                                         status=2).count()
    #     context['totsamount_paid'] = Salem.objects.filter(company=c, till_id=till,
    #                                                       status=2).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_overdue'] = Salem.objects.filter(company=c, till_id=till,
    #                                                            status=3).count()
    #     context['totsamount_overdue'] = Salem.objects.filter(company=c, till_id=till,
    #                                                          status=3).aggregate(totamount=Sum('amount'))
    #     context['tot_inv'] = Salem.objects.filter(company=c, till_id=till).count()
    #     context['tot_amt'] = Salem.objects.filter(company=c, till_id=till).aggregate(
    #         totamount=Sum('amount'))
    #
    #     context['totsinvoices_processing'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                                 status=0).count()
    #     context['totsamount_processing'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                               status=0).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_dispatched'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                                 status=1).count()
    #     context['totsamount_dispatched'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                               status=1).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_delivered'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                                status=2).count()
    #     context['totsamount_delivered'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                              status=2).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_finished'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                               status=3).count()
    #     context['totsamount_finished'] = Sorderm.objects.filter(company=c, till_id=till,
    #                                                             status=3).aggregate(totamount=Sum('amount'))
    #     context['tot_inv_o'] = Sorderm.objects.filter(company=c, till_id=till).count()
    #     context['tot_amt_o'] = Sorderm.objects.filter(company=c, till_id=till).aggregate(
    #         totamount=Sum('amount'))
    #     # stock at locations graph
    #     stock_at_lcoations = Stock.objects.filter(company=c, qty__gte=1).values('location__name').annotate(
    #         stock_at_loc=Count('id'))
    #     stock_at_array = []
    #     for s in range(len(stock_at_lcoations)):
    #         obj = {'name': '', 'y': 0}
    #         obj['name'] = str(stock_at_lcoations[s]['location__name'])
    #         obj['y'] = stock_at_lcoations[s]['stock_at_loc']
    #         stock_at_array.append(obj)
    #     context['stock_array'] = stock_at_array
    #     # sale at different tills
    #
    #     sale_at_tills = Salem.objects.filter(company=c).values('till__name').annotate(tot_sale_at_tills=Sum('amount'))
    #     sale_at_array = []
    #     for s in range(len(sale_at_tills)):
    #         obj_sale = {'name': '', 'y': 0}
    #         obj_sale['name'] = str(sale_at_tills[s]['till__name'])
    #         obj_sale['y'] = math.floor(sale_at_tills[s]['tot_sale_at_tills'])
    #         sale_at_array.append(obj_sale)
    #     context['sale_at_till_array'] = sale_at_array
    #     # sale at different tills current day
    #     today = date.today()
    #     sale_at_tills_current = Salem.objects.filter(company=c, cdate__year=today.year, cdate__month=today.month,
    #                                                  cdate__day=today.day).values('till__name').annotate(
    #         tot_sale_at_tills=Sum('amount'))
    #     sale_at_array_current = []
    #     for s in range(len(sale_at_tills_current)):
    #         obj_sale_current = {'name': '', 'y': 0}
    #         obj_sale_current['name'] = str(sale_at_tills_current[s]['till__name'])
    #         obj_sale_current['y'] = math.floor(sale_at_tills_current[s]['tot_sale_at_tills'])
    #         sale_at_array_current.append(obj_sale_current)
    #     context['sale_at_till_array_current'] = sale_at_array_current
    #     # instock out stock count
    #     in_stock = Stock.objects.filter(company=c).exclude(qty=0).values('product_id').distinct().count()
    #     tot_items = Product.objects.filter(company=c).values('id').count()
    #     out_stock = tot_items - in_stock
    #
    #     context['in_stock'] = in_stock
    #     context['out_stock'] = out_stock
    # else:
    #     context['totsinvoices_unpaid'] = Salem.objects.filter(company=c,
    #                                                           status=0).count()
    #     context['totsamount_unpaid'] = Salem.objects.filter(company=c,
    #                                                         status=0).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_partial'] = Salem.objects.filter(company=c,
    #                                                            status=1).count()
    #     context['totsamount_partial'] = Salem.objects.filter(company=c,
    #                                                          status=1).aggregate(totamount=Sum('invoice_balance'))
    #     context['totsinvoices_paid'] = Salem.objects.filter(company=c,
    #                                                         status=2).count()
    #     context['totsamount_paid'] = Salem.objects.filter(company=c,
    #                                                       status=2).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_overdue'] = Salem.objects.filter(company=c,
    #                                                            status=3).count()
    #     context['totsamount_overdue'] = Salem.objects.filter(company=c,
    #                                                          status=3).aggregate(totamount=Sum('amount'))
    #     context['tot_inv'] = Salem.objects.filter(company=c).count()
    #     context['tot_amt'] = Salem.objects.filter(company=c).aggregate(
    #         totamount=Sum('amount'))
    #
    #     context['totsinvoices_processing'] = Sorderm.objects.filter(company=c,
    #                                                                 status=0).count()
    #     context['totsamount_processing'] = Sorderm.objects.filter(company=c,
    #                                                               status=0).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_dispatched'] = Sorderm.objects.filter(company=c,
    #                                                                 status=1).count()
    #     context['totsamount_dispatched'] = Sorderm.objects.filter(company=c,
    #                                                               status=1).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_delivered'] = Sorderm.objects.filter(company=c,
    #                                                                status=2).count()
    #     context['totsamount_delivered'] = Sorderm.objects.filter(company=c,
    #                                                              status=2).aggregate(totamount=Sum('amount'))
    #     context['totsinvoices_finished'] = Sorderm.objects.filter(company=c,
    #                                                               status=3).count()
    #     context['totsamount_finished'] = Sorderm.objects.filter(company=c,
    #                                                             status=3).aggregate(totamount=Sum('amount'))
    #     context['tot_inv_o'] = Sorderm.objects.filter(company=c).count()
    #     context['tot_amt_o'] = Sorderm.objects.filter(company=c).aggregate(
    #         totamount=Sum('amount'))
    #     stock_at_lcoations = Stock.objects.filter(company=c, qty__gte=1).values('location__name').annotate(
    #         stock_at_loc=Count('id'))
    #     stock_at_array = []
    #     for s in range(len(stock_at_lcoations)):
    #         obj = {'name': '', 'y': 0}
    #         obj['name'] = str(stock_at_lcoations[s]['location__name'])
    #         obj['y'] = stock_at_lcoations[s]['stock_at_loc']
    #         stock_at_array.append(obj)
    #     context['stock_array'] = stock_at_array
    #     # sale at different tills
    #
    #     sale_at_tills = Salem.objects.filter(company=c).values('till__name').annotate(tot_sale_at_tills=Sum('amount'))
    #     sale_at_array = []
    #     for s in range(len(sale_at_tills)):
    #         obj_sale = {'name': '', 'y': 0}
    #         obj_sale['name'] = str(sale_at_tills[s]['till__name'])
    #         obj_sale['y'] = math.floor(sale_at_tills[s]['tot_sale_at_tills'])
    #         sale_at_array.append(obj_sale)
    #     context['sale_at_till_array'] = sale_at_array
    #
    #     # sale at different tills current day
    #     today = date.today()
    #     sale_at_tills_current = Salem.objects.filter(company=c, cdate__year=today.year, cdate__month=today.month,
    #                                                  cdate__day=today.day).values('till__name').annotate(
    #         tot_sale_at_tills=Sum('amount'))
    #     sale_at_array_current = []
    #     for s in range(len(sale_at_tills_current)):
    #         obj_sale_current = {'name': '', 'y': 0}
    #         obj_sale_current['name'] = str(sale_at_tills_current[s]['till__name'])
    #         obj_sale_current['y'] = math.floor(sale_at_tills_current[s]['tot_sale_at_tills'])
    #         sale_at_array_current.append(obj_sale_current)
    #     context['sale_at_till_array_current'] = sale_at_array_current
    #     # instock out stock count
    #     in_stock = Stock.objects.filter(company=c).exclude(qty=0).values('product_id').distinct().count()
    #     tot_items = Product.objects.filter(company=c).values('id').count()
    #     out_stock = tot_items - in_stock
    #
    #     context['in_stock'] = in_stock
    #     context['out_stock'] = out_stock
    #
    # context['totcustomers'] = Customer.objects.filter(user=request.user, status=0).count()
    # context['totcustomers_inactive'] = Customer.objects.filter(user=request.user, status=1).count()
    # context['totsuppliers'] = Supplier.objects.filter(user=request.user, status=0).count()
    # context['totsuppliers_inactive'] = Supplier.objects.filter(user=request.user, status=1).count()
    # context['totpinvoices'] = Purchasem.objects.filter(user=request.user).count()
    # context['totpamount'] = Purchasem.objects.filter(user=request.user).aggregate(totamount=Sum('amount'))
    # context['totproducts'] = Product.objects.filter(user=request.user, status=0).count()
    # context['totproducts_inactive'] = Product.objects.filter(user=request.user, status=1).count()
    # context['totsorders'] = Sorderm.objects.filter(user=request.user).count()
    # context['totsamount'] = Sorderm.objects.filter(user=request.user, ).aggregate(totamount=Sum('amount'))
    return render(request, 'dashboard/dashboard.html')

