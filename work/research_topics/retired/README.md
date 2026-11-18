# 폐기한 연구 후보 — 핵심 결과와 판단

- Decision: 2026-11-17 / 사용자 요청에 따른 연구 포트폴리오 정리
- 아래 7개는 `RETIRED`이며 실험 대기 queue가 아니다. GPU 확보만으로 재개하지 않는다.
- 폐기는 연구자 투자 판단이며 분야 전체의 무가치·가설 반증을 뜻하지 않는다.
- 결과와 해석에 필요한 계약 7파일은 `evidence/`에 보존했다. 실행 code/dependency recipe·상세 설계는 활성 workspace에서 제거했다.
- [현행 후보](../README.md) · [삭제·이동 원장](../../sources/candidate_triage_2026-11-17.json)

보존한 JSON의 당시 경로·hash·status는 역사적 실행/감사 근거다. 현재 실행 명령으로 사용하지 않으며 bytes를 고치지 않았다. 탐색 재진입에 효과 입증을 미리 요구하지 않지만 같은 설계에 대한 자동 실행은 종료한다.

<a id="action_tokenization"></a>
## 행동 토큰화의 실행 구간 복원 (CODEC1)

**폐기 이유:** 기존 CPU 결과는 알려진 양자화·복원 특성의 범위를 벗어나지 못했다. 실제 codec/정책 선택을 바꾸는 증거 없이 독립 방법으로 확장할 이유가 약하다.

**실제 확보한 결과·한계:** 20 episode·101 window의 offline 진단은 실제 결과다. Robot rollout 101회 또는 정책 성공 개선은 아니다.

**재사용할 핵심:** 복원 오차와 행동 성능을 분리하는 평가 원칙.

