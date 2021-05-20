import os
import torch
import numpy as np
from django.conf import settings
import pandas as pd


def predict():
    # 경로 설정
    STATICFILES_DIRS = getattr(settings, "STATICFILES_DIRS", None)

    # CPU / GPU 설정
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"현재 {device} 사용중")

    load = torch.load(
        os.path.join(STATICFILES_DIRS[0], "model/model4.pth"), map_location="cpu"
    )  # 그저 test데이터 입력값 불러오려고만 쓰는거임

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

    return predict_y.flatten().tolist()
