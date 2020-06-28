from product.models import Category

def nav_data(request):
    context = dict()
    context['categories'] = Category.objects.filter(
        status = "True"
    ).order_by('title')

    return context