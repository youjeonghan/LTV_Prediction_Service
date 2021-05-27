from django.shortcuts import render
from django.http import HttpResponse
from .MongoDbManager import MongoDbManager
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .controllers import make_pipeline
from .predrction import predict


def index(request):
    return render(request, "ltv/index.html")


def income_predict(request):
    predict_list = predict(
        request.GET["from"], request.GET["to"], request.GET["percentile"]
    )

    return HttpResponse(json.dumps(predict_list), status=200)


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


def device_os_analysis(request):
    if request.method == "GET":
        percentile = int(
            MongoDbManager().database_len * float(request.GET["percentile"])
        )
        pipeline = make_pipeline("device_operating_system_version", percentile)
        result = list(MongoDbManager().database.aggregate(pipeline))
        for item in result:
            item["device_os"] = item["_id"]
            del item["_id"]
        result.sort(key=lambda x: float(x["device_os"][8:11]))
        return HttpResponse(json.dumps(result), status=200)


def weekday_analysis(request):
    if request.method == "GET":
        percentile = int(
            MongoDbManager().database_len * float(request.GET["percentile"])
        )
        week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        pipeline = make_pipeline("weekday", percentile)
        result = list(MongoDbManager().database.aggregate(pipeline))
        result.sort(key=lambda x: x["_id"])
        for item in result:
            item["weekday"] = week[item["_id"]]
            del item["_id"]

        return HttpResponse(json.dumps(result), status=200)


def device_name_analysis(request):
    if request.method == "GET":
        percentile = int(
            MongoDbManager().database_len * float(request.GET["percentile"])
        )
        pipeline = make_pipeline("device_mobile_marketing_name", percentile)
        result = list(MongoDbManager().database.aggregate(pipeline))
        for item in result:
            if item["_id"] == None:
                item["device_name"] = "Uncertain"
            else:
                item["device_name"] = item["_id"]
            del item["_id"]
        return HttpResponse(json.dumps(result), status=200)


def region_analysis(request):
    if request.method == "GET":
        percentile = int(
            MongoDbManager().database_len * float(request.GET["percentile"])
        )
        pipeline = make_pipeline("geo_region", percentile)
        result = list(MongoDbManager().database.aggregate(pipeline))
        for item in result:
            if item["_id"] == "":
                item["region"] = "Uncertain"
            else:
                item["region"] = item["_id"]
            del item["_id"]
        return HttpResponse(json.dumps(result), status=200)


def time_analysis(request):
    if request.method == "GET":
        percentile = int(
            MongoDbManager().database_len * float(request.GET["percentile"])
        )
        pipeline = make_pipeline("hour", percentile)
        result = list(MongoDbManager().database.aggregate(pipeline))
        for item in result:
            item["hour"] = item["_id"]
            del item["_id"]
        result.sort(key=lambda x: x["hour"])

        return HttpResponse(json.dumps(result), status=200)
