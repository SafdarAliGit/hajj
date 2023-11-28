from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from hajj_application.forms import HajjApplicationForm
from hajj_application.models import HajjApplication


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
