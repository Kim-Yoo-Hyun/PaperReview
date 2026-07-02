# Method

- Year/Venue: 2017 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, geometry
- Paper link: ./2017/CVPR/2017_CVPR_SSCNet-Semantic-Scene-Completion-from-a-Single-Depth-Image/paper.pdf
- Code/Project: https://github.com/shurans/sscnet
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.
- To leverage the coupled nature of these two tasks, we introduce the semantic scene completion network (SSCNet), an end-to-end 3D convolutional network that takes a single depth image ...
- Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image .

## 원리적 동기
- However, we observe that these two problems are tightly intertwined.
- Therefore, the two problems of predicting voxel occupancy and identifying object semantics are strongly coupled.
- The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.

## 핵심 방법론
- The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.
- Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image .
- For the real data, we use the NYU dataset , which contains 1449 depth maps captured from Kinect.
- As our evaluation metric, we use the voxel-level intersection over union (IoU) of predicted voxel Does recognizing objects help scene completion?
- training prec. recall IoU Zheng et al.
