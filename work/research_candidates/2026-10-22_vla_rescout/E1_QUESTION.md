# E1 — 로봇 추가 학습에서 행동 충돌의 의미와 replay 효율

- 날짜: 2026-10-22
- 단계: **CURATION-HYPOTHESIS / 최초 탐색 card**. 후속 [E1 buildup 결과](../2026-10-22_e1_buildup/README.md)가 현재 판단을 대체한다: REVISE·진단 HOLD, 새 replay 방법 채택 보류.
- [탐색 결과](./README.md) · [문헌 P1–P16](./LITERATURE.md)
- Native 정책 실행 0회. 아래는 연구자 제안이며 검증 결과가 아니다.

## 1. 문제와 연구 질문

이미 로봇 A에서 여러 작업을 하는 VLA에 로봇 B의 demonstration을 추가한다고 하자. 새 로봇의 능력을 얻으면서 A의 능력을 유지하고, 저장할 과거 데이터와 학습 비용을 제한하고 싶다. 로봇별 모델을 모두 따로 보존하는 방법도 유효한 대안이므로 처음부터 공유 모델의 우월성을 가정하지 않는다.

질문은 **“로봇이 바뀔 때 replay가 보호해야 할 경험을 command-space disagreement로 판단해도 되는가? 실제 물리적 효과의 차이를 기준으로 판단하면, 단순 정렬·균형 replay 이후에도 기존 능력 보존을 더 잘 설명하거나 개선하는가?”**다.

예를 들어 다른 관절 구성의 두 팔이 물체를 동일한 방향으로 옮길 때 관절 명령은 다르다. 반대로 같은 숫자의 명령도 frame·gain·시간 간격이 다르면 다른 효과를 낼 수 있다. 이는 일반적인 제어 사실이다. **이 차이가 실제 VLA의 replay 순위를 왜곡하고 forgetting을 유발한다는 부분이 미검증 가설**다. 좌표 변환 예시만으로 논문 기여를 주장하지 않는다.

## 2. 선행이 이미 해결한 범위

| 선행 | 그대로 가져오면 새롭지 않은 부분 | E1에서 남겨 볼 비교 |
|---|---|---|
| P4 ICML continual VLA | 강한 replay, pretraining 효과, 모듈 교환과 빠른 재학습 | 새 로봇 추가 시에도 기본 replay로 충분한지 먼저 확인 |
| P10 Memory Anchors | latent overlap과 action disagreement로 과거 경험 선택 | 그 disagreement가 이질적 action 의미에서도 적절한지 |
| P12 실환경 continual v3 | normalization 일관성, 단일 팔/양팔 stream, replay 비대칭 배분 | 다른 하드웨어와 task 변화의 효과를 분리하되 단순 normalization·reweighting과 비교 |
| P2/P6/P11/P15 | 통일된 물리적 action 표현, cross-embodiment 학습/전이 | 정렬만으로 충돌 판단과 retention 문제가 사라지는지 |
| P9/P13 | adapter 분리·확장·routing과 action-space MoE | 용량과 저장 비용을 맞춘 독립/분리 모델이 더 나은지 |

