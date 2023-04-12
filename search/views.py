import requests
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import SearchForm


def search(request):
    """perform music search from iTunes API
    and return JSON response

    Args:
        request (text): enter the text

    Returns:
        JSON: response of search query
    """
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            return redirect("search_results", query=query)
    else:
        form = SearchForm()
    return render(request, "search/search.html", {"form": form})


def search_results(request, query):
    response = requests.get(
        f"https://itunes.apple.com/search?term={query}&media=music&entity=album",
    )
    results = response.json()["results"]
    # results = json.dumps(response.json()["results"])
    paginator = Paginator(results, 13)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "search/search_results.html", {"page_obj": page_obj})
