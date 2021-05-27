import os
import torch
import numpy as np
from django.conf import settings
import pandas as pd
from datetime import datetime, timedelta


def predict(start, end, percentile):
    # 경로 설정
    STATICFILES_DIRS = getattr(settings, "STATICFILES_DIRS", None)

    # CPU / GPU 설정
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"현재 {device} 사용중")

    load = torch.load(
        os.path.join(STATICFILES_DIRS[0], "model/model4.pth"), map_location="cpu"
    )  # 그저 test 데이터 입력값 불러오려고만 쓰는거임

    print("모델 설명: ", load["config"]["neural_net_structure"])
    print("data_set: ", load["config"]["data_set"])
    print("Learning rate: ", load["config"]["lr"])
    print("Train ratio: ", load["config"]["train_ratio"])
    print("Test ratio: ", 1 - load["config"]["train_ratio"])

    # 모델 바로 불러오기
    model_pt = torch.load(
        os.path.join(STATICFILES_DIRS[0], "model/model4.pt"), map_location="cpu"
    )  # model 전체 불러오기
    x_test = np.array(load["test_features"])  # 입력값
    y_test = np.array(load["test_target"])  # 출력값
    x_test = torch.tensor(x_test).to(device)  # 텐서화
    y_test = torch.tensor(y_test).to(device)  # 텐서화

    rand_idx = torch.randperm(x_test.size(0)).to(device)
    x_test = torch.index_select(x_test, dim=0, index=rand_idx)
    y_test = torch.index_select(y_test, dim=0, index=rand_idx)

    print("x_test : ", x_test)
    print(x_test.shape)
    model_pt.eval()

    predict_y = model_pt(x_test.float())
    print(predict_y.shape)
    print("prediction : ", predict_y)

    # 테스트용
    start = datetime(2021, 5, 24)  # "2021-05-24"
    end = datetime(2021, 7, 18)  # "2021-06-06"

    # date, per 작업
    result = predict_y.flatten().tolist()

    # 테스트용
    d = datetime(2021, 5, 24)
    result_date = []
    for i in range(0, 10):
        result_date.extend([d] * (len(result) // 10))
        d += timedelta(days=7)
    # result_date = [datetime(2021, 5, 24)] * (len(result) // 2)
    # result_date.extend([datetime(2021, 5, 31)] * (len(result) - len(result) // 2))

    # result_date = [0] * len(result)  # test데이터의 날짜 목록

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
        week_criteria.append(
            (f"week{week_idx}", target_day, target_day + timedelta(days=6))
        )
        result["data"][f"week{week_idx}"] = 0
        target_day += timedelta(days=7)

    total = 0
    user = 0
    for item in data:
        for n, s, e in week_criteria:
            if s <= item[1] <= e:
                result["data"][n] += item[0]
                total += item[0]
                user += 1
                break
    result["total"] = total
    result["user"] = user
    result["avg"] = total / user
    return result