관련 선행: [source 1](https://arxiv.org/abs/2610.09170). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/action_tokenization). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.

- [보존한 CONTRACT.json](evidence/action_tokenization/CONTRACT.json)
- [보존한 CONTRACT_SUFFIX.json](evidence/action_tokenization/CONTRACT_SUFFIX.json)
- [보존한 runtime.json](evidence/action_tokenization/results/runtime.json)
- [보존한 results.json](evidence/action_tokenization/results/verified/results.json)
- [보존한 results.json](evidence/action_tokenization/results/suffix_verified/results.json)

<a id="context_retrieval"></a>
## 시연 저장소 확장과 기존 과제 성능 보존 (RETRIEVAL)

**폐기 이유:** Cross-task 검색의 도움/간섭은 이미 선행에 있고 목표별 분리보다 나은 기여가 좁다. 시연 성공·평가 독립성 provenance와 native 입력까지 별도 확보해야 해 투자 효율이 낮다.

**실제 확보한 결과·한계:** 12,840,960-byte archive hash와 261개 frame 등 CPU 자산 감사를 수행했다. 성공 시연 인증·정책 효과는 미검증이다.

**재사용할 핵심:** 검색 자료의 identity·성공·평가 중복을 구분하는 원칙.

관련 선행: [source 1](https://arxiv.org/abs/2610.05492). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/context_retrieval). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.

- [보존한 ASSET_AUDIT.json](evidence/context_retrieval/ASSET_AUDIT.json)
- [보존한 COMPARISON_CONTRACT.json](evidence/context_retrieval/COMPARISON_CONTRACT.json)

<a id="object_set"></a>
## 물체 집합 선택·수량 지시 (SET)

**폐기 이유:** 단순 k회 반복·외부 counter 이후 남는 실패가 확인되지 않았고 counting/조합 benchmark와 겹친다. 현재 RL·시각 신뢰성 중심 연구와의 연결보다 evaluator 구축 부담이 크다.

**실제 확보한 결과·한계:** 비실험 설계와 Docker 제어/준비 검사만 수행했다. Native 다중 물체 능력·수량/선택 효과는 미검증이다.

**재사용할 핵심:** 수량 오류를 객체 grounding·진행 상태·운동 실패로 나누는 평가 항목.

관련 선행: [source 1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/object_set). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.


<a id="mobile_policy_transfer"></a>
## 모바일 조작 정책 교체와 접근 조건 전이 (HANDOFF)

**폐기 이유:** 기존 policy mobilization 이후 남는 질문이 좁고 현재 한 scene template로 일반성을 보이기 어렵다. Mobile stack·transport·동일 상태 분기 구현 부담이 석사 주력 후보의 기여 기대에 비해 높다.

**실제 확보한 결과·한계:** 단일 scene template·자원/정적 source 검토와 실행 설계만 있다. 실제 도착→정지→A/B 분기와 정책 비교는 미실행이다.

**재사용할 핵심:** 정책 교체 시 접근 조건 재검증과 전반적 조작 능력의 분리.

관련 선행: [source 1](https://proceedings.mlr.press/v305/yang25b.html). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/mobile_policy_transfer). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.


<a id="task_allocation"></a>
## 계산 예산을 고려한 다중 과제 VLA RL (ALLOC)

**폐기 이유:** 샘플 배분·가중치·group variance의 일반 RL 문제로 수렴하며 현재 설계의 CV/로봇 고유 기여가 약하다. 단순 uniform/비용 보정 대비 이득이 미확인인 상태에서 여러 학습 run을 투자할 우선순위가 낮다.

**실제 확보한 결과·한계:** N2-R1 설계와 CPU 제어24검사만 수행했다. Native 학습비용·성능·allocator 효과는 미측정이다.

**재사용할 핵심:** Episode 수와 실제 GPU/환경 비용을 분리하고 고정 배포 목적을 유지하는 실험 원칙.

관련 선행: [source 1](https://arxiv.org/html/2608.17423v1) · [source 2](https://arxiv.org/html/2610.15888v1). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/task_allocation). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.


<a id="hindsight_transfer"></a>
## 원 과제 전이를 고려한 hindsight 목표 선택 (HINDSIGHT)

**폐기 이유:** LfH 등 이후 남는 차이는 유효한 재라벨 간 선택이라는 좁은 부분이다. 동일 실패·라벨 정확성·원 목표 전이·sampling support를 함께 맞춘 학습의 부담에 비해 방법 근거가 약하다.

**실제 확보한 결과·한계:** A/B 비교·분할·공통 loss 설계와 CPU 제어15검사만 있다. 자연 witness·native 효과는 미확인이다.

**재사용할 핵심:** 성공/실패 데이터와 원 목표 관련성을 구분하는 baseline.

관련 선행: [source 1](https://arxiv.org/abs/2607.09042). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/hindsight_transfer). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.


<a id="vla_residual_update"></a>
## VLA 교체 후 residual RL 재사용·적응 (VRL)

**폐기 이유:** Base A의 residual 학습과 B 적응을 모두 해야 하며 정확한 A→B 계보·B 자체 우월성도 미확정이다. Warm-start·gain·동일 데이터 모방 뒤에 남는 독립 원리의 근거가 비용에 비해 약하다. 단지 계층형이라서 폐기한 것은 아니다.

**실제 확보한 결과·한계:** Native A/B IO·residual 유용성은 미검증이다. 기존 Docker CPU 제어9검사는 준비 증거다.

**재사용할 핵심:** Residual·action editing은 다른 retained 후보의 강한 비교군으로 계속 사용 가능.

관련 선행: [source 1](https://arxiv.org/html/2606.18953v1) · [source 2](https://arxiv.org/html/2511.00091v1). 이 중 일부는 기존 dossier 검토 근거이며 이번 재검토 범위는 source 원장에 구분한다.

[폐기 전 전체 기록·코드](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/vla_residual_update). 재탐색은 다른 중요한 로봇 문제나 판단을 바꾸는 새 문헌·논리·데이터가 있을 때 작은 비교로 시작한다. GPU 확보만으로 같은 계획을 자동 재개하지 않는다.
