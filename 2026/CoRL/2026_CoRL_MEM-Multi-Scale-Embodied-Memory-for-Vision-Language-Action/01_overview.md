# MEM: Multi-Scale Embodied Memory for Vision Language Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Marcel Torne, Karl Pertsch, Homer Walke, Kyle Vedder, Suraj Nair, Brian Ichter, Allen Z. Ren, Haohuan Wang, Jiaming Tang, Kyle Stachowicz, Karan Dhabalia, Michael Equi, Quan Vuong, Jost Tobias Springenberg, Sergey Levine, Chelsea Finn, Danny Driess
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, episodic memory, long-horizon manipulation
- Official paper: https://arxiv.org/abs/2603.03596
- Code/Project: https://pi.website/research/memory

## 연구 질문과 기여

짧은 시각 이력과 긴 의미 이력을 다른 형식으로 보존하는 로봇 정책이다.

최근 관측 비디오는 압축하고 장기 이력은 텍스트로 표현한다. 실제 장시간 조작에서 이력에 따른 행동 적응을 평가한다.

## 평가 범위

실제 다단계 조작에서 메모리 없는 정책과 단일 기억 표현을 비교했다. [원문 및 평가 절](https://arxiv.org/pdf/2603.03596#page=7)

## 선정 근거

단기 영상 이력과 장기 의미 이력이 서로 다른 행동 오류를 해결하는지 시험할 기준이다.
