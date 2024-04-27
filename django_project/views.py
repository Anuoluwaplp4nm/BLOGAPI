import requests
from django.shortcuts import render


def home(request):
  #USING APIs
  response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
  data = response.json()
  result = data['meals']

  #response2 = requests.get('https://api.puppydeveloper.com/food')
  #data2 = response2.json()
  #result2 = data2['meals']

  return render(request, 'templates/index.html', {
      'result': result,
  })
