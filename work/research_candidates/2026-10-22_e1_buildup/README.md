# E1 buildup — 행동 효과의 차이는 VLA의 망각을 설명하는가?

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- 심사일: 2026-10-22 KST. 사용자 요청: E1 buildup 진행, VLA 중심·RL 선택 사항.
- 판정: **REVISE / 진단 연구 조건부 HOLD. 현재 형태의 새 replay 방법은 채택하지 않는다.**
- 완료: 기존 [8단계 guide](../../../research/IDEA_BUILDUP_GUIDE.md)의 1–6 문헌·설계 심사, 7의 해석적·정적 검사, 8의 내부 반박과 판단. **Native 정책 검증과 실제 외부 피드백은 미완료**다.
- 근거: [직접 선행](./CLOSEST_WORK.md), [공개 구현·데이터 감사](./SOURCE_ASSET_AUDIT.md), [해석적 반례·비교 계약](./CLAIM_CONTRACT.md), [재개 명세](./EVIDENCE_REQUIREMENTS.json), [source ledger](./sources_2026-10-22.json), [유지보수 검증](./VALIDATION.md).
- 최초 [E1 card](../2026-10-22_vla_rescout/E1_QUESTION.md)는 탐색 이력이다. 현재 판정은 이 문서와 [TODO](../../../TODO.md)가 우선한다.

**후속 E1-R1 완료:** [재개 심사](./R1_REVIEW.md)에서 RH20T cfg3/5 공통 task ID 59개와 구체적 view key, X-VLA-Pt의 Franka/UR pose-native interface를 확보했다. 정상 pose 잔차 이후의 추가 효과 정보와 일관된 native 비교 경로는 미확보여서 **gate NOT_MET·REVISE·진단 HOLD**다. 다음은 [R1 이후 명세](./R1_EVIDENCE_REQUIREMENTS.json)의 **E1-R2 / WAITING_EVIDENCE**다. 아래 1차 심사의 관측·판정은 이력이며 최신 재개 항목은 이 후속 문서를 따른다.

## 이번에 달라진 판단

원래 질문은 새 로봇을 학습할 때 **명령 표현의 차이와 실제 행동 충돌을 구분해 과거 경험을 더 잘 선택할 수 있는가**였다. 중요한 문제지만, 물리적 행동 정렬과 기존 conflict replay를 결합하는 것만으로는 차별성이 부족하다. 현재 새 방법 구현에 투자할 근거는 확보하지 못했다.

이번에 남긴 질문은 더 좁다. **정상적인 action 정렬·normalization·mask 이후에도, 행동 잔차/효과 차이가 새 로봇 학습에 따른 기존 로봇의 능력 저하를 예측하는가? 그 예측은 가상 업데이트의 손실 증가보다 유용하거나 저렴한가?** 효과 공간이 항상 더 좋다는 전제를 버린다. 이 질문의 답이 replay 선택과 shared/분리 모델 선택을 실제로 바꿀 때 연구 가치가 생긴다.

핵심 근거는 세 가지다.

1. **직접 선행의 범위가 넓다.** Memory Anchors는 단순 로봇 간 raw-action 비교가 아니며, MIR/GSS 비교도 이미 수행했다. SPACE와 HiMoE는 각각 물리 action interface와 이질성 분리를 다룬다. [선행 비교](./CLOSEST_WORK.md).
2. **제안의 논리적 연결이 자동으로 성립하지 않는다.** 선형 효과 변환의 거리는 가중 행동 잔차와 같고, 동일한 잔차도 parameter update에 따라 old loss를 늘리거나 줄일 수 있다. 또한 기록된 다음 상태는 실행하지 않은 예측 행동의 결과가 아니다. 이는 연구자 도출이며 VLA 효과의 실험적 반증은 아니다. [도출 A–C](./CLAIM_CONTRACT.md).
3. **비교 자료는 일부만 적합하다.** RoboMIND 공개 annotation 6,073개에서 두 로봇의 유사 task 경로는 찾았지만, 정상 EE pose·동기화·동일 goal·controller command가 묶인 qualified pair는 확보하지 못했다. RH20T는 시간·pose interface가 더 명시적이지만 task×robot coverage와 arm command 의미는 추가 근거가 필요하다. [자산 감사](./SOURCE_ASSET_AUDIT.md).

## 1. 해결되면 달라질 일

로봇 A에서 작업하는 공유 VLA에 B의 demonstration을 추가할 때, 새 능력과 A의 능력을 함께 유지하면서 과거 데이터 재처리·보관·학습 비용을 제한한다. 관심 결과는 로봇별 closed-loop 성공과 비용이다. Replay score 자체를 높이는 것이 목표가 아니다.

Continual VLA의 중요성은 충분하지만, 잘 설정한 단순 replay가 강하다는 반대 근거도 있다. 따라서 “망각이 크다”를 모든 pretrained VLA에 일반화하지 않는다. [ICML 2026 공식 논문](https://proceedings.mlr.press/v306/liu26bu.html).

## 2. 필요한 문헌 역할

[비교표](./CLOSEST_WORK.md)에 foundation/MIR, 직접 방법/Memory Anchors, 강한 단순 대안/continual VLA·Never v3, 물리 정렬/SPACE·LAP·Rethink, 구조 대안/HiMoE·CLARE, dataset/RoboMIND·RH20T를 배치했다. 이전 2024–2026 탐색의 [P1–P16](../2026-10-22_vla_rescout/LITERATURE.md)을 이어받되, 핵심 retrieval 메커니즘은 NeurIPS 2019까지 추적했다. 이번 dossier 추가를 registry 등록으로 표시하지 않는다.

## 3. 가정·interface·증거 대조

처음에는 단일 팔·parallel gripper의 공통 manipulation task만 고려한다. 서로 다른 robot의 command 차원, 카메라, scene, task를 동시에 바꾼 결과로 embodiment 원인을 단정하지 않는다. 각 로봇의 native output이 유효하고 기본 능력이 있는 모델이어야 한다. 다른 DoF의 명령을 정의할 수 없는 checkpoint는 conflict score를 계산하기 전에 탈락시킨다.

Pose, command, achieved displacement, contact/object outcome을 구분한다. Action 정렬 recipe가 존재한다는 사실은 동역학적 효과의 동일성이나 continual competence를 보증하지 않는다. 공개 코드의 실제 mask·normalizer·replay step 경로와 데이터의 시간·pose 경계는 [감사](./SOURCE_ASSET_AUDIT.md)에 기록했다.

## 4. 가설과 경쟁 설명

- **H1, 조건부 통계 가설:** 정렬 후의 효과 차이가 held-out task–robot pair의 retention 하락에 추가 예측력을 제공한다.
- **H2, 별도 개입 가설:** H1의 신호로 replay를 바꾸면 동일 자원에서 old retention이 개선되고 new competence가 유지된다.
- **H0:** 올바른 정렬·균형 replay·모델 분리로 충분하거나, 효과 차이는 controller/domain shift만 설명한다.
- **H3:** 망각은 optimizer·parameter sharing·gradient interference가 주로 결정하며 효과 score에는 추가 가치가 없다.

H1이 실패하면 H2 구현으로 넘어가지 않는다. H1이 성립해도 H2가 참이라는 뜻은 아니다. 단순 좌표 변환 사례만 확인되면 구현 품질 문제로 분류한다.

## 5. 직접 충돌과 신규성 경계

새로움으로 주장하지 않을 것은 물리 action 통일, conflict replay, MIR 적용, mask/normalizer 수정, adapter 분리다. 직접 선행의 flow estimator 세부와 공개 release 경계도 남아 있어 동일 구현이라고 주장할 수 없다. [직접 비교와 미확인 범위](./CLOSEST_WORK.md).

잠정적인 기여 문장은 **“실제로 가능한 다중 로봇 조건에서 어떤 conflict 지표가 retention을 설명하며, 어떤 정보·비용 조건에서 그 설명이 깨지는지 규명한다”**다. 현재는 독창적 현상과 일반성을 입증하지 못한 질문이다. 문헌에서 정확히 같은 제목을 찾지 못했다는 사실은 신규성 근거가 아니다.

## 6. 주장–증거와 공정 비교

[계약](./CLAIM_CONTRACT.md)에 표현-only 대조, 실제 robot 대조, task-conflict 대조, residual/효과/MIR 진단 비교와 uniform·balanced·AnchorER·adapter 대안을 정의했다. 총 update, new/old exposure, 저장 payload와 archive 접근, 선택 비용을 따로 통제한다. 원 논문의 과거 전체 데이터 접근과 엄격한 resident buffer 설정을 섞지 않는다.

실행 model/commit/checkpoint·두 episode payload·split·seed·표본 수·margin은 미확보다. [명세](./EVIDENCE_REQUIREMENTS.json)는 `executable=false`이며 만들어지지 않은 실행 artifact를 완료로 표시하지 않는다.

## 7. 가장 약한 연결의 저비용 검사

**완료:** affine metric 동치, 잔차로 망각 방향을 식별하지 못하는 반례, counterfactual effect의 정보 부족, 공개 replay 비용·mask 경로, annotation/schema 감사.

**결과:** 표현 차이만으로 새 selector를 정당화하는 논리는 불충분하다. 공개 task 후보는 discovery 수준이며 실제 두 로봇의 matched 물리 packet과 native competence가 없다. 전체 연구를 GPU 문제 하나로 보류한 것이 아니다.

**미실행:** FK 재계산, 데이터 배열·영상 검증, policy inference/update/rollout, 성능 측정. Host·Docker 어디에서도 이번 정책 실험은 하지 않았다.

## 8. 내부 반박·가치 판단·다음 행동

| 반박 | 이번 답 | 남은 조건 |
|---|---|---|
| 좌표/단위를 맞추면 끝나는가? | 선형 경우는 가중 잔차로 환원된다 | 정상 recipe에서도 예측이 갈리는 자연스러운 사례 |
| MIR를 쓰면 되는가? | 직접 대안이며 AnchorER도 이미 비교했다 | 같은 정보·비용에서 추가 설명력 또는 절감 |
| 실제 다른 로봇의 같은 task인가? | 유사 instruction 경로만 확인 | goal/scene·EE·시간·controller를 함께 검증 |
| 효과 모델이 oracle 정보를 더 쓰는가? | 현재 counterfactual mapper 미확보 | 추론 가능한 forward map과 오차/비용 검증 |
| 좋은 결과가 나와도 연구 가치가 작은가? | 한 pair의 전처리 수정만으로는 작다 | 여러 held-out pair에서 일관된 현상·의사결정 가치 |

**본격 방법 연구로의 발전 가치는 아직 부족하다.** 제한된 진단 연구로 검토할 가치는 남지만, 현재 근거로 top-tier 기여를 기대한다고 평가하지 않는다. E1-L1/비실험 buildup과 후속 R1 심사는 DONE이며 R1 gate는 NOT_MET다. 다음 **E1-R2는 WAITING_EVIDENCE**, native E1-E1은 HOLD_RESEARCH다. 재개에 필요한 것은 [후속 packet](./R1_EVIDENCE_REQUIREMENTS.json)이며, 실험 전에 효과를 이미 증명하라는 조건은 아니다.

실제 외부 비판은 E1-F1 미착수다. 위 표는 내부 검토이며 전문가 피드백이 아니다. 외부 연락·E2 전환·기존 C/D 후보 재개는 수행하지 않았다. 같은 문서 재조회나 GPU 확보만으로 연구 gate를 통과시키지 않는다.
