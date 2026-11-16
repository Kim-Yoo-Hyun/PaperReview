# GAP-H1 — 협업에서 사람의 도움이 늦거나 틀릴 때도 질문이 이득인가?

- 검토일: 2026-10-23 KST. 문헌·공개 source 정적 검토; 정책 실행·사람 대상 실험 없음.
- 작업 판정: **GAP-H1 DONE**. 연구 판정: **일반 ask/act/intervene 방법 NO-GO / 좁힌 진단 REVISE·HOLD**.
- Canonical 질문: [GAP-HRI](../../synthesis/01_planning_control.md#gap-hri-2026). [출처·revision·확인 구간](../sources/hri_help_reliability_review_2026-10-23.json).
- 기존 D3의 instruction switch, E2의 feedback timing, C4/C6의 평가 후보를 재개하지 않는다. 사용자 reading status와 registry tier도 바꾸지 않는다.

## 1. 결과

**질문·실행·행동 개입을 선택하거나, 사람의 오류와 질문 비용을 고려하는 것만으로는 새 주제가 되기 어렵다.** RCIP·UPS는 uncertainty에 따른 도움 요청을, Ask-to-Clarify는 dialogue와 실제 manipulation을 연결한다. 최신 실패 진단 연구는 틀리거나 무정보인 응답과 비용에 따른 act/ask/sense 비교까지 수행한다. [RCIP §III–IV](https://arxiv.org/html/2403.15959v2), [UPS §IV-C](https://arxiv.org/html/2602.22474v2), [Ask-to-Clarify §III-C](https://arxiv.org/html/2509.15061v3), [When Should a Failing Robot Ask? §III-C·IV-C](https://arxiv.org/html/2609.21942v1).

남길 질문은 **질문 종류·상대가 볼 수 있는 정보·현재 작업 조건에 따라 응답의 정확도와 지연이 함께 달라질 때, 독립 calibration에서 정한 도움 요청 규칙이 실제 VLA의 작업 손실을 줄이는가**다. 평균적인 “사람 정답률”과 질문 횟수만으로 충분한지 먼저 검사한다. 이는 아직 신규성이 입증된 방법이 아니라 **조건부 진단 가설**이다. 단순 expected-cost rule, 파트너별 calibration, 재관측/안전한 대기가 설명하면 복잡한 router를 만들 이유가 없다.

현재 이 주제를 우선 구현할 근거는 부족하다. 중요성은 있지만, 질문–응답–실제 실행 결과가 연결된 자료와 상대 모델을 검증할 근거가 없다. GPU가 생기면 계산 경로를 검증할 수 있으나 인간의 부담·신뢰 또는 자연스러운 응답 오류를 자동으로 검증할 수는 없다.

## 2. 문헌 집합·버전·확인 깊이

14편을 비교했다. 2024–2026 공식 proceedings/program 근거 8편(BMVC 발표 예정 1편 포함), preprint/working paper 5편, 2023 foundation 1편이다. 지정 본문/부록을 읽은 직접 비교는 7편이고, 나머지는 abstract·공식 metadata 수준이다. 검색은 targeted review이며 모든 venue·모든 관련 문헌의 전수 검토가 아니다. Registry의 PARTNR(pr-0082)·KnowNo(pr-0706)를 외부 선행과 연결했다.

| ID | 논문·status | 확인 범위 | 역할·경계 |
|---|---|---|---|
| H01 | [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://proceedings.mlr.press/v229/ren23a.html), CoRL 2023 | 공식 abstract | KnowNo foundation; registry pr-0706 |
| H02 | [Risk-Calibrated Human-Robot Interaction via Set-Valued Intent Prediction](https://www.roboticsproceedings.org/rss20/p027.html), RSS 2024 | [arXiv v2 §III-B·C, IV-A·D·E, VI](https://arxiv.org/html/2403.15959v2); source/config | RCIP: sequence-level risk와 help 비용. 본문 버전과 최종 proceedings 전체 동일성은 미감사 |
| H03 | [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html), ICLR 2025 | [arXiv v1 §4.3, App A.12–13](https://arxiv.org/html/2411.00081v1); 공식 source/docs | 실제 참가자가 simulator agent를 조종한 평가와 robot hardware 평가 구별 |
| H04 | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://roboticsproceedings.org/rss22/p142.html), RSS 2026 | [arXiv v2 §III–VI, App A-A](https://arxiv.org/html/2602.22474v2); source/docs | UPS: ambiguity와 sampled-action incapability 분리. 실제 base policy는 diffusion policy |
| H05 | [LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](https://proceedings.mlr.press/v306/zhou26i.html), ICML 2026 | [arXiv v1 §3–4·6, Table 1](https://arxiv.org/html/2606.28182v1); source/docs | PARTNR-Dialog의 Talk·행동 규칙과 협업 평가. 인간 도움 품질 보장으로 확대하지 않음 |
| H06 | [CoRI: Communication of Robot Intent for Physical Human-Robot Interaction](https://proceedings.mlr.press/v305/wang25e.html), CoRL 2025 | 공식 abstract | Motion 기반 설명과 사람의 communication clarity 평가; 질문 gating의 증거와 분리 |
| H07 | [Towards Uncertainty Unification: A Case Study for Preference Learning](https://www.roboticsproceedings.org/rss21/p091.html), RSS 2025 | 공식 abstract | Human/robot uncertainty와 user-specific calibration은 기존 방법군 |
| H08 | [Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue](https://arxiv.org/html/2509.15061v3), 2025 preprint / v3 2026 | §III-B·C, IV-A·C | 질문 중 motor loop 중단, refined instruction 확인 후 실행. Formal acceptance·공식 공개 code는 이번 검색에서 미확인 |
| H09 | [PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration](https://arxiv.org/html/2605.24350v1), 2026 preprint | §3.3·4·5 | Cross-day partner/scene 변화·ask utility. Profile-conditioned simulated human 평가 |
| H10 | [When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](https://arxiv.org/html/2609.21942v1), 2026 preprint | §III-C·IV-C·V·VII | Noisy scripted answerer·cost sweep·진단 정확도. 질문 문구가 응답 분포에 영향을 주지 않는 설정 |
| H11 | [Ask When It Pays: Cost-Aware Open-Ended Interaction for Instance Goal Navigation](https://arxiv.org/abs/2606.03175), 2026 preprint | abstract·[저자 project](https://billzhao1030.github.io/IVLN/) | 질문 유형별 비용·navigation uncertainty. 공개 code/data는 project에서 준비 중 표시 |
| H12 | [Benchmarking Interaction, Beyond Policy: a Reproducible Benchmark for Collaborative Instance Object Navigation](https://arxiv.org/abs/2604.00265), BMVC 2026 공식 program 등재 | abstract·[공식 program #641](https://bmvc2026.bmva.org/programme/tuesday/) | QAsk-Nav: 질문과 navigation을 분리 평가. 11월 예정 tentative program이며 발표 완료·최종 proceedings 공개로 쓰지 않음 |
| H13 | [Learning to Defer in Congested Systems: The AI-Human Interplay](https://arxiv.org/abs/2402.12237), 2024 working paper / v4 2025 | 최신 abstract·[저자 status](https://mitmgmtfaculty.mit.edu/tlykouris/research/) | 요청량이 응답 지연을 만드는 queueing 계보. Operations Research 게재로 확인되지 않았으며 구제목은 Content Moderation |
| H14 | [Collaborative Instance Object Navigation: Leveraging Uncertainty-Awareness to Minimize Human-Agent Dialogues](https://openaccess.thecvf.com/content/ICCV2025/html/Taioli_Collaborative_Instance_Object_Navigation_Leveraging_Uncertainty-Awareness_to_Minimize_Human-Agent_Dialogues_ICCV_2025_paper.html), ICCV 2025 | 공식 abstract | AIUTA/CoIN: ask·continue·stop과 human/simulated-user 평가. 본문 전체·code는 이번 심화 범위 밖 |

Survey·검색 index·자동 리뷰는 발견에만 사용했다. 위 method 판단은 저자 본문/공식 source에 근거한다. QAsk-Nav와 L2D의 버전/status를 재확인했으며 검색 결과의 과거 제목·저자 발표를 journal 게재로 옮기지 않았다. 신규 registry admission은 별도 수행하지 않았다.

## 3. 가장 가까운 선행이 실제로 가정한 것

| 선행 | 직접 확인한 경계 | 연구 판단에 주는 의미 |
|---|---|---|
| RCIP | §IV-E는 도움을 요청하면 suboptimal action이 발생하지 않는다고 가정한다. §VI는 low-level controller 실행 보장과 verbalizable finite intent의 한계를 밝힌다. 같은 action으로 이어지는 여러 intent는 합칠 수 있다. | Ambiguity 자체보다 행동을 바꾸는 불확실성을 봐야 한다. Perfect help 가정 밖으로 확장할 수 있지만, noisy help의 최초 제안이 되지는 않음 |
| UPS | §V의 모든 base policy는 image-conditioned diffusion policy다. App A-A는 같은 분포의 calibration/test sequence, §VI는 faithful imagination/narration을 전제한다. Residual 학습 뒤 verifier를 다시 calibrate한다. | “저자가 policy 변화 뒤 보정을 안 했다”는 gap은 틀리다. 예측 집합 coverage를 임의의 잘못된 답변·새 파트너 아래의 성공 보장으로 확대하지 않음 |
| PARTNR | §4.3/App A.13에 실제 129명 참가자 평가가 있다. App A.13.2는 재시도 중 성공 또는 최고 completion 시도를 선택하는 집계 절차를 명시한다. | 전부 LLM partner 실험이라고 쓰면 안 됨. Simulator 안의 인간 협업이며, 새로운 도움 정책 평가에서는 첫 시도/재시도·사람/작업 분모를 따로 고정해야 함 |
| LLawCo | §4.1은 message event·§4.2는 simulation steps/Talk 등을 평가한다. Table 1에서 8B LLawCo success 0.57, 비통신 ReAct 0.62다. | Communicative baselines에 대한 개선과 모든 baseline 우위를 구별. 설명·질문이 많거나 법칙을 썼다는 이유로 인간 부담 감소를 추정하지 않음 |
| Ask-to-Clarify | §III-C는 질문 중 motor loop를 멈추고 refined instruction의 실행 가능성을 확인한다. §IV-C의 latency는 모델 generation 시간이다. | 실제 motor interface와 학습된 dialogue 능력이 있음. Human response delay와 모델 추론 latency를 같은 실험으로 취급하지 않음 |
| PACT | §4–5는 partner/scene 변화와 history 효과를 다루되 simulated-human protocol·균일 질문 비용을 사용한다. | Partner adaptation·질문 횟수 효율 자체는 직접 충돌. 실제 사람의 오류·피로·부담 평가를 한 것으로 확대하지 않음 |
| Failing Robot Ask | §IV-C의 답변은 correct/uninformative/wrong을 episode seed로 뽑는 scripted stand-in이다. §VII는 질문 문구 독립성과 scripted simulation 범위를 명시한다. | “답이 틀릴 수 있음을 고려” 또는 “cost에 따라 질문”은 이미 비교됨. Natural response 이해와 실제 repair 성공은 별도 검증 |

위 표는 문헌의 실험 범위이며 우리의 재현 결과가 아니다. 또한 **‘이 논문이 다루지 않음’은 ‘아무도 다루지 않음’이 아니다.** Interactive POMDP·selective prediction·learning-to-defer·dialogue grounding 계보까지 차별화해야 새 방법을 채택할 수 있다.

## 4. 공개 구현에서 확인한 실행 경계

4개 repository의 고정 revision에서 21개 source/config/doc 파일을 확인했다. 실행·import·설치를 하지 않았으며 관련 구간과 hash만 ledger에 남겼다.

| Repository revision | 정적 확인 | 이번에 확보하지 못한 것 |
|---|---|---|
| [RCIP `ba90ccb`](https://github.com/irom-princeton/risk_calibrated_interactive_planning/tree/ba90ccbb333b0a80bc40ea8d2f72c5a1a9b5c812) | Risk utility·calibration config가 있지만 `scripts/calibrate_vlm.py`는 0 byte다. VLM config는 별도 로컬 dataset 경로를 요구한다. | 이 script를 실행해 sorting calibration을 바로 재현할 수 있다고 판정하지 않음. 다른 경로까지 구현이 없다는 주장도 하지 않음 |
| [UPS `f7bad4d`](https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering/tree/f7bad4d7cd6d5e4350751a958ba9bb146a99ecec) | README는 NutAssembly용 release와 calibration/run scripts를 안내하나 해당 scripts는 고정 root tree에 없다. 앞선 submodule 이동 명령이 있어 실제 의도한 경로는 추가 확인이 필요하며 submodule 내부는 미검토다. Narrator source는 Gemini 외부 API를 호출한다. | 저자 pipeline의 전체 실행 경로와 현재 **로컬 Docker-only** 조건에서의 충실 실행 가능성은 미검증. 로컬 VLM 대체는 별도 baseline 변경이며 충실 재현으로 표시할 수 없음 |
| [PARTNR `ddfff19`](https://github.com/facebookresearch/partnr-planner/tree/ddfff19f4b6c098a31edea4d19e7b75db72433c2) | Agent→Tool→Skill 경로와 HITL analysis의 episode/user/attempt metric 명세를 확인했다. `agent.py:200–201`의 dry-run은 motor 실행 없이 success 응답을 만들 수 있다. | Dataset payload·원시 모든 시도·실행 설정은 미확인. Dry-run tool response는 native 성공이 아님 |
| [LLawCo `0f08a41`](https://github.com/merlresearch/llawco/tree/0f08a418295840829b9e5aa012ab562912298363) | Talk는 speech event를 반환하고 planner는 action history를 prompt에 넣는다. 지정 decentralized runner는 planner를 차례로 호출하며 시간을 합산한다. README의 pretrained bundle 링크는 비어 있다. | Tool의 delivered 응답은 상대의 수신·이해·실행 완료 증거가 아님. End-to-end event/물리 시간·checkpoint·모든 실행 config는 미검증 |

Server/병렬 실행 설명과 한 runner의 호출 순서는 공존할 수 있다. 위 source 관찰로 논문 전체가 동기식이거나 latency를 무시한다고 단정하지 않는다. Cloud model 호출·remote GPU 실험으로 제한을 우회하지 않았으며, HF weights/data·simulation assets도 받지 않았다.

## 5. 남길 수 있는 질문과 주장–증거 연결

**잠정 RQ:** 같은 VLA·task·사람에게 보이는 정보를 고정했을 때, 도움의 평균 정답률을 쓰는 규칙과 질문 유형/상대 관측/응답 시간을 조건으로 쓰는 규칙은 언제 다른 행동을 선택하며, 그 차이가 실제 작업 손실을 줄이는가?

다음은 연구자 가설이지 확인된 현상이 아니다. 지연 때문에 state가 달라진 효과만 남으면 기존 feedback/staleness 문제로 귀속한다. 질문이 불확실성을 줄여도 base policy가 실행하지 못하면 도움 선택의 효과로 세지 않는다.

| 잠정 주장 | 필요한 증거 | 경쟁 설명·강한 대안 | 기각 기준 |
|---|---|---|---|
| 평균 helper reliability만으로 충분하지 않은 조건이 있다 | Question/context별 응답·개입 시점·정답/무정보/오답과 독립 native outcome | Known-reliability expected-cost rule, 간단한 조건부 calibration, robot 자체 오류 보정 | 단순 조건별 threshold가 전부 설명하면 새 learned method 중단 |
| 질문 선택이 답의 품질을 바꾼다 | 같은 상태에서 질문 문구/대상 정보만 바꾼 matched 비교 또는 적절한 무작위 배정 | 더 많은 task 정보·긴 답변·고성능 helper를 제공한 효과 | 정보량/시간을 맞추면 차이가 없어지거나 자연스러운 답변에서 효과가 없으면 주장 축소 |
| 응답 후 실행 결과까지 봐야 help의 가치를 알 수 있다 | 정확한 해석, actionable instruction, native skill 성공을 분리한 평가 | UPS식 incapability 처리, 재관측, 공통 보수적 행동, no-help/stop | Policy competence나 단순 retry/hold가 설명하면 별도 HRI contribution으로 채택하지 않음 |

선행이 다룬 조건을 함께 보아야 한다. UUPL의 user calibration, PACT의 partner/history, QAsk-Nav의 질문/행동 분리, L2D의 endogenous delay를 제외한 채 빈칸을 만들지 않는다. 특히 L2D의 abstract는 응답 지연이 요청량에 좌우되는 경우를 이미 모델링하지만, VLA contact나 불완전한 human repair의 해법이라고도 주장하지 않는다.

## 6. 최소 비교 계약 초안과 중단 순서

1. **비교 단위:** 같은 reset/task에서 하나의 help decision. Instruction ambiguity, robot 실행 능력, 사람의 정보/능력, channel delay를 별도 축으로 둔다. Calibration·train·test는 episode와 partner/task 단위로 분리한다.
2. **정책 입력:** 당시 observation/history, instruction, 지금까지 도착한 메시지, 측정된 경과 시간, calibration에서 얻은 통계만 허용한다. Hidden cause·미래 reply·정답 helper label은 평가 전용이다.
3. **Action set:** 바로 수행, 명확화 질문, 현재 상태 재관측, 안전한 대기/중단, action intervention 요청. 각 대안은 실제 skill/interface가 있을 때만 포함하며 “help”라는 하나의 추상 oracle로 합치지 않는다.
4. **비용과 metric:** Native task success·잘못된 실행/복구 비용, 질문 수, 응답/대기 시간, 실제 teleoperation 시간, 사람의 모니터링 시간, computation을 따로 보고한다. UPS의 normalized intervention steps나 LLawCo의 Talk 횟수를 그대로 human seconds/workload로 바꾸지 않는다.
5. **강한 baseline:** Never/always ask, best fixed choice, calibrated expected-cost threshold, partner별 단순 calibration, RCIP/UPS식 gating, 주기적 확인/재관측, 공통 보수적 행동. 정보·모델·데이터·total time 예산을 동일하게 맞춘다.
6. **원인 분리:** Scripted 응답 실험은 label correctness·response delay를 독립 조작하는 진단에만 사용한다. 이후 question-conditioned response, participant holdout에서 검증해야 인간 관련 결론을 낼 수 있다. 평균 ask rate가 줄었다는 이유로 부담 감소를 선언하지 않는다.
7. **Selection bias:** 요청한 경우에만 답을 기록하면 never-ask 영역의 helper accuracy를 추정할 수 없다. Matched 질문 수집·적절한 무작위 배정·propensity 기록 중 식별 가능한 경로를 먼저 고정한다. Replay된 한 질문의 답으로 다른 질문의 효과를 추정하지 않는다.
8. **순차 gate:** Base skill 성공·답변 해석·safe wait/stop 가능성 → 질문/응답/행동 시간 연결 → 단순 대안의 잔여 오차 → 새로운 partner/task 조건 예측 순으로 검사한다. 첫 실패에서 복잡한 학습을 멈춘다.

위는 구현 전 계약 초안이다. 특정 VLA checkpoint·환경/asset revision·normalizer·controller·seed/split·효과 크기·trial 수·cost weight가 정해지지 않았으므로 실행 manifest가 아니다. 사람 대상 평가를 한 것처럼 쓰지 않으며, 향후 실제 실험은 사용자 선택 컴퓨터의 로컬 Docker에서만 진행한다.

## 7. Buildup 단계별 완료 범위·가치 판단

| 단계 | 결과 |
|---|---|
| 0 공백 탐색 | Registry+2024–2026 외부+KnowNo 계보 14편, 공식 status/버전 대조 |
| 1 행동 가치 | 답에 따라 질문·대기·재관측·실행 중 무엇을 택할지가 달라져야 함 |
| 2 문헌 집합 | 지정 본문 7편, abstract/metadata 7편. 완전한 체계적 review 아님 |
| 3 가정·interface | Perfect/noisy help, simulated/real human, DP/VLA, question/native outcome, simulator/wall time을 분리 |
| 4 질문 구체화 | 단순 도움 선택에서 question/partner 조건부 reliability의 실제 행동 가치로 축소 |
| 5 직접 충돌 | 일반 cost/noise/partner adaptation/질문–행동 분리 주장은 독립 신규 주제로 채택하지 않음 |
| 6 주장–증거 | 경쟁 설명·동일 예산 baseline·기각 규칙·비교 계약 초안 작성 |
| 7 저비용 확인 | 공개 interface 정적 확인까지만 완료. Native packet·정책 실행·인간 반응 실험 없음 |
| 8 외부 비판·결정 | 내부 판단은 REVISE/HOLD. 실제 외부 연구자 피드백은 미수행 |

**연구 가치:** 불완전한 도움 아래의 행동 선택은 중요한 문제다. 그러나 지금의 넓은 주장은 선행과 겹치고, 남은 질문도 classical value-of-information·POMDP·learning-to-defer로 설명될 수 있다. 현재는 우선 구현 후보로 올리지 않는다. 새로운 실제 사례, 동일 정보/시간의 강한 대조, 단순 대안 이후 남는 전이 가능한 예측이 생길 때 재검토한다.

**GPU 확보 시 가능한 일:** 공개 source를 보완한 뒤 local Docker에서 한 환경의 base skill/질문 interface·native outcome 연결을 검증하는 pilot. GPU만으로 해결되지 않는 것은 natural helper response 자료, participant 수준 평가, 공정한 실제 비용 측정이다. 구현 누락을 메우는 작업 자체도 연구 기여가 아니다.

다음 비실험 TODO는 [GAP-CAUSAL](../../synthesis/02_rl_il_offline.md#gap-causal-2026)의 **GAP-CF1**이다. 시연자만 본 정보와 action coverage 부족을 구별하고, 추가 로그 cue/작은 개입이 policy 선택을 바꿀 조건을 직접 문헌과 대조한다. 초기 RL 전이·C2의 재개나 새 simulator 실행은 포함하지 않는다.

## 8. 유지보수 검증

- 작업 전 audit: 오류·경고 0, 1,037편·322개 활성 tracker·47개 history·5,185개 노트.
- 작업 후 compile·tier generator·repository audit·diff 검사 통과, 오류·경고 0. 1,037편·활성 tracker 322행·history 47행·표준 노트 5,185개를 유지했다. Markdown 5,335개·링크 10,146개를 검사했다.
- Manifest·registry meta·tier·active/history reading CSV 5개의 SHA256은 작업 전과 같다. 기존 변경 354개 중 수동 문서 7개를 의도적으로 갱신했고 나머지 347개는 hash가 동일하다. 신규 report·ledger를 추가했다.
- 대조용 source/config/doc 21개 hash를 검증한 뒤 이번 작업의 임시 디렉토리와 pointer를 삭제했다. 고정 revision·확인 위치·hash·검증 결과는 source ledger에 보존했다.
- 이번 범위는 수동 synthesis·report·ledger·guide·navigation·TODO다. Registry admission·읽기 승격·실험·설치·PDF/model/data 다운로드·Git 게시를 수행하지 않았다.
