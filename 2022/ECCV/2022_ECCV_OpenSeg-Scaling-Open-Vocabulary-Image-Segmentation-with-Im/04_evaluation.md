# Evaluation

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, semantic, open-vocabulary, segmentation
- Paper link: ./2022/ECCV/2022_ECCV_OpenSeg-Scaling-Open-Vocabulary-Image-Segmentation-with-Im/paper.pdf
- Code/Project: https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/openseg
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO

## Metrics
- accuracy
- mIoU
- IoU
- mAP
- ADE

## Evaluation Protocol and Results
- 4.1 Experimental Settings Architecture.
- We use EfficientNet-B7 (and ResNet101 in Table 2) as the backbone architecture and employ FPN for multi-scale feature fusion.
- We use pyramid levels from P2 to P5 with feature dimension 640, upsample all feature levels to P2 , and then merge them by a sum operation to ...
- To compute Fz and Fs , we apply a fc layer followed by 3 layers of 3 × 3 convolutions with 640 channels after F.
- OpenSeg significantly outperforms the recent openvocabulary method of LSeg by +19.9 mIoU on PASCAL dataset, thanks to its scalability. bride groom hills field sky cow calf grass trees ...

## Baselines
- Unless otherwise stated, for each core we compute the loss over the local batch of examples (See Appendix F for the comparison between sync and unsync contrastive loss ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
