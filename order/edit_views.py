from django.views.generic import *
from django.core.urlresolvers import resolve
from .models import *
from django.http import *

class GenericCreate(CreateView):
    def form_valid(self, form):
        model_inst = form.save(commit=False)
        print("#############")
        if resolve(self.request.path_info).url_name == 'order_create':
            print("@@@@@@@@@@@@@@")
            model_inst.user = self.request.user
        model_inst.save()
        return HttpResponseRedirect(self.get_success_url())

    def __init__(self, **kwargs):
        super(GenericCreate, self).__init__( **kwargs)


class GenericUpdate(UpdateView):

    def __init__(self, **kwargs):
        super(GenericUpdate, self).__init__(**kwargs)


class GenericList(ListView):

    def get_queryset(self):
        qs = super(GenericList, self).get_queryset()
        if resolve(self.request.path_info).url_name == 'order_list':

            qs = qs.filter(user = self.request.user)
            print(qs)
        return qs

    def __init__(self, **kwargs):
        super(GenericList, self).__init__(**kwargs)


class GenericDetail(DetailView):

    def __init__(self, **kwargs):
        super(GenericDetail, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(GenericDetail, self).get_context_data(**kwargs)

        if resolve(self.request.path_info).url_name == 'order_detail':
            print(context)
            context['bids'] = Bids.objects.filter()
        return context