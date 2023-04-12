import requests
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_search_view(client):
    # Test GET request
    response = client.get(reverse("search"))
    assert response.status_code == 200
    assertTemplateUsed(response, "search/search.html")

    # Test POST request with valid form data
    response = client.post(reverse("search"), {"query": "Micheal Jackson"})
    assert response.status_code == 302  # Redirect
    assert response.url == reverse("search_results", args=["Micheal Jackson"])

    # Test POST request with invalid form data
    response = client.post(reverse("search"), {"query": ""})
    assert response.status_code == 200
    assertTemplateUsed(response, "search/search.html")


def test_search_results_view(client):
    # Test request with valid query
    response = client.get(reverse("search_results", args=["Micheal Jackson"]))
    assert response.status_code == 200
    assertTemplateUsed(response, "search/search_results.html")

    # Test request with invalid query
    response = client.get(reverse("search_results", args=[""]))
    assert response.status_code == 404


def test_search_api_request():
    # Test valid api request
    response = requests.get("https://itunes.apple.com/search?term=Micheal+Taylor&media=music&entity=album")
    assert response.status_code == 200
    assert "results" in response.json()

    # Test invalid api request
    response = requests.get("https://itunes.apple.com/search?term=&media=music&entity=album")
    assert response.status_code == 200
    assert "results" in response.json()  # API returns results with empty query
