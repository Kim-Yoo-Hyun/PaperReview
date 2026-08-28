# Evaluation — A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1968 / IEEE Transactions on Systems Science and Cybernetics
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, graph search, A*
- Official paper: https://doi.org/10.1109/TSSC.1968.300136
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof details and experimental claims remain UNVERIFIED.

## Protocol

이론적 성질과 search-efficiency 분석이 중심이며 modern robot benchmark 평가는 없다.

## Limitations and Reproducibility

연속 동역학, 접촉, 불확실성과 learned heuristic은 직접 다루지 않는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
