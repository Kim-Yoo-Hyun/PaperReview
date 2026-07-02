# Depth Map Prediction from a Single Image using a Multi-Scale Deep Network

- Year/Venue: 2014 / NeurIPS
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, geometry
- Paper link: ./2014/NeurIPS/2014_NeurIPS_Depth-Map-Prediction-from-a-Single-Image-using-a-Multi-Sca/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.
- While there is much prior work on estimating depth based on stereo images or motion , there has been relatively little on estimating depth from a single image.
- Moreover, the task is inherently ambiguous, with a large source of uncertainty coming from the overall scale.

## Core Idea
- In this paper, we present a new method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction based on the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- By leveraging the raw datasets as large sources of training data, our method achieves boundaries without the need for superpixelation.

## Limitation
- In future work, we plan to extend our method to incorporate further 3D geometry information, such as surface normals.

## Contribution
- By leveraging the raw datasets as large sources of training data, our method achieves boundaries without the need for superpixelation.
- In this paper, we present a new method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction based on the ...
- Moreover, the task is inherently ambiguous, with a large source of uncertainty coming from the overall scale.

## Abstract Cue
- Predicting depth is an essential component in understanding the 3D geometry of a scene.
