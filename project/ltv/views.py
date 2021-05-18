from django.shortcuts import render
from django.http import HttpResponse
from .MongoDbManager import MongoDbManager
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(requset):
    temp = MongoDbManager().get_users_from_collection({})
    li = []
    for i in temp:
        del i["_id"]
        del i["first_play_day"]

        li.append(i)
    return HttpResponse(json.dumps(""), status=200)
    # return HttpResponse("안녕하세요 LTV 예측 서비스 입니다.")


def test(request):
    temp = MongoDbManager().get_users_from_collection(
        {"ad_id": "cfc31233-e5f7-4eb2-a442-0b2df5f2f83f"}
    )
    context = {"item": temp[0]}
    return render(request, "ltv/test.html", context)


@csrf_exempt
def test_json(request):
    if request.method == "GET":
        temp = MongoDbManager().get_users_from_collection(
            {"ad_id": "cfc31233-e5f7-4eb2-a442-0b2df5f2f83f"}
        )
        return HttpResponse(json.dumps(temp[0], default=str), status=200)

    elif request.method == "POST":
        temp = MongoDbManager().get_users_from_collection(
            {"ad_id": "cfc31233-e5f7-4eb2-a442-0b2df5f2f83f"}
        )
        return HttpResponse(
            json.dumps({"id": temp[0]["ad_id"]}, default=str), status=200
        )

    else:
        return HttpResponse(status=405)
