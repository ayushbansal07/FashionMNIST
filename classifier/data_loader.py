import torchvision
import torch
import os

class DataLoader:
    def __init__(self, base_dir="./data/", batch_size=32, shuffle=True):
        self.base_dir = base_dir
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.train_dataset = None
        self.test_dataset = None
        self.transform = torchvision.transforms.Compose([
                           torchvision.transforms.ToTensor(),
                           torchvision.transforms.Normalize(
                             (0.1307,), (0.3081,))
                         ])

    def loadTrainData(self):
        if self.train_dataset is None:
            self.train_dataset = torchvision.datasets.FashionMNIST(self.base_dir, train = True, transform=self.transform)
        loader = torch.utils.data.DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=self.shuffle)
        return loader

    def loadTestData(self):
        if self.test_dataset is None:
            self.test_dataset = torchvision.datasets.FashionMNIST(self.base_dir, train = False, transform=self.transform)
        loader = torch.utils.data.DataLoader(self.test_dataset, batch_size=self.batch_size, shuffle=self.shuffle)
        return loader
