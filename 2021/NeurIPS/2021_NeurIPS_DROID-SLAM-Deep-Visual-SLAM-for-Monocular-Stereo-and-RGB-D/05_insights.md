# Insights — DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **Robotics-enabling 3D perception**에서 3D representation과 state estimation이 downstream planning/control에 주는 실질적 효과를 판별하기 위한 기반로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: The SLAM problem has been approached from a number of different angles.
- Method cue: We introduce DROID-SLAM, a new deep learning based SLAM system.
- Result/evaluation cue: Despite training on monocular video, it can leverage stereo or RGB-D video to achieve improved performance at test time.

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation → DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras → 3D Gaussian Splatting for Real-Time Radiance Field Rendering`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- input/representation, temporal update, calibration, latency, uncertainty, downstream robot interface와 task-level metric
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- perception score와 closed-loop robot performance 사이의 causal link를 검증한다.
- 연결 gap: `G-03 / G-04 / G-13` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

동일 policy와 sensor budget에서 representation만 바꾸고 success, collision, latency와 stale-state failure를 비교한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
