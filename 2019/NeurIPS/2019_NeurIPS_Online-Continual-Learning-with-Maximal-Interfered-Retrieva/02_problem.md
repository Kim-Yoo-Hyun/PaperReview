# Online Continual Learning with Maximal Interfered Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Continual 학습에서 과거 memory를 무작위로 고르는 한계를 다룬다.

## Bottleneck and Changed Formulation

예상 parameter update 뒤 손실이 많이 증가할 sample을 선택해 replay한다.

## System and Robotics Loop

현재 minibatch·stored memory → virtual update → 간섭 score.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

virtual step, candidate memory budget, classification과 robot rollout의 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Continual learning benchmark에서 경험/생성 replay 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) · [저자 project/code](https://github.com/optimass/Maximally_Interfered_Retrieval). Exact objective, constraints, success definition은 본문 수동 확인 필요.
