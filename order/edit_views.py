from django.views.generic import *
from django.core.urlresolvers import resolve
from .models import *

class GenericCreate(CreateView):

    def __init__(self, **kwargs):
        super(GenericCreate, self).__init__( **kwargs)


class GenericUpdate(UpdateView):

    def __init__(self, **kwargs):
        super(GenericUpdate, self).__init__(**kwargs)


class GenericList(UpdateView):

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