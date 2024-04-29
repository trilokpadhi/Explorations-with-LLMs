import torch 
import torch.nn as nn
import torch.nn.functional as F

class LayerNormalization(nn.Module):
    def __init__(self):
        super(LayerNormalization, self).__init__()
        self.gamma = nn.Parameter(torch.ones(768))
        self.beta = nn.Parameter(torch.zeros(768))
        
    def forward(self, x, residual):
        mean = x.mean(dim=-1, keepdim=True)
        std = x.std(dim=-1, keepdim=True)
        return self.gamma * (x - mean) / (std + 1e-6) + self.beta + residual
        
    
class MultiHeadSelfAttention(nn.Module):
    def __init__(self, num_heads):
        super(MultiHeadSelfAttention, self).__init__()
        self.num_heads = num_heads
        self.attention = nn.MultiheadAttention(embed_dim=768, num_heads=num_heads)
    
    def forward(self, x):
        return self.attention(x, x, x)[0]

class AdapterFusion(nn.Module):
    def __init__(self):
        super(AdapterFusion, self).__init__()
        self.fc = nn.Linear(768, 768)
    
    def forward(self, x, residual):
        return F.relu(self.fc(x) + residual)


def transformer_block_with_adapter(x):
    residual = x
    x = MultiHeadSelfAttention(num_heads=4)(x)
    x = AdapterFusion()([x]) # adapter fusion
    x = LayerNormalization()(x, residual) # layer normalization
    residual = x
    x = nn.Linear(768, 3072)(x)
    x = nn.ReLU()(x)
    x = nn.Linear(3072, 768)(x)
    x = LayerNormalization()(x, residual) # layer normalization
    return x
    