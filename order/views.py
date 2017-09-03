from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


def bid_create(request, pk):
    request.user = User.objects.get(pk=1)
    bid = request.POST.get('amount')
    try:
        user_bid = Bids.objects.get(user=request.user, order_id=pk)
        user_bid.amount = bid
        user_bid.save()
    except ObjectDoesNotExist:
        Bids.objects.create(user=request.user, order_id=pk, amount=bid)

    return redirect('order_detail', pk=pk)


