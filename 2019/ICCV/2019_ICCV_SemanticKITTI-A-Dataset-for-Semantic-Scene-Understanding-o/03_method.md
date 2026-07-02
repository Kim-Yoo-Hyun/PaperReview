# Method

- Year/Venue: 2019 / ICCV
- Category: Benchmarks and Datasets
- Tags: 3D Vision, LiDAR, semantic, Dataset
- Paper link: ./2019/ICCV/2019_ICCV_SemanticKITTI-A-Dataset-for-Semantic-Scene-Understanding-o/paper.pdf
- Code/Project: http://semantic-kitti.org/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose three benchmark tasks based on this dataset: (i) semantic segmentation of point clouds using a single scan, (ii) semantic segmentation using multiple past scans, and (iii) ...
- In this paper, we introduce a large dataset to propel research on laser-based semantic segmentation.

## 원리적 동기
- Despite the relevance of semantic scene understanding for this application, there is a lack of a large dataset for this task which is based on an automotive LiDAR.
- Complementary sensor modalities enable to cope with deficits or failures of particular sensors.
- We propose three benchmark tasks based on this dataset: (i) semantic segmentation of point clouds using a single scan, (ii) semantic segmentation using multiple past scans, and (iii) ...

## 핵심 방법론
- mIoU road sidewalk parking other-ground building car truck bicycle motorcycle other-vehicle vegetation trunk terrain person bicyclist motorcyclist fence pole traffic sign PointNet SPGraph SPLATNet PointNet++ SqueezeSeg SqueezeSegV2 TangentConv ...
- All methods were trained on sequences 00 to 10, except for sequence 08 which is used as validation set.
- PointNet PointNet++ SPGraph SPLATNet TangentConv SqueezeSeg SqueezeSegV2 DarkNet21Seg DarkNet53Seg Approach PointNet PointNet++ SPGraph TangentConv SPLATNet SqueezeSeg SqueezeSegV2 DarkNet21Seg DarkNet53Seg
