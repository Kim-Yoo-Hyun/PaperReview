# Method

- Year/Venue: 2022 / ICLR
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, semantic, open-vocabulary, alignment
- Paper link: ./2022/ICLR/2022_ICLR_Language-driven-Semantic-Segmentation/paper.pdf
- Code/Project: https://github.com/isl-org/lang-seg
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Assuming that ni is the number of classes in fold i, for each fold i, we use images of other folds for training and randomly sampled 1000 images ...
- We use a base learning rate of 0.05 and train the model for 60 epochs.
- We follow their official code, training setting and training steps on the basis of their provided model pretrained on ImageNet (Deng et al., 2009).

## 원리적 동기
- Assuming that ni is the number of classes in fold i, for each fold i, we use images of other folds for training and randomly sampled 1000 images ...

## 핵심 방법론
- Assuming that ni is the number of classes in fold i, for each fold i, we use images of other folds for training and randomly sampled 1000 images ...
- We use a base learning rate of 0.05 and train the model for 60 epochs.
- We follow their official code, training setting and training steps on the basis of their provided model pretrained on ImageNet (Deng et al., 2009).
- It consists of 1000 object classes with pixelwise annotated segmentation masks.
- Following the standard protocol, we split the 1000 classes into training, validation, and test classes, with 520, 240, and 240 classes, respectively.
