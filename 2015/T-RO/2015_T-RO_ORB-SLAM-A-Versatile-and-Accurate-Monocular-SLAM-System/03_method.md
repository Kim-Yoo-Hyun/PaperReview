# Method

- Year/Venue: 2015 / T-RO
- Category: Foundations: SLAM and Sensor Geometry
- Tags: SLAM, calibration, geometry
- Paper link: ./2015/T-RO/2015_T-RO_ORB-SLAM-A-Versatile-and-Accurate-Monocular-SLAM-System/paper.pdf
- Code/Project: https://github.com/raulmur/ORB_SLAM2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present an exhaustive evaluation in 27 sequences from the most popular datasets.

## 원리적 동기
- —This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments.
- The system is robust to severe motion clutter, allows wide baseline loop closing and relocalization, and includes full automatic initialization.
- We present an exhaustive evaluation in 27 sequences from the most popular datasets.

## 핵심 방법론
- ORB-SLAM + Global BA (20 its.) Time (s) Pose Graph Edges RMSE (m) Dimension (m×m) RMSE (m) Time BA (s) - - 48.77 KFs RMSE (m) - Sequence ...
- Number between brackets for BA (Bundle Adjustment) means number of Levenberg-Marquardt (LM) iterations, while for EG (Essential Graph) is the θmin to build the Essential Graph.
- All EG optimizations perform 10 LM iterations.
