from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'index.html')

def success_page(request):
  return HttpResponse("<h1>This is success page</h1>")

def context(request):
  text="""
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rerum, velit eveniet nihil, labore autem esse temporibus facere veniam atque, dolore unde. Enim, repudiandae nihil? Ipsum voluptatum accusantium numquam fugit dolorum deleniti soluta, nostrum, aperiam suscipit porro aliquam quasi autem nemo qui. Tempore a ad cumque laudantium! Ratione, ex iusto obcaecati dolorum eveniet facere nesciunt itaque repellendus, maiores debitis porro blanditiis aperiam architecto, deleniti nemo dolore consectetur necessitatibus? Quo dignissimos facere placeat voluptas temporibus iure voluptate iste neque? Facere error dolor non, fugit eius commodi molestiae deleniti. Itaque asperiores sit minima vitae quis in commodi possimus repellendus explicabo. Est, placeat reiciendis?
"""
  peoples=[
    {'name':'Virat', 'age':36},
    {'name':'rahul', 'age':31},
    {'name':'rohti', 'age':38},
    {'name':'Hardik', 'age':30},
    {'name':'shubhman', 'age':24},
  ]
  return render(request, 'context.html', context={'peoples':peoples, 'text':text})