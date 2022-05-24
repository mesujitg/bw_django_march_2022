from broadway.settings import MEDIA_URL
from categories.models import Category


def all_categories(request):
    categories = Category.objects.all()
    return {'categories': categories, 'MEDIA_URL': MEDIA_URL}
