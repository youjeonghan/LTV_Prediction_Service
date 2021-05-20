import torch
import torch.nn as nn
import torch.optim as optim


class CustomModel(nn.Module):
    def __init__(self):
        """
        모델 구조 정의와 초기화
        """
        super().__init__()
        # self.model = nn.Sequential(
        #     nn.Linear(78, 78, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(78, 78, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(78, 78, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(78, 60, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(60, 40, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(40, 20, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(20, 10, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(10, 6, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(6, 3, bias=True),
        #     nn.ReLU(),
        #     nn.Linear(3, 1, bias=True),
        # )
        self.model = nn.Sequential(
            nn.Linear(76, 76, bias=True),
            nn.ReLU(),
            nn.Linear(76, 76, bias=True),
            nn.ReLU(),
            nn.Linear(76, 76, bias=True),
            nn.ReLU(),
            nn.Linear(76, 60, bias=True),
            nn.ReLU(),
            nn.Linear(60, 40, bias=True),
            nn.ReLU(),
            nn.Linear(40, 20, bias=True),
            nn.ReLU(),
            nn.Linear(20, 10, bias=True),
            nn.ReLU(),
            nn.Linear(10, 6, bias=True),
            nn.ReLU(),
            nn.Linear(6, 3, bias=True),
            nn.ReLU(),
            nn.Linear(3, 1, bias=True),
        )

    def forward(self, x):
        """
        학습데이터를 입력받아서 forward 연산을 진행시키는 함수
        """
        return self.model(x)


# 손실함수
def RMSE(y_pred, Y):
    return torch.sqrt(nn.MSELoss()(y_pred, Y))


# 손실함수
def RMSLE(y_pred, Y):
    add = torch.ones_like(y_pred)
    return torch.sqrt(nn.MSELoss()(torch.log(y_pred + add), torch.log(Y + add)))


# 손실함수 MAPE
def MAPE(y_pred, Y):
    temp = (Y - y_pred).abs() / Y.abs()
    return temp.mean() * 100
