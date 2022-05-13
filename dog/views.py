


import json
from django.http import JsonResponse
from django.views import View
from .models import Owner, Dog


class OwnersView(View):
  def post(self, request):
    input_data = json.loads(request.body)
    Owner.objects.create(
      name = input_data["name"],
      email = input_data["email"],
      age = input_data["age"]
    )
    return JsonResponse({"message" : "SUCCESS"}, status=201)

  def get(self, request):
    results = []
    owners = Owner.objects.all()
    for owner in owners:
      results.append({
        "name" : owner.name,
        "age" : owner.age,
        "email" : owner.email,
      })
    return JsonResponse({"Owners": results}, status = 200)



class DogsView(View):
  def post(self, request):
    input_data = json.loads(request.body)
    o = Owner.objects.get(name=input_data["owner_name"])
    Dog.objects.create(
      owner_id = o.id,
      name = input_data["name"],
      age = input_data["age"]
    )
    return JsonResponse({"message" : "SUCCESS"}, status = 201)