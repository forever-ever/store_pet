from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import BlanketProduct, BedSetProduct


def index(request):
    return render(request, 'index.html', {})


def blanked_view(request):
    item = get_object_or_404(BlanketProduct, pk=1)
    print(item)
    context = {
    }
    return render(request, 'blanked.html', context)


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'blanked': BlanketProduct,
        'bed-set': BedSetProduct,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwargs = 'slug'
