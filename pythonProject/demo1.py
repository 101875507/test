from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.optim as optim
import requests
from torchvision import models
from torchvision import transforms
import time
import hiddenlayer as h
vgg19 = models.vgg19(pretrained=True)
vgg = vgg19.features
for param in vgg.parameters():
    param.requires_grad_(False)
def load_image(img_path,max_size=400,shape=None):
    image = Image.open(img_path).convert('RGB')
    if max(image.size) > max_size:
        size = max_size
    else:
        size =max(image.size)
    if shape is not None:
        size = shape
    in_transform = transforms.Compose([transforms.Resize(size),transforms.ToTensor(),transforms.Normalize((0.485,0.456,0.406),(0.229,0.224,0.225))])
    image = in_transform(image)[:3,:,:].unsqueeze(dim=0)
    return image
def im_convert(tensor):
    image = tensor.data.numpy().squeeze()
    image = image.transpose(1,2,0)
    image = image*np.array((0.485,0.456,0.406))+np.array((0.229,0.224,0.225))
    image = image.clip(0,1)
    return image
content = load_image("D:\\lijun\\Pictures\\Saved Pictures\\th (4).jpg",max_size=400)
print("content shape:",content.shape)
style = load_image("C:\\Users\\lijun\\Pictures\\Saved Pictures\\下载.png",shape = content.shape[-2:])
print("style shape:",style.shape)
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,5))
ax1.imshow(im_convert(content))
ax2.imshow(im_convert(style))
plt.show()

def get_feature(image,model,layers=None):
    if layers is None:
        layers = {
            '0':'conv1_1',
            '5':'conv2_1',
            '10':'conv3_1',
            '19':'conv4_1',
            '21':'conv4_2',
            '28':'conv5_1'
        }
    features = {}
    x =image
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x
        return features
def gram_matrix(tensor):
    _,d,h,w = tensor.size()
    tensor = tensor .view(d,h*w)
    gram = torch.mm(tensor,tensor.t())
    return gram
content_features=get_feature( content ,vgg)
style_features=get_feature(style,vgg)
style_grams={layer : gram_matrix(style_features[layer]) for layer in style_features}
target = content.clone().requires_grad_(True)
style_weights = {
    'conv1_1': 1.,
    'conv2_1': 0.75,
    'conv3_1': 0.2,
    'conv4_1': 0.2,
    'conv4_2': 0.2,
    'conv5_1': 0.2

}
alpha = 1
beat = 1e6
content_weight = alpha
style_weight = beat
show_every = 1000
total_loss_all = []
content_loss_all = []
stytle_loss_all = []
optimizer = optim.Adam([ target ],lr=0.0003)
steps = 5000
t0 = time.time()
for ii in range(1,steps+1):
    target_features =  get_feature(target,vgg)
    content_loss = torch.mean((target_features['conv4_2'] - content_features["conv4_2"]) **2)
    stytle_loss = 0
    for layer in style_weights :
        target_feature = target_features[layer]
        target_garm=gram_matrix(target_feature)
        _,d,h,w, = target_feature.shape
        style_garm= style_grams[layer]
        layer_style_loss = style_weights[layer]*torch.mean((target_garm-style_garm) **2)
        stytle_loss+=layer_style_loss/(d*h*w)
        total_loss=content_weight * content_loss+ style_weight*stytle_loss
        content_loss_all.append(content_loss.item())
        stytle_loss_all.append(stytle_loss.item())
        total_loss_all.append(total_loss.item())
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        if ii % show_every == 0:
            print("total loss:",total_loss.item())
            print("use time:",(time.time()-t0)/3600,"hour")
            newim = im_convert(target)
            plt.imshow(newim)

