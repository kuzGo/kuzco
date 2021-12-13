
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.db.models.functions import Lower


def reviews_total(request):

    reviews = Review.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sorting = request.GET['sort']
            sort = sorting
            if sorting == 'username':
                reviews = reviews.annotate(
                    lower_username=Lower('username__username'))
            if sorting == 'watches':
                sorting = 'watches__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sorting = f'-{sorting}'
            reviews = reviews.order_by(sorting)

    current_sorting = f'{sort}_{direction}'

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


@login_required
def add_reviews(request):
    """ Add reviews of the watches """

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.username = request.user
            review.save()
            messages.success(request, "Your review has" +
                             "been submitted successfully")
        else:
            messages.error(request, 'Sorry, we could not' +
                           'submit you review at this time')
    else:
        form = ReviewForm()

    template = 'reviews/add_reviews.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
