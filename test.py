import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import numpy as np
import pickle

torch.manual_seed(11)  # random seed 설정 나중에 없애셈
# CPU / GPU 설정
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"현재 {device} 사용중")

load = torch.load("model4.pth")  # 그저 test데이터 입력값 불러오려고만 쓰는거임

print("모델 설명: ", load["config"]["neural_net_structure"])
print("data_set: ", load["config"]["data_set"])
print("Learning rate: ", load["config"]["lr"])
print("Train ratio: ", load["config"]["train_ratio"])
print("Test ratio: ", 1 - load["config"]["train_ratio"])

# model 및 trainer 호출 - 이게 원래 방식
model = CustomModel(load["config"]["neural_net_structure"]).to(device)
model.load_state_dict(load["model"])
optimizer = load["optimizer"]
crit = load["crit"]
crit_mape = load["crit_mape"]

# 모델 바로 불러오기
model_pt = torch.load("model4.pt")  # model 전체 불러오기
x_test = np.array(load["test_features"])  # 입력값
y_test = np.array(load["test_target"])  # 출력값
x_test = torch.tensor(x_test).to(config.device)  # 텐서화
y_test = torch.tensor(y_test).to(config.device)  # 텐서화

rand_idx = torch.randperm(x_test.size(0)).to(config.device)
x_test = torch.index_select(x_test, dim=0, index=rand_idx)
y_test = torch.index_select(y_test, dim=0, index=rand_idx)

print("x_test : ", x_test)
print(x_test.shape)
model_pt.eval()

# with torch.no_grad(): # 써도되고 안써도 된다.
predict_y = model_pt(x_test.float())
loss = crit(predict_y, y_test.unsqueeze(1))  # 그냥 loss값 같게 나오는지 체크해볼라고 쓴거
print(predict_y.shape)
print("prediction : ", predict_y)
print("loss : ", loss)
