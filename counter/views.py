import re
from django.shortcuts import render


def word_count_view(request):
    word_count = None
    text = ""
    words = ""

    if request.method == "POST":
        text = request.POST.get("text", "").strip()  # Get input and remove extra spaces
        words = re.split(r"[ -]+", text)  # Split by space or hyphen
        words = [word for word in words if word]  # Remove empty entries
        word_count = len(words)

    return render(request, "counter/counter.html", {"word_count": word_count, "text": text, "words": words})


def about(request):
    return render(request, 'counter/about.html')
