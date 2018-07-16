# CAMP-Project
## Visualization Methods:

* Guided Back Prop / Vanilla Back Prop

    J. T. Springenberg, A. Dosovitskiy, T. Brox, and M. Riedmiller. Striving for Simplicity: The All Convolutional Net, https://arxiv.org/abs/1412.6806
    
    K. Simonyan, A. Vedaldi, A. Zisserman. Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps, https://arxiv.org/abs/1312.6034
    
* Smooth Back Prop

    D. Smilkov, N. Thorat, N. Kim, F. Viégas, M. Wattenberg. SmoothGrad: removing noise by adding noise https://arxiv.org/abs/1706.03825
* Grad Cam / Guided Gram Cam

    R. R. Selvaraju, A. Das, R. Vedantam, M. Cogswell, D. Parikh, and D. Batra. Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization, https://arxiv.org/abs/1610.02391
    
* Deep Dream

    D. Smilkov, N. Thorat, N. Kim, F. Viégas, M. Wattenberg. SmoothGrad: removing noise by adding noise https://arxiv.org/abs/1706.03825

* Inverted image representations

    A. Mahendran, A. Vedaldi. Understanding Deep Image Representations by Inverting Them, https://arxiv.org/abs/1412.0035 
    
* Deep Image Prior (To be implemented)

    Dmitry Ulyanov, Andrea Vedaldi, Victor Lempitsky. Deep Image Prior https://arxiv.org/abs/1711.10925

## Attacks:

* FGSM

    Alexey Kurakin, Ian Goodfellow, Samy Bengio, “Adversarial examples in the physical world”,
https://arxiv.org/abs/1607.02533
* PGD

    Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, Adrian Vladu, “Towards Deep Learning Models Resistant to Adversarial Attacks”, https://arxiv.org/abs/1706.06083
* Single Pixel

    Nina Narodytska, Shiva Prasad Kasiviswanathan, “Simple Black-Box Adversarial Perturbations for Deep Networks”, https://arxiv.org/pdf/1612.06299.pdf
* Boundary

    Wieland Brendel (*), Jonas Rauber (*), Matthias Bethge, “Decision-Based Adversarial Attacks: Reliable Attacks Against Black-Box Machine Learning Models”, https://arxiv.org/abs/1712.04248
* Deep Fool

    Seyed-Mohsen Moosavi-Dezfooli, Alhussein Fawzi, Pascal Frossard, “DeepFool: a simple and accurate method to fool deep neural networks”, https://arxiv.org/abs/1511.04599
    
* ...?
    
## ConvNets:
  Currently, AlexNet & VGG19 from torch vision library (pre-trained on ImageNet).

## Instructions:

[1] Choose a visualization method by opening the corresponding file.

[2] Choose a sample image (first line of the main methods, "target example") A number from 0-2.

[3] Choose a ConvNet. (Either 'AlexNet' or 'VGG19')

[4] Choose an attack. (FGSM, PGD, Boundary, DeepFool, SinglePixel)

[5] Run the code :D
