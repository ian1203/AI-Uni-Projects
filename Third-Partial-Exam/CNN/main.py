import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

#Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#Transform (normalize RGB values to [-1, 1])
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

#PyTorch will download the dataset here
dataset_path = './data'

#Load CIFAR-10 (automatically downloads and sets up everything)
trainset = torchvision.datasets.CIFAR10(root=dataset_path, train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.CIFAR10(root=dataset_path, train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

classes = trainset.classes

#Define the CNN model
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)  # 32 filters, 3x3
        self.pool = nn.MaxPool2d(2, 2)  # Max pooling
        self.dropout = nn.Dropout(0.2)  # 20% dropout
        self.fc1 = nn.Linear(32 * 16 * 16, 128)  # Dense layer
        self.fc2 = nn.Linear(128, 10)  # Output layer

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # Conv -> ReLU -> MaxPool
        x = x.view(-1, 32 * 16 * 16)  # Flatten
        x = torch.relu(self.fc1(x))  # Dense + ReLU
        x = self.dropout(x)
        x = self.fc2(x)  # Output logits
        return x

#Initialize the model
net = SimpleCNN().to(device)

#Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

#Training loop
epochs = 5
for epoch in range(epochs):
    running_loss = 0.0
    net.train()
    for inputs, labels in trainloader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch+1} - Loss: {running_loss:.3f}")

#Test accuracy
correct = 0
total = 0
net.eval()
with torch.no_grad():
    for inputs, labels in testloader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = net(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"\nTest Accuracy: {100 * correct / total:.2f}%")

#Visualize filters from the first conv layer
def visualize_filters(layer):
    weights = layer.weight.data.cpu()
    fig, axes = plt.subplots(4, 8, figsize=(10, 5))
    for i, ax in enumerate(axes.flat):
        img = weights[i].permute(1, 2, 0)
        img = (img - img.min()) / (img.max() - img.min())  # Normalize
        ax.imshow(img)
        ax.axis('off')
    plt.suptitle("Filters from the First Convolutional Layer")
    plt.tight_layout()
    plt.show()

visualize_filters(net.conv1)

#Sample images
def imshow(img):
    img = img / 2 + 0.5  # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.axis('off')
    plt.show()

dataiter = iter(testloader)
images, labels = next(dataiter)
imshow(torchvision.utils.make_grid(images[:8]))
print("Labels:", [classes[labels[i]] for i in range(8)])
