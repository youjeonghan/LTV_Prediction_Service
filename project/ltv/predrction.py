import os
import torch
import numpy as np
from django.conf import settings
import pandas as pd
from datetime import datetime, timedelta

from django.http import HttpResponse
import json


def predict(start, end, percentile):
    # 경로 설정
    STATICFILES_DIRS = getattr(settings, "STATICFILES_DIRS", None)

    # CPU / GPU 설정
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"현재 {device} 사용중")

    load = torch.load(
        os.path.join(STATICFILES_DIRS[0], "model/model2.pth"), map_location="cpu"
    )  # 그저 test 데이터 입력값 불러오려고만 쓰는거임

    # return HttpResponse(json.dumps(load), status=200)

    # print("모델 설명: ", load["config"]["neural_net_structure"])
    # print("data_set: ", load["config"]["data_set"])
    # print("Learning rate: ", load["config"]["lr"])
    # print("Train ratio: ", load["config"]["train_ratio"])
    # print("Test ratio: ", 1 - load["config"]["train_ratio"])

    # 모델 바로 불러오기
    model_pt = torch.load(
        os.path.join(STATICFILES_DIRS[0], "model/model2.pt"), map_location="cpu"
    )  # model 전체 불러오기

    x_test = np.array(load["test_features"][0])  # 입력값
    y_test = np.array(load["test_target"])  # 출력값
    print(min(load["test_features"][1]))
    print(max(load["test_features"][1]))
    x_test = torch.tensor(x_test).to(device)  # 텐서화
    y_test = torch.tensor(y_test).to(device)  # 텐서화

    model_pt.eval()

    predict_y = model_pt(x_test.float())
    ads = predict_y.sum(dim=0)
    # predict_y = predict_y.sum(dim=1)  # output 3개 하나로 합치기(rv is ba)

    # 테스트용
    start = datetime(int(start[0:4]), int(start[5:7]), int(start[8:10]))  # "2021-05-24"
    end = datetime(int(end[0:4]), int(end[5:7]), int(end[8:10]))  # "2021-06-06"

    # date, per 작업
    result = predict_y.tolist()
    # result = predict_y.flatten().tolist()

    result_date = load["test_features"][1]

    result = list(zip(result, result_date))
    result.sort(key=lambda x: x[0])
    percentile = int(len(result) * float(percentile))
    result = result[:percentile]
    result = devide_period(result, start, end)
    return result


def devide_period(data, start, end):
    result = {}
    result["data"] = {}
    target_day = start
    week_idx = 0
    week_criteria = []
    while target_day < end:
        week_idx += 1
        week_criteria.append((f"week{week_idx}", target_day, target_day + timedelta(days=6)))
        result["data"][f"week{week_idx}"] = 0
        target_day += timedelta(days=7)

    total = 0
    user = 0
    ads_ratio = {"is": 0, "rv": 0, "ba": 0}

    for item in data:
        for n, s, e in week_criteria:
            if s <= item[1] <= e:
                result["data"][n] += sum(item[0])
                ads_ratio["is"] += item[0][0]
                ads_ratio["rv"] += item[0][1]
                ads_ratio["ba"] += item[0][2]
                total += sum(item[0])
                user += 1
                break
    result["data"] = {k: v for k, v in sorted(result["data"].items(), key=lambda x: -x[1])}
    result["max"] = 0
    result["min"] = float("inf")
    for k, v in result["data"].items():
        result["max"] = max(result["max"], v)
        result["min"] = min(result["min"], v)
    result["total"] = total
    result["user"] = user
    result["avg"] = total / user
    result["ads_ratio"] = ads_ratio

    return result
