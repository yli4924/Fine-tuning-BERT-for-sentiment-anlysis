from torch.utils.data import Dataset
from torchtext.data.utils import get_tokenizer

class MovieDataset(Dataset):
    def __init__(self, path) -> None:
        self.tokenizer = get_tokenizer('basic_english')
if __name__ == '__main__':
    print("Prepare dataset...")

