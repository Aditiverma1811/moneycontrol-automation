import requests

def test_get_stock():
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"symbol":"ITC.NS","region":"IN"}
    headers = {
        "X-RapidAPI-Key": "b9880a473amsh15b60b74de66fbdp16ce50jsn66cd1c2729da",
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    assert response.status_code == 200
    assert "price" in response.json()

def test_post_dummy():
    url = "https://httpbin.org/post"
    payload = {"stock":"ITC","action":"add"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["json"]["stock"] == "ITC"