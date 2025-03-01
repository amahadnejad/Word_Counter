from django.shortcuts import render


def word_counter(request):
    return render(request, 'counter/counter.html')
