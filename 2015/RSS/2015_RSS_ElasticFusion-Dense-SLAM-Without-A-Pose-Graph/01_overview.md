# ElasticFusion: Dense SLAM Without A Pose Graph

- Year/Venue: 2015 / RSS
- Category: Foundations: SLAM and Sensor Geometry
- Tags: 3D Vision, SLAM, RGB-D, 3D reconstruction
- Paper link: ./2015/RSS/2015_RSS_ElasticFusion-Dense-SLAM-Without-A-Pose-Graph/paper.pdf
- Code/Project: https://github.com/mp3guy/ElasticFusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross loop back on ...
- In sparse feature-based SLAM, it is well understood that loopy local motion can be dealt with either via joint probabilistic filtering , or in-the-loop joint optimisation of poses ...
- In fact, even in sparse feature-based SLAM there have been relatively few attempts to deal with motion which is both extended and extremely loopy, such as Strasdat et ...

## Core Idea
- —We present a novel approach to real-time dense visual SLAM.
- Our approach applies local model-to-model surface loop closure optimisations as often as possible to stay close to the mode of the map distribution, while utilising global loop closure ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- —We present a novel approach to real-time dense visual SLAM.
- Our system is capable of capturing comprehensive dense globally consistent surfel-based maps of room scale environments explored using an RGB-D camera in an incremental online fashion, without pose ...
- This is accomplished by using dense frame-tomodel camera tracking and windowed surfel-based fusion coupled with frequent model refinement through non-rigid surface deformations.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- —We present a novel approach to real-time dense visual SLAM.
- Our approach applies local model-to-model surface loop closure optimisations as often as possible to stay close to the mode of the map distribution, while utilising global loop closure ...
- However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross loop back on ...

## Abstract Cue
- —We present a novel approach to real-time dense visual SLAM.
