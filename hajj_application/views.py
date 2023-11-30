from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from hajj_application.forms import HajjApplicationForm
from hajj_application.models import HajjApplication
from package_making.models import Package, PackageHotelItem


# ================================HajjApplication=============================
class CreateHajjApplication(CreateView):
    template_name = 'hajj_application/add.html'
    model = HajjApplication
    form_class = HajjApplicationForm
    success_url = "/hajj_application/list"

    # @method_decorator(privilegesRequired)
    # def dispatch(self, *args, **kwargs):
    #     return super(CreateCategory, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateHajjApplication, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class ListHajjApplication(LoginRequiredMixin, ListView):
    template_name = 'hajj_application/list.html'
    context_object_name = 'hajj_application_items'
    model = HajjApplication

    # @method_decorator(privilegesRequired)
    # def dispatch(self, *args, **kwargs):
    #     return super(GetCategories, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(ListHajjApplication, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListHajjApplication, self).get_context_data(**kwargs)
        # context['tot_item_groups'] = ItemGroup.objects.count()
        # context['tot_sub_item_group'] = ItemGroup.objects.filter(parent__item_group__item_group=True).count()
        return context


#
#
class UpdateHajjApplication(UpdateView):
    model = HajjApplication
    form_class = HajjApplicationForm
    template_name = 'hajj_application/update.html'
    success_url = '/hajj_application/list'

    # @method_decorator(privilegesRequired)
    # def dispatch(self, *args, **kwargs):
    #     return super(UpdateCategory, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(UpdateHajjApplication, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class DetailHajjApplication(DetailView):
    model = HajjApplication
    context_object_name = 'hajj_application_item'
    template_name = 'hajj_application/detail.html'


class DeleteHajjApplication(DeleteView):
    model = HajjApplication
    success_url = '/hajj_application/list'


# ================================HajjApplication End============================
# ================================Fetching Package Information============================
class GetPackage(View):
    def serialize_package(self, package):
        return {
            'id': package.id,
            'package_name': package.name,
            'package_type': package.package_type,
            'maktab': package.maktab,
            'country': package.country_name,
            'package_days': package.package_days,
            'package_sale_price_sar': package.package_sale_price_sar,
            'exchange_rate': package.exchange_rate,
            'package_sale_price_pkr': package.package_sale_price_pkr,
            'terms_and_conditions': package.terms_and_conditions,
        }

    def package_hotel_items(self, package_item):
        return {
            'id': package_item.id,
            'city_name': package_item.city_name,
            'hotel_name': package_item.hotel_name,
            'room_type_name': package_item.room_type_name,
            'check_in_date': package_item.check_in_date,
            'check_out_date': package_item.check_out_date,
            'meal': package_item.meal,
            'nights': package_item.nights,
            'cost': package_item.cost,
            'currency': package_item.currency
        }

    def get(self, request, *args, **kwargs):
        package_id = request.GET.get('package_id')

        if package_id:
            # Fetching a single object
            package = get_object_or_404(Package, id=package_id)
            serialized_package = self.serialize_package(package)
            package_hotel_items = PackageHotelItem.objects.filter(package=package)
            serialized_package_hotel_items = [self.package_hotel_items(package_item) for package_item in package_hotel_items]
            return JsonResponse({'package': serialized_package, 'success': True, 'package_items': serialized_package_hotel_items})
        return JsonResponse({'success': False})
