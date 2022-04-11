import torch
from torch.autograd import Variable
import torchvision.transforms as transforms
import torchvision.datasets as dsets
from pl_bolts.models.regression import LogisticRegression
import pytorch_lightning as pl

from pl_bolts.datamodules.mnist_datamodule import MNISTDataModule

train_dataset = dsets.MNIST(
    root="./data", train=True, transform=transforms.ToTensor(), download=True
)
test_dataset = dsets.MNIST(
    root="./data", train=False, transform=transforms.ToTensor(), download=True
)


# class LogisticRegression(torch.nn.Module):
#     def __init__(self, input_dim, output_dim):
#         super(LogisticRegression, self).__init__()
#         self.linear = torch.nn.Linear(input_dim, output_dim)

#     def forward(self, x):
#         outputs = self.linear(x)
#         return outputs


batch_size = 100
n_iters = 3000
epochs = n_iters / (len(train_dataset) / batch_size)
input_dim = 784
output_dim = 10
lr_rate = 0.001

# train_loader = torch.utils.data.DataLoader(
#     dataset=train_dataset, batch_size=batch_size, shuffle=True
# )
# test_loader = torch.utils.data.DataLoader(
#     dataset=test_dataset, batch_size=batch_size, shuffle=False
# )

# REVIEW: I am blocked here. The LR doesn't train:
logistic_regression = LogisticRegression(input_dim=28 * 28, num_classes=10)

trainer = pl.Trainer(
    accelerator="gpu", devices=1, auto_select_gpus=True, max_epochs=10000
)

datamodule = MNISTDataModule(data_dir="./data", batch_size=256)

# REVIEW: Something is wrong here!
trainer.fit(model=logistic_regression, datamodule=datamodule)

# model = LogisticRegression(input_dim, output_dim)
# criterion = torch.nn.CrossEntropyLoss()  # computes softmax and then the cross entropy
# optimizer = torch.optim.SGD(model.parameters(), lr=lr_rate)


# iter = 0
# for epoch in range(int(epochs)):
#     for i, (images, labels) in enumerate(train_loader):
#         images = Variable(images.view(-1, 28 * 28))
#         labels = Variable(labels)

#         optimizer.zero_grad()
#         outputs = model(images)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

#         iter += 1
#         if iter % 500 == 0:
#             # calculate Accuracy
#             correct = 0
#             total = 0
#             for images, labels in test_loader:
#                 images = Variable(images.view(-1, 28 * 28))
#                 outputs = model(images)
#                 _, predicted = torch.max(outputs.data, 1)
#                 total += labels.size(0)
#                 # for gpu, bring the predicted and labels back to cpu fro python operations to work
#                 correct += (predicted == labels).sum()
#             accuracy = 100 * correct / total
#             print(
#                 "Iteration: {}. Loss: {}. Accuracy: {}.".format(
#                     iter, loss.item(), accuracy
#                 )
#             )
