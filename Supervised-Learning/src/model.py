import torch
import torch.nn as nn

class Seq2SeqLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=100, num_layers=2, output_len=15, learn_init_state=False):
        super(Seq2SeqLSTM, self).__init__()
        self.learn_init_state = learn_init_state
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                            num_layers=num_layers, batch_first=True, dropout=0.2)
        self.fc = nn.Linear(hidden_size, output_len)

        if learn_init_state:
            self.h0 = nn.Parameter(torch.randn(num_layers, 1, hidden_size))
            self.c0 = nn.Parameter(torch.randn(num_layers, 1, hidden_size))

    def forward(self, x, warm_up=None):
        batch_size = x.size(0)

        if self.learn_init_state:
            h0 = self.h0.repeat(1, batch_size, 1)
            c0 = self.c0.repeat(1, batch_size, 1)
        else:
            h0 = torch.zeros(self.num_layers, batch_size, self.hidden_size, device=x.device)
            c0 = torch.zeros(self.num_layers, batch_size, self.hidden_size, device=x.device)

        if warm_up is not None:
            _, (h0, c0) = self.lstm(warm_up, (h0, c0))

        out, _ = self.lstm(x, (h0, c0))
        return self.fc(out[:, -1, :])
