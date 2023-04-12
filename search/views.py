import json

import requests
from django.shortcuts import render

from .forms import SearchForm


def search(request):
    """perform music search from iTunes API
    and return JSON response

    Args:
        request (text): enter any text

    Returns:
        JSON: response of search query
    """
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            response = requests.get(
                f"https://itunes.apple.com/search?term={query}&media=music&entity=album",
            )
            results = json.dumps(response.json()["results"])
            return render(request, "search_results.html", {"results": results})
    else:
        form = SearchForm()
    return render(request, "search/search.html", {"form": form})
