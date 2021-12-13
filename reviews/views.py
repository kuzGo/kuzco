
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Review
from .forms import ReviewForm


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


@login_required
def update_reviews(request, review_id):

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users" +
                       "can update reviews")
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully")
            return redirect(reverse('update_reviews'))
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid.")
            return redirect(reverse('reviews_total'))
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.name}')

    template = 'reviews/update_review.html'

    context = {
        'form': form,
        'review': review,
    }
    return render(request, template, context)


@login_required
def remove_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser or review.username == request.user:
        review.delete()
        messages.success(request, "Review has been removed" +
                         "successfuly")
    else:
        messages.error(request, 'Sorry, we could not' +
                       'delete you review at this time')
        return redirect(reverse('reviews_total'))
