# Method

- Year/Venue: 2014 / ECCV
- Category: Foundations: SLAM and Sensor Geometry
- Tags: 3D Vision, SLAM, monocular geometry, 3D reconstruction
- Paper link: ./2014/ECCV/2014_ECCV_LSD-SLAM-Large-Scale-Direct-Monocular-SLAM/paper.pdf
- Code/Project: https://github.com/tum-vision/lsd_slam
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the environment.

## 원리적 동기
- The fundamental idea behind feature-based approaches (both filtering-based and keyframe-based ) is to split the overall problem – estimating geometric information from images – into two sequential steps: ...
- One of the major benefits of monocular SLAM – and simultaneously one of the biggest challenges – comes with the inherent scale-ambiguity: The scale of the world cannot ...
- We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the environment.

## 핵심 방법론
- Real-time monocular Simultaneous Localization and Mapping (SLAM) and 3D reconstruction have become increasingly popular research topics.
- Two major reasons are (1) their use in robotics, in particular to navigate unmanned aerial vehicles (UAVs) , and (2) augmented and virtual reality applications slowly making their ...
- One of the major benefits of monocular SLAM – and simultaneously one of the biggest challenges – comes with the inherent scale-ambiguity: The scale of the world cannot ...
- The advantage is that this allows to seamlessly switch between differently scaled environments, such as a desk environment indoors and large-scale outdoor environments.
- Scaled sensors on the other hand, such as depth or stereo cameras, have a limited range at which they can provide reliable measurements and hence do not provide ...
