from django.shortcuts import render


def cart(request, username):
    return render(request, 'cart/layout.html', {
        'username': username,
    })
