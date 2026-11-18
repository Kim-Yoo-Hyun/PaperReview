# 석사 연구를 위한 VLA·Robotics 공백 탐색

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- 조사: 2026-11-11–12 KST / GAP-MASTERS-SCOUT
- 상태: **공백 후보 탐색 완료, CURATION-HYPOTHESIS**. 아래 순서는 이번 세 질문의 후속 검토 순서이며 논문 채택 확률·기존 11개 주제의 전체 재순위가 아니다.
- 근거: [22편 source·확인 범위](../sources/vla_masters_gap_scout_2026-11-12.json), [현재 후보](../research_topics/README.md), [비실험 buildup 절차](../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow). 논문 보고와 연구자 가설을 구별한다.

**같은 날 후속 N1/N2·P0-PREP 완료:** [직접 선행·통합 판단](../research_topics/unified_vla_rl/내용/README.md#langret-n1), [모델·비교 설계](../research_topics/unified_vla_rl/내용/README.md#langret-n2), [실행 준비·실제 확인](../research_topics/unified_vla_rl/재현%20방법/README.md#langret-p0-preparation)을 기존 UNIFIED의 두 폴더에 통합했다. 독립 방법 분리를 보류하고 보존 분석을 유지한다. P0-PREP의 전용 실행 파일5개·Docker stdlib22검사는 native 증거가 아니며 Mac GPU allocation 실패로 다음 LANGRET-P0는 호환 자원/구현 교정 대기다. 아래는 문헌 탐색 당시 기록이다.

**Registry 연결:** 초기 조사에서 미등록이었던8편은 [REG-R14](./REGISTRY_MAINTENANCE_2026-11-12.md)에서 표준5-note와 stable ID로 등록했다. 아래의 “등록 없음”은 조사 당시 결과이며 현재 등록 여부는 공통 원장의 `registry_id`를 따른다.

## 1. 결론과 선정 기준

**먼저 검토할 질문은 “단일 VLA를 RL로 적응시킬 때, 같은 장면에서 다른 유효한 지시를 수행하는 능력은 어떤 조건에서 보존되는가?”다.** 작은 단일 팔 조작에서 시작할 수 있고, 결과가 정책 후학습·데이터 선택 결정을 바꾸며, 단일 정책 내부 학습이라는 선호와 맞는다. 다만 일반적인 망각·언어 무시 현상의 재발견으로 끝날 위험이 크다. 새로운 방법을 먼저 정하지 않고 가장 가까운 반대 근거와 공개 비교 조건을 확인한다.

| 검토 순서 | 공백 후보 | 석사 연구 관점의 장점 | 핵심 위험·현재 판단 |
|---|---|---|---|
| **1** | **RL 후학습에서 지시별 행동 구분 능력의 보존 조건** | 단일 VLA·동일 로봇·공개 조작 환경에서 시작 가능. 획득 성능과 기존 목표 수행의 교환 관계를 분석할 수 있음 | RL 자체가 보존에 유리하다는 근거, replay·KL·추론 보정 선행이 강함. **작은 문헌/코드 검토에 투자할 가치 있음; 방법 신규성·효과 미확립** |
| **2** | **실행 중 바뀌는 제어 간격에 대한 VLA 적응** | 물리 시간과 실제 제어 문제에 직접 연결. 표현·학습·시스템 기여를 선택 가능 | 연속시간 표현·비동기 실행 선행과 controller 교정 비용. **예비 후보**, 일반 시간 조건화는 새 기여 아님 |
| **3** | **명령·경과 시간이 아닌 실제 수행 결과에 따른 기억 갱신** | 실패한 집기·미끄러짐 이후 잘못된 진행 판단이라는 구체적 로봇 문제 | 11/10 공개된 시간 지름길 진단·event indexing과 직접 중복. **독립 주제로 채택하지 않고 SET/FEEDBACK 보완 질문으로 보존** |

판단 기준은 문제의 중요성, 선행 대비 얻을 새 지식, VLA 행동과의 연결, 공개 자산, 구현·학습·실물 검증 부담이다. 제어기·새 센서·새 로봇·대규모 데이터 수집을 동시에 추가하지 않는 범위를 우선했다. 석사 기간·GPU 예산·실물 접근성이 미정이므로 소요 개월 수나 GPU 메모리 충족을 단정하지 않는다. 현상이 단순 대안으로 설명되더라도 초기에 탐색할 수 있으나, 그 경우 새 알고리즘 주장은 축소한다.

## 2. 문헌 조사 범위와 한계

기존 1,171편 registry에서 관련 논문을 찾고, 외부 검색으로 후학습·언어 조건화/보존, 실행 시간·행동 표현, 기억·진행 상태의 세 축을 대조했다. **CoRL 2024, NeurIPS 2025, ICLR·ICML·ECCV·RSS·ACL 2026 공식 페이지**와 최신 저자 preprint를 함께 사용했다. Top-tier 근거를 우선했으며 최신 preprint는 중복 위험 확인에 포함했다. 모든 venue·journal·registry 원문을 전수 조사한 systematic review는 아니다.

22편은 이 판단에 사용한 고유 논문 수다. 공식 metadata·초록을 기본으로 확인했고 RL4VLA, RL’s Razor, DeLock, TEMPO, CounterAlign은 지정 HTML 본문 절을 추가 대조했다. 최종 proceedings 버전과 preprint의 모든 변경을 검토한 것은 아니다. LIBERO-CF는 공개 README와 goal-condition 경로, 네 repository는 HEAD metadata까지 확인했다. 코드 존재는 실행 가능성이나 기본 정책 능력의 증거가 아니다.

CoRL 2024의 PMLR 출판 연도 2025를 행사 연도와 구별했다. VLA-CF의 CoRL 2026 Spotlight는 저자 페이지 주장만 확인했으므로 공식 채택 확정으로 쓰지 않는다. CounterAlign의 기존 CoRL 기록은 유지하되 이번 OpenReview 재접속 실패를 원장에 남겼다. 신규 발견 8편은 source 원장에만 기록했고, 이번에는 paper 등록·tier·사용자 reading status를 변경하지 않았다.

<a id="instruction-retention"></a>

## 3. 우선 후보: VLA 강화학습 후학습에서 지시별 행동 구분 능력의 보존 조건

### 문제와 가까운 선행

한 로봇을 특정 물체·목적지 작업에 적응시킨 뒤에도 사용자는 다른 물체·목적지를 지정할 수 있어야 한다. 적응한 작업의 성공률만 보면, 같은 장면에서 다른 목표를 수행하는 능력의 변화를 놓칠 수 있다. 여기서 관심은 언어 답변의 정확도가 아니라 **지시에 맞는 물체 선택·이동·놓기를 실제로 완료하는가**다.

| 직접 근거 | 이미 알려진 것 / 이번 검토 범위 | 새로 주장하지 않을 것 |
|---|---|---|
| [Contrast Sets, CoRL 2024](https://proceedings.mlr.press/v270/anwar25a.html) | 작은 표적 변화로 language-guided robot policy를 평가; 공식 초록 | 지시 대비쌍 평가 자체 |
| [RL4VLA, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html), [v4 §4–5.3](https://arxiv.org/html/2505.19789v4) | RL의 semantic generalization, 새 object/receptacle·표현·다중 물체 조건을 이미 평가 | RL의 언어 일반화가 연구되지 않았다는 주장 |
| [RL’s Razor, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html), [v1 §B.2](https://arxiv.org/html/2509.04259v1) | 같은 새 과제 성능에서 RL이 SFT보다 기존 능력을 보존. 로봇 비교는 can grasp/lift 적응과 별도 drawer 작업; 새 과제 분포의 KL과 보존 관계 | “RL이 망각을 일으킨다”, RL/SFT 보존 비교나 KL 설명 자체 |
| [VLA continual learning, ICML 2026](https://proceedings.mlr.press/v306/liu26bu.html) | Pretraining의 망각 저항성과 단순 experience replay의 강한 성능; 초록 | 충분히 조정한 replay를 제외한 새 보존 방법 |
| [DeLock, arXiv 2026](https://arxiv.org/html/2604.23121v1) | §3.1–3.3: 적은 데이터 SFT의 concept/spatial lock-in, visual grounding 보존·contrastive prompt guidance | 후학습 이후 언어 조종 가능성 저하의 발견, 단순 SFT→RL 교체 |
| [TEMPO, arXiv 2026](https://arxiv.org/html/2608.07314v1) | §IV-A/B: frozen VLM과 semantic projection/action expert의 분리 RL 갱신 | 의미 모듈 동결·학습 속도 분리 자체 |
| [VLA-CF / LIBERO-CF](https://vla-cf.github.io/), [공개 코드](https://github.com/yuffish/VLA-CF) | 같은 layout의 다른 유효 지시, counterfactual action guidance. 단, focused suite는 원 학습 대상을 제거하므로 그대로 same-scene 통제로 쓰면 안 됨 | Language shortcut 진단이나 두 branch 추론 guidance 자체 |
| [CounterAlign, CoRL 2026 기존 등록 / v1 본문](https://arxiv.org/html/2608.21740v1) | §3·Appendix 6: instruction/action 재표기, similarity threshold·unlabeled 처리, offline advantage-weighted 학습 | 모든 다른 지시를 negative로 처리하거나 counterfactual reward 학습을 새로 제안 |
| [IGAR, ECCV 2026](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3), [RSS, ACL 2026](https://aclanthology.org/2026.acl-long.190/) | 초록: instruction contradiction의 attention 보정, 의미 표현 확장·잔차 steering이라는 강한 대안 | 불가능한 지시에 멈춘 것을 유효한 다른 목표의 수행 성공으로 해석 |
| [Embodied Interpretability, ICML 2026](https://proceedings.mlr.press/v306/zhang26gz.html) | 시각 개입·task-irrelevant region과 일반화 진단; 초록 | Attention/embedding 변화만으로 언어 원인·행동 보존을 입증 |

**남겨 둘 질문 — 연구자 해석:** 동일한 물리 상태에서 두 유효 목표 A/B를 수행하던 정책을 A 중심으로 RL 적응시킬 때, 새 과제 성능과 총비용을 맞춰도 목표 B의 보존 조건에 차이가 남는가? **학습 분포에서 측정한 KL·일반 replay로 충분히 설명되는지**, 아니면 관측–목표 조합의 학습 범위를 별도로 고려해야 하는지를 확인한다. 확인한 선행의 robot 비교 범위를 좁혀 묻는 것이며, 이 조건이 문헌 전체에서 미해결이라고 확정하지 않았다. 분포 밖 행동이 학습 분포 KL만으로 보장되지 않는 일반 사실도 새 이론으로 내세우지 않는다.

### 한 페이지 연구 이야기와 구별할 예측

예상 기여는 **“다른 지시 수행 능력을 희생하지 않는 VLA 적응을 선택하기 위한 조건과 측정 근거”**다. 지시 무시 현상 하나를 추가로 보이는 것으로는 부족하다. 기존 지표와 baseline 이후 남는 조건을 찾고, 그것이 학습 선택을 바꾸는지를 보여야 한다. 잔여 효과가 확인될 때만 단일 정책의 학습 목적·보존 데이터 구성 개선을 검토한다. Goal-balanced replay·KL·동결은 출발 baseline이며 그 자체로 신방법이 아니다.

| 가능한 설명 | 구별할 관측 | 결과에 따른 판단 |
|---|---|---|
| 원 정책이 B를 애초에 못함 | 적응 전 두 목표의 native 성공·오류 유형 | 보존 연구의 해당 pair에서 제외; 기본 언어 grounding 문제로 분리 |
| 단순 update 크기·KL·replay 부족 | 같은 적응 성능에서 보존 곡선과 조정된 단순 baseline | 충분하면 적용 범위 확인으로 축소; 독립 보존 방법을 추가하지 않음 |
| 특정 관측–목표 조합에 편중된 학습 | 전체 transition·성공 데이터·update/compute를 맞춘 목표 구성 대조 | 다른 scene/seed에서도 반복되고 의사결정을 바꿀 때 조건 분석 기여 검토 |
| 입력은 읽지만 조작 능력이 부족함 | 목표 물체 선택·집기·놓기 실패를 terminal success와 분리 | 언어 보존 손실로 일괄 집계하지 않음 |
| 보존 차이가 RL 고유 효과가 아님 | 같은 수집 자료의 성공 선택/return-weighted imitation 대조 | RL objective 효과 주장 축소; 자료/목표 구성 설명으로 수정 |

### 최소 비교 초안 — 미실행

- **범위:** 한 single-arm simulator·한 base VLA·유효 목표쌍 두 종류부터. 서로 다른 물체 선택과 서로 다른 목적지 선택이 가능한 공개 scene을 후보로 둔다. 실제 pair identity와 시작 정책의 양쪽 능력은 아직 미확인이다. 공개 [OpenVLA](https://proceedings.mlr.press/v270/kim25c.html), [RLinf-VLA](https://www.roboticsproceedings.org/rss22/p089.html), LIBERO-CF를 출발 자산으로 비교하되 서로 다른 action head·backend를 임의로 호환된다고 쓰지 않는다.
- **공정성:** 같은 시작 weight·normalizer·관측·controller·action 의미·초기 상태·reward/evaluator를 쓴다. Fixed total rollout/update 비용 비교와 새 과제 성공 수준을 맞춘 비교를 별도로 보고한다. 후자는 validation에서 사전에 정한 checkpoint 선택 규칙을 쓰고 held-out 결과로 가장 좋은 checkpoint를 고르지 않는다. 성공 수준을 못 맞춘 경우 불일치를 보고한다.
- **강한 baseline:** 미적응 정책, vanilla RL, 일반 KL anchor 또는 teacher/BC replay, backbone freezing. 필요하면 DeLock/CAG/IGAR/RSS 계열 추론 보정을 비교하고 추가 forward·latency를 센다. 첫 pilot에 모든 방법을 구현하지 않으며 직접 차별점을 판단하는 대안을 먼저 고른다.
- **관측:** A/B 각각 성공률, 같은 reset 조건에서 두 지시를 모두 만족한 비율, 잘못 선택한 물체/목적지, 적응 성능–보존–계산 비용 곡선. Action distance는 보조 진단이다. 다른 최종 목표라도 초기 접근 동작이 같을 수 있으므로 모든 chunk를 멀어지게 강제하지 않는다. 정지·아무것도 하지 않음이 낮은 오선택률로 보상되지 않게 task completion을 함께 본다.
- **분할·불확실성:** 개발용 pair/상태와 최종 평가 상태·지시 표현을 분리한다. Paired reset은 물리 상태를 일치시키는 장치이며 서로 다른 목표의 유효성은 별도 확인한다. 학습 seed와 task/scene을 보고 단위로 두고 프레임·chunk를 독립 학습 반복처럼 세지 않는다. 반복 수·성공 기준·예산은 N1 이후 작은 실행 계획에서 정하며 현재 수치 결과는 없다.
- **방법으로 확장할 조건:** 적응 성능을 유지하면서 강한 대안 이후 일관된 보존 차이가 남고, 조건을 바꾸면 사전 예측이 맞으며, 새로운 scene/goal 또는 두 번째 backbone에서 유효성을 보일 수 있어야 한다. 한 모델의 작은 비율 차이만으로 top-tier 기여를 주장하지 않는다. 실물 일반화는 별도 real-robot 검증이 있을 때만 주장한다.

### 석사 적합성과 다음 비실험 검토

하드웨어 제작·새 데이터 수집 없이 시작할 경로가 있고 하나의 학습 loop에 질문을 집중할 수 있어 세 후보 중 초기 부담이 상대적으로 작다. 그러나 온라인 VLA 학습, 여러 checkpoint 평가, 복수 seed에는 NVIDIA 자원과 구현이 필요하다. **7B 공개 모델이라는 이유로 단일 24GB GPU에서 RL이 가능하다고 가정하지 않는다.** 추론이 가능해도 rollout 병렬화·optimizer·reference model 비용은 다르다. 실제 모델·GPU 예산은 미정이다.

**GAP-LANGRET-N1의 완료 기준:** RL’s Razor 최종본과 DeLock/TEMPO/CounterAlign의 가장 가까운 비교·공개 구현 범위를 확인하고, LIBERO-CF에서 **동일 scene·서로 유효한 목표·관측/action 계약을 만족할 수 있는 두 pair의 source 위치**를 정리한다. 지원 checkpoint·기본 능력은 확인/미확인을 구분한다. 추가 검색으로 순위를 반복하지 않고, 이 결과로 기존 UNIFIED에 합칠지 별도 좁은 분석으로 진행할지 결정한다. 선행이 정확히 같은 질문에 답했다면 그 결과를 적용할 검증만 남긴다. Native competence를 비실험 단계에서 통과시키려 하지 않는다.

외부 검토 질문은 “KL·replay의 알려진 한계 설명을 넘어 어떤 로봇 학습 결정을 바꾸는가?”, “같은 상태의 두 목표가 유효하고 원 정책이 둘 다 가능한가?”, “보존 방법 추가 없이 충분한가?”다. 실제 독립 연구자 응답은 미수신이고 외부 전송은 하지 않았다.

<a id="control-interval"></a>

## 4. 예비 후보: 실행 중 바뀌는 제어 간격에 대한 VLA 적응

**논문 근거:** [RTC, NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html)는 비동기 chunk 실행, [RTR, ICML 2026](https://proceedings.mlr.press/v306/wang26lj.html)는 고주파 latent chunk와 reuse/refine, [CAT, ECCV 2026](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24)는 고정 실제 시간 구간의 연속 행동 표현·frequency-aware encoding을 다룬다. [PaceVLA](https://arxiv.org/abs/2610.25961)는 적응적 시간 양자화, [PTS](https://arxiv.org/abs/2611.01390)는 고정 VLA 경로의 실행 시간 단축, [LIBERO-RIG](https://arxiv.org/abs/2610.18843)는 제어 주기를 포함한 hardware-setup robustness를 다룬다. 마지막 세 편은 arXiv status로 구별한다. 이번 근거는 초록 범위다.

**남겨 둘 질문 — 연구자 해석:** 정책 바깥의 일정 때문에 episode 중 command 간격이 바뀌고 contact phase와 겹칠 때, 같은 VLA의 time-conditioned 학습/RL이 단순 resampling·RTC·주기 randomization 이상의 가치를 주는가? “여러 주기를 지원한다”만으로는 CAT와 구분되지 않는다. CAT/RTR의 본문·code가 within-episode 변화를 이미 처리하는지 먼저 확인해야 한다.

최소 비교는 고정 controller/sensor clock·action 단위에서 command 간격만 조절하고, 동일 물리 시간·최대 query budget으로 기존 실행기와 비교하는 것이다. 추론 지연, 관측의 오래됨, 정책 호출 간격, 저수준 servo 주기를 혼합하면 원인을 알 수 없다. 자연스러운 지연 trace와 action의 velocity/delta/target 의미도 필요하다. 첫 범위는 기존 single-arm 접촉 task 하나이며 mobile robot·실물 시간 보장까지 넓히지 않는다.

**판정:** 실제 로봇에 직접적이지만 controller 교정·동기화·새 학습 비교 비용이 1순위보다 높다. 보간/RTC/기존 representation만으로 충분하면 시스템 적용으로 축소한다. 기존 E2의 timing NO-GO/HOLD를 해제하는 우회 경로가 아니며 CONTACT의 sensor/gain 준비를 이 질문의 검증으로 재사용하지 않는다. 현재 후속 구현 없이 예비 카드로 남긴다.

<a id="outcome-memory"></a>

## 5. 통합 보존: 실제 수행 결과에 따른 기억 갱신

**논문 근거:** [RoboMME, ICML 2026](https://proceedings.mlr.press/v306/dai26c.html)는 memory 평가·설계 비교를, [ActMem-VLA, arXiv 2026](https://arxiv.org/abs/2609.37307)는 action-history memory를 다룬다. 특히 **11/10 공개된 [Is Your Robot’s Memory Just a Clock?](https://arxiv.org/abs/2611.14488)**는 pause/fidget의 가짜 진행, time-sampled memory의 지름길과 event-indexing 대안을 직접 보고한다. 초록·공개 repository metadata를 확인했으며 실험을 재현하지 않았다.

따라서 “시간이 흘러도 작업은 안 됐는데 기억만 진행한다”, “event 기반 memory를 쓰자”를 새 기여로 채택하지 않는다. 남길 수 있는 질문은 물체를 집으려 했지만 실패하거나 놓은 뒤 미끄러져 목표가 취소된 경우, **실제 목표 상태와 command history의 불일치**를 어떤 정보로 구분하는가다. 이조차 위 최신 연구의 본문·failure coverage와 기존 outcome-aware memory를 확인하기 전에는 독립 공백으로 승격하지 않는다.

기존 [SET](../research_topics/retired/README.md#object_set)의 진행/수량 진단과 [FEEDBACK](../research_topics/visual_feedback/내용/README.md)의 물리 변화 이후 관측 활용에 연결한다. 결과를 아는 oracle progress를 policy에 주는 조건은 상한 비교로 구분하며 배포 가능한 해결책처럼 쓰지 않는다. 새 12번째 memory topic이나 GPU 실행 자료는 만들지 않는다.

## 6. 기존 후보와 겹치는 부분·보존할 판정

| 기존 후보 | 이번 1순위와의 관계 |
|---|---|
| UNIFIED | 같은 scene에서 지시가 행동을 바꾸는 평가를 공유할 수 있다. 기존은 value-loss routing의 효과, 이번은 post-training 전후 목표 능력 보존과 학습 범위다. 실제 독립 설명이 없으면 **UNIFIED 하위 분석으로 통합**한다. Backend/정규화 호환성 확인 전 실행 코드를 합치지 않는다 |
| REVISION / SET | Episode 도중 지시 수정·제약 철회, 수량/진행 판단이 중심. 이번은 episode 시작 지시를 고정하고 학습 업데이트 전후를 비교 |
| FEEDBACK | 물리 변화 이후 fresh/stale 관측의 가치가 중심. 이번은 fresh 관측을 고정한 다른 목표의 수행 능력 |
| HINDSIGHT / ALLOC | 실패 재표기의 원 과제 전이, 수집 과제 배분의 비용이 중심. 목표 coverage를 단순 배분 최적화로 바꾸면 해당 주제에 통합 |
| CONTACT / VRL / HANDOFF | Impedance 적응, base 교체 후 residual 재사용, 이동→조작 정책 교체의 문제. 이번에는 controller·base 교체를 추가하지 않음. 기존 P0 자원/구현 대기를 유지 |
| RETRIEVAL / CODEC1 | 시연 검색 집합 확장, 행동 양자화 문제. 이번에는 reference 입력 확대·새 codec이 필요하지 않음 |
| 과거 GAP-RETENTION / C1–C6·D1–D3·E1/E2 | 일반 continual-learning 방법 보류와 과거 NO-GO/HOLD를 유지. 새 RL’s Razor 근거를 포함한 좁은 재검토이며 같은 계획의 자동 재개가 아님 |

## 7. 초기 공백 탐색 당시 완료 범위와 인계

| 비실험 buildup 단계 | 이번 상태 |
|---|---|
| 1 문제와 독자 | 세 질문을 실제 로봇 사용 상황에 연결 |
| 2 가까운 선행 | 22편 metadata/초록·5편 지정 본문·공개 README/metadata 대조. 1순위 최종본/직접 code 비교는 N1에 남음 |
| 3 질문과 대안 | 1순위 반대 근거·단순 설명·축소 조건 정리; 다른 두 후보의 직접 중복 명시 |
| 4 짧은 논문 이야기 | 조건 분석 중심 초안. 새 방법·결과·독립 기여는 미확정 |
| 5 최소 비교 | 목표쌍·비용·baseline·결과 해석 초안. 실제 pair identity·평가기·상한은 미확정 |
| 6 실행 부담 | 공개 출발 자산 및 주요 구현 의존성 확인. 지원 GPU·dependency·native 실행 검증 없음 |
| 7 외부 비판 | 질문 준비, 실제 피드백 미수신 |

탐색 당시 다음 행동은 GAP-LANGRET-N1이었으며, **후속 심사 결과는 상단의 두 폴더 문서, 현재 다음 행동은 [TODO](../../TODO.md)**를 따른다. CONTACT-P0 등 이미 준비한 native 실험은 기존 자원/구현 대기로 보존한다. 이번은 문헌 탐색 요청이므로 Docker 재측정·실험·dependency/weights/PDF 다운로드는 하지 않았다. 기존 11개 dossier와 과거 연구 gate, canonical registry·사용자 읽기 기록을 유지했다. 새 결과가 없으면 같은 광범위 검색을 반복하지 않는다.

검증 결과는 위 source 원장의 `validation`에 기록한다. 이번 보고서는 다주제 공통 탐색 기록이며, 후속에 별도 주제로 채택되면 `내용/`·`재현 방법/` 두 폴더에 통합하고 날짜별 유사 보고서를 늘리지 않는다.
