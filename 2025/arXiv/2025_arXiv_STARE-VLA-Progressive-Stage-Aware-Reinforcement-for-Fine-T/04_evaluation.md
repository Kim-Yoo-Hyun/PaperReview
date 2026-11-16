# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

SimplerEnv와 ManiSkill3의 조작 과제를 평가한다. 실제 로봇 결과로 확대하지 않는다.

## Metrics, Baselines, and Generalization

stage label·geometric/contact predicate·potential 경계·TPO/PPO 비용.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

arXiv v2 및 저자 project 확인. 검색 색인의 ICLR 표기는 공식 proceedings/forum으로 확인하지 못해 arXiv 2025로 유지한다. 공개 구현 URL은 식별하지 못했다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

동일 stage 정보에서 단순 potential shaping과 STARE식 갱신을 원 sparse 성공 지표로 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://arxiv.org/abs/2512.05107). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