P10은 서로 다른 데이터 행의 raw action을 단순 비교하는 방법이 아니다. 현재 정책으로 **새 데이터의 action을 noise–denoise하여 disagreement를 측정**한다. 따라서 비교 시에는 이 원래 estimator를 보존해야 한다. 출력 차원이 다른 로봇에 정의되지 않는 estimator를 억지로 적용해 약한 baseline을 만들지 않는다. [원문 §4](https://arxiv.org/html/2608.26545v1#S4).

## 3. 잠정 가설과 반대 설명

**H1:** 새로운 로봇의 데이터에 대해 측정한 action disagreement에는 재사용 가능한 행동의 실제 충돌과 제어 interface 차이가 섞일 수 있다. 비교 가능한 물리 공간에서 둘을 분리하면, 동일한 replay 예산에서 과거 task의 성능 하락을 더 잘 예측한다.

**H2:** H1의 예측력이 확인되면 그 구분을 replay 선택에 이용하여, 새 로봇의 학습을 희생하지 않고 과거 능력 보존을 개선할 수 있다. H1이 성립해도 H2는 별도 검증이 필요하다.

반대 설명은 다음과 같다.

- 공통 frame·단위·normalizer·유효 action mask를 올바르게 적용하면 이미 충분하다.
- task/robot별 replay 비율 또는 더 많은 replay update가 성능 차이의 전부다.
- 카메라·배경·작업 난도가 달라 생긴 visual-domain shift다.
- 추정된 물리 효과가 노이즈를 줄인 것이 아니라 simulator GT나 미래 정보를 추가한 것이다.
- 명령의 물리적 차이는 기계적 실패만 설명하며 shared representation의 forgetting과는 관계없다.
- encoder freeze 또는 독립 adapter가 더 단순하고 비용 효율적이다.

이 중 하나로 충분히 설명되면 새로운 replay 방법을 만들 이유가 약해진다.

## 4. 비교 가능한 효과와 정보 경계

초기 범위는 **단일 팔 + parallel gripper의 공통으로 실행 가능한 task**로 제한한다. 다른 DoF 자체를 연구 효과로 삼거나 manipulation과 navigation을 한 action vector로 섞지 않는다.

비교에 필요한 후보 정보는 RGB, 언어 지시, proprioception, 기록된 EE pose, action frame·단위·timestamp·controller semantics, 유효 action mask다. 이들 필드가 실제 공개 자료에 함께 있는지는 E1-L1에서 확인한다. 로봇 ID는 알려진 deployment metadata로 모든 baseline에 동일하게 제공한다.

정렬된 EE displacement/rotation, gripper event, 필요할 때 object-relative motion을 후보 비교량으로 삼을 수 있다. 그러나 **EE 경로가 같다는 것이 contact force·object outcome까지 같다는 뜻은 아니다.** 초기에는 비교 가능한 task 구간만 포함하고 contact outcome은 별도 평가한다. Rotation은 물리적 회전 차이로 비교하고 단위·시간 간격을 명시한다. Missing pose나 incompatible actuator를 0으로 채워 유효한 비교로 만들지 않는다.

최소한 다음을 분리한다.

| 조건 | 보존하는 것 | 바꾸는 것 | 목적 |
|---|---|---|---|
| Interface-only 대조 | 로봇·물리 trajectory·task | 알려진 action 표현 | estimator의 표현 의존성 확인. 이것만으로 연구 효과 입증 불가 |
| Embodiment 대조 | 공통 task·instruction·가능한 effect 범위 | 실제 로봇 | 표현 오류를 제거한 후 남는 전이/retention 문제 |
| Task 대조 | 같은 로봇·interface | task의 요구 행동 | 기존 Memory Anchors가 다루는 진짜 task conflict |
| Joint 변화 | 평가 가능한 공통 task 기준 | 로봇과 task | 앞의 두 효과와 구분한 확장. 첫 pilot에서 제외 가능 |

서로 다른 로봇의 관측을 완전히 같게 만들 수 있다고 가정하지 않는다. 카메라/scene 차이를 기록하고 matched subset 또는 별도 요인으로 통제한다. Policy effect와 데이터 품질 차이를 분리할 수 없으면 해당 pair는 채택하지 않는다.

## 5. 최소 비교와 측정

구현 전 확정할 비교 가족은 다음과 같다. 현재 executable manifest는 없다.

1. Sequential SFT와 동일 저장 예산의 uniform replay.
2. Robot/task-balanced replay, P12식 비대칭 배분. 배분은 validation split에서 결정한다.
3. 정렬·normalization·mask를 적용한 뒤의 uniform replay와 **원래 Memory Anchors**. 이것이 가장 중요한 강한 대조다.
4. 공통 encoder freeze / robot별 adapter 또는 head. Trainable parameter뿐 아니라 전체 보관 모델 크기·routing 비용도 보고한다.
5. 효과 차이를 이용하는 잠정 selector. Estimator가 실제 정의될 때만 구현한다.
6. 전체 과거 데이터를 사용하는 joint training은 비인과적·추가 저장 reference로 분리한다. 실용 replay와 동일 정보 예산이라고 표시하지 않는다.

각 방법은 같은 pretrained checkpoint·new demonstration·총 update 수·old-data exposure·replay 저장 bytes를 기준으로 비교한다. 선택기의 embedding 계산과 추가 forward/denoise 비용도 포함한다. 서로 다른 이미지 크기에서 sample 수만 같게 맞추지 않는다. 시간 예산 비교는 별도로 보고한다.

Primary outcome은 로봇별 old-task success 변화와 new-task success의 동시 비교다. 전체 평균만으로 한 로봇의 실패를 숨기지 않는다. Event/trajectory별 진단 score가 held-out task–robot pair의 retention 하락을 예측하는지도 별도로 본다. Action MSE·VQA·latent distance는 closed-loop 능력 보존의 대체 metric이 아니다.

Task–robot pair, scene, episode 단위 train/validation/test 분할과 학습 순서를 사전에 고정한다. 본 실험 결과에서 실패가 큰 pair만 골라 효과를 보고하지 않는다. 표본 수·seed·noninferiority margin·효과 크기 기준은 competence와 variance를 확보한 뒤 실험 전에 정한다. 지금 임의의 성공률 기준을 확정하지 않는다.

## 6. 채택·축소·기각 조건

- **E1-L1 진행 조건:** 가장 가까운 방법과 다른 예측을 하나 이상 기술하고, 비교 가능한 task–robot pair의 공개 field/interface 경로를 식별한다. 이 단계에서 정책 효과 입증을 요구하지 않는다.
- **진단 연구로 축소:** 효과 공간 분석이 forgetting을 설명하지만 기존 replay보다 개선하지 못할 때, 여러 로봇·task에서 재현되는 현상과 실무적 의사결정 가치가 있을 때만 검토한다.
- **방법 주장 기각:** 정렬된 action + 원래 Memory Anchors, 단순 균형 replay 또는 adapter가 같은/낮은 비용으로 설명한다면 현재 selector 주장을 종료한다.
- **인위적 현상 기각:** 잘못된 단위·normalizer·padding만 고쳤을 때 이득이 사라지거나, 정상적인 공개 recipe에는 그 오류가 없으면 일반 VLA 연구로 확대하지 않는다.
- **비교 불가능:** 공통 task/effect·action semantics 또는 두 로봇의 기본 능력을 확보하지 못하면 native 실험을 시작하지 않는다.
- **신규성 재검토:** cross-embodiment effect 기반 conflict/replay를 이미 다룬 직접 선행을 찾으면 해당 방법 이후의 질문으로 수정하거나 종료한다. 이번 검색에서 못 찾았다는 사실은 부재의 증명이 아니다.

## 7. E1-L1 후속 심사 결과

- [x] P10의 release와 estimator 경계 확인. Diffusion/VLA 설정이 다르며 공식 code는 미공개, flow 세부는 WAITING_SOURCE다.
- [x] P12 v3·P13·P15의 본문·공개 source를 대조하고 mask·normalization·replay step scaling과 미확보 구현 범위를 기록했다.
- [x] P6/P11 action transform과 registry의 RoboMIND/RH20T 자산을 감사했다. 공개 annotation 6,073개와 time/pose API를 확인했으나 matched physical pair는 미확보다. 기존 OXE/Octo/OFT의 존재를 신규 qualification으로 승계하지 않는다.
- [x] 해석적 반례와 데이터/시점/정보 예산 계약 작성. 실제 VLA에서 다른 예측을 보이는 사례는 NOT_MET다.
- [x] [비실험 buildup 판정](../2026-10-22_e1_buildup/README.md): REVISE·진단 HOLD. 현재 새 selector는 채택하지 않는다.

체크는 **심사 작업 완료**이며 미공개 코드 확보·payload 검증·정책 효과 입증이 아니다. 이후 [E1-R1 심사](../2026-10-22_e1_buildup/R1_REVIEW.md)도 완료했으나 gate NOT_MET다. 현재 다음은 [E1-R2 evidence packet](../2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json)이다. 정상 정렬 이후의 효과/잔차 지표가 retention을 설명하는지로 질문을 좁혔으며 top-tier 기여의 근거는 아직 부족하다.
