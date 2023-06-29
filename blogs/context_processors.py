from blogs.models import Category
from blogs.models import SocialLink


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)



def get_social_links(request):
    links = SocialLink.objects.all()
    return dict(links=links)