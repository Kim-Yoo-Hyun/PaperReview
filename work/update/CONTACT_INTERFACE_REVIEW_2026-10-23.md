# GAP-R2 — 접촉 VLA의 정보·학습·제어 interface 검토

- 검토일: **2026-10-23 KST**. 작업 **DONE**, 연구 판정 **REVISE / 진단 후보 HOLD**.
- 질문의 canonical 위치: [GAP-CONTACT](../../synthesis/03_manipulation_contact.md#gap-contact-2026). [출처·버전·code 감사](../sources/contact_interface_review_2026-10-23.json) · [TODO](../../TODO.md).
- 범위: 직접 비교 8편의 지정 HTML 본문/부록과 RDP의 공식 proceedings를 확인했다. 전체 논문 정독·재현 완료를 의미하지 않는다. 두 GitHub repository와 연결된 dataset metadata를 정적으로 읽었으며 설치·추론·학습·PDF 다운로드는 하지 않았다.

## 1. 앞선 공백 조사는 registry 밖의 논문도 포함했는가?

**포함했다.** 기존 registry 1,037편의 metadata·synthesis·후보 판단을 참조하면서 외부 공식 proceedings/program/publisher와 최신 preprint를 함께 조사했다. 그러나 registry 전체와 2024–2026 모든 top-tier 논문을 정독하거나 전수 조사한 것은 아니다.

| 앞선 작업 | 기록된 조사 단위 | 확인 깊이·registry 연결 |
|---|---|---|
| [GAP-R1](./VLA_GAP_SCOUT_2026-10-23.md) | 논문 46건 + 공개 자원 1건 | registry 연결 13건, 직접 충돌의 지정 본문과 나머지 abstract/index 확인 |
| [GAP-W1](./BROAD_RESEARCH_GAP_SCOUT_2026-10-23.md) | 다분야 논문 40건 | 지정 본문 7건·project 1건·abstract/index 32건; registry 연결 6건 |
| [GAP-V2](./INTEGRATED_GAP_REVIEW_2026-10-23.md) | 통합 비교 논문 30건 | 지정 본문 6건·abstract/index 24건; registry 연결 14건 |

목록 사이에 중복이 있어 합계를 unique 논문 수로 사용하지 않는다. 공식 출처는 CVPR·ICCV·ECCV·NeurIPS·ICLR·ICML·CoRL·RSS·ICRA·IROS·T-RO 등을 포함하지만 journal 범위는 conference보다 좁고 IJRR·Science Robotics를 균등하게 조사하지 않았다. NeurIPS 2026 program abstract와 최종 proceedings도 구분했다. 따라서 broad search를 처음부터 반복하기보다 다음 TODO였던 CONTACT의 직접 충돌과 비교 조건을 심화했다.

## 2. 결론과 연구 가치

**접촉 정보가 언제 필요한지 묻는 문제는 중요하지만, 현재 설명만으로 독립적인 새 VLA 방법을 시작할 근거는 부족하다.** 단순 센서 추가·입력 제거·증류·고주파화·숨은 기계 조건 테스트는 이미 다뤄졌다. 남길 수 있는 후보는 **새 task/기계 조건에서 어떤 개입이 유효할지 미리 예측하는 진단**이다. 그 예측의 신규성도 아직 확정하지 않았다.

| Buildup 검사 | 이번 판정 | 의미 |
|---|---|---|
| 실제 행동상 중요한 문제인가? | 충족 | 접촉 실패·coverage·feedback 통합에 대한 실제 평가 근거가 있음 |
| 기존 대안과 갈리는 예측이 있는가? | 미충족 | 기존 ablation을 넘어선 held-out 예측 규칙·baseline 계약이 없음 |
| 비교할 구체적인 task가 있는가? | 문헌상 후보 있음 | ContactBench doorknob variation. 센서 필요성의 결정적 사례는 아님 |
| 공정한 실행 자산 묶음이 확보됐는가? | 미충족 | task–checkpoint–sensor–controller–clock–evaluator를 연결한 구성이 없음 |
| 효과·runtime·외부 피드백 검증 | 미실행 | 문헌/정적 code 검토로 대신하지 않음 |

**GAP-R2의 비실험 판단은 완료한다.** CONTACT는 새 방법 착수 대신 조건부 진단 질문으로 보존하고, 다음 활성 문헌 작업을 **GAP-W2의 GEOMETRY → DATA-TRANSFER → SYSID**로 넘긴다. 단순히 GPU가 없어 멈춘 상황이 아니다. Hardware와 공개 실행 자산뿐 아니라 기존 설명과 구별되는 예측이 필요하다.

## 3. 학습 supervision·policy 입력·controller를 분리한 비교

아래 내용은 지정 구간에서 확인한 사실이다. 미확인은 부재를 뜻하지 않는다. Force/tactile을 서로 대체 가능한 동일 센서로 취급하지 않는다. 코드가 없는 항목의 policy 설명으로 저수준 controller의 입력까지 추정하지 않았다.

| 논문 / 공식 지위 | 학습·실행 시 contact 정보 | action/controller 경계와 직접 충돌 | 근거 구간 |
|---|---|---|---|
| **ForceVLA**, NeurIPS 2025, pr-0128 | 학습·추론 모두 6D force 사용; VL/proprio와 MoE 결합 | TCP pose·gripper 출력. 공개 구현의 force 경로를 아래에서 확인 | [본문](https://arxiv.org/html/2505.22159v2) §4–5, App. A–D; [공식](https://papers.nips.cc/paper_files/paper/2025/hash/8633b46e12cc5f2ee1f05a6ca2c65b38-Abstract-Conference.html) |
| **ForceVLA2**, CVPR 2026, pr-0691 | RGB·proprio·wrench 및 force/subtask prompt; 진행도 supervision | pose·force·transition 출력과 hybrid control까지 변경. ACP(Adaptive Compliance Policy) baseline과 force-branch ablation이 이미 있음 | [본문](https://arxiv.org/html/2603.15169v1) §3–5, Table 1/3, App. D; [공식](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html) |
| **AT-VLA**, CVPR 2026, pr-0690 | Xense normal/tangential force, 수동 contact label로 gate 학습; 실행 중 tactile | slow VL/fast tactile, 양팔 EE pose 출력. 같은 weight의 tactile 제거 실험도 이미 있음 | [본문](https://arxiv.org/html/2605.07308v1) §3–4, Table 2; [공식](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html) |
| **FD-VLA**, ICRA 2026, pr-0185 | 실제 force로 vision/state-conditioned token을 감독; policy 추론에는 live force 불필요 | SmolVLA action expert. 로봇 전체가 force-free라는 증거는 아님. Generalization은 배경·조명 변화의 정성 검토 | [본문](https://arxiv.org/html/2602.02142v1) §III, IV-A–E; [공식 program ThI2I.154](https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html) |
| **ContactBench 1.0**, 2026 preprint | 6개 실제 task 중 4개만 GelSight Mini; RDP는 marker, FTP-1은 tactile image 사용 | DP/π0.5와 RDP/FTP-1 비교; π0.5·FTP-1은 task별 fine-tuning. Coverage·incidental cue·hidden mechanics를 이미 분석 | [본문](https://arxiv.org/html/2610.24512v1) §III-D–V-D, Table III/IV |
| **ForceDelta-VLA**, 2026 preprint | teacher correction 증류 후에도 최근 wrench history를 실행 중 사용 | force correction과 delay correction을 분리. Zero-force·head·async ablation이 이미 있어 단순 요인 분해 자체가 기여는 아님 | [본문](https://arxiv.org/html/2609.18242v1) §III-D/E, IV-A–D, Table IV |
| **TaF-VLA**, 2026 preprint/status 미확정 | force/pressure로 tactile adapter 사전학습; 실행 중 tactile history 필요 | force-aligned token을 π0.5 action expert에 전달. Vision-only force distillation과 다름 | [본문](https://arxiv.org/html/2601.20321v2) §III–V, VII, App. A |
| **Visuotactile estimation/control**, CoRL 2024, PMLR 출판 2025 | privileged simulation trajectory로 estimator 학습; 실행 시 object pose·proprio·F/T history | Bayesian recurrent estimator와 uncertainty-aware RL; VLA가 아닌 선행 대안. KUKA iiwa에서 EE velocity를 joint command로 변환 | [본문](https://arxiv.org/html/2412.13157v1) §3–7; [공식](https://proceedings.mlr.press/v270/ferrandis25a.html) |

RDP 자체도 [RSS 2025 공식 논문](https://www.roboticsproceedings.org/rss21/p052.html), registry pr-0751이다. 이번에는 공식 abstract/status만 추가 확인했으며 ContactBench가 보고한 RDP 결과를 RDP 원논문의 재현으로 표시하지 않는다. 위 preprint 3편은 신규성 충돌용이며 top-tier 채택 논문 수에 포함하지 않는다.

## 4. 공정 비교를 가르는 평가 조건

| 논문 | embodiment·task·trial | 시간/coverage/초기화에서 확인한 경계 |
|---|---|---|
| ForceVLA | Flexiv Rizon, 5 tasks, 244 demonstrations. Pump/plug/USB 20 trials, wiping 10, peeling 15 | RGB 30fps를 policy/controller Hz로 해석하지 않음. Peeling은 반복 stroke를 포함해 task별 분모가 다름 |
| ForceVLA2 | Flexiv Rizon 4s, 5 tasks, 1,000 demonstrations, 20 trials/task | force sampling 300Hz ≠ policy rate. Table 3에서 force branch 이득이 모든 task에 양수는 아님 |
| AT-VLA | Genie1, contact 4 + noncontact 2 tasks, 30–50 demonstrations/task, 15 trials | 일부 비교 baseline은 접촉 subtask만 학습하고 미리 grasp한 상태로 시작. 전체 trajectory 방법과 성공률을 단순 등치 불가. 40ms forward와 slow:fast 1:3도 system Hz와 구분 |
| FD-VLA | UR5e, 3 tasks, 50 demonstrations/task, 30 trials/task | 저수준 controller의 force 접근·실제 command Hz는 이번 근거에서 고정하지 못함 |
| ContactBench | UR5e, 6 tasks, Table III/IV 각 방법·task/조건 30 trials | 36개 reference task 전부에서 정책 평가한 것이 아님. FinRay를 쓴 2 tasks는 tactile 비교 없음 |
| ForceDelta-VLA | Franka 5 + XSquare 양팔 4 tasks; 200 demonstrations/task, 기본 20 trials, 지연/새 물체 10 | RGB/state 30Hz, wrench/command 100Hz. 2.43ms forward를 전체 control rate로 바꾸지 않음. Peak force/time은 성공 trial에 한정돼 실패를 포함한 위험 비교와 다름 |
| TaF-VLA | FR3 teleoperation/data collection, 15 trials/model/task | §V-A는 8 tasks, Table I는 7 rows. 분모 불일치 미해소. Adapter 수집 30Hz ≠ robot command rate; 사전학습 frame과 policy episode 구분 |
| 2024 visuotactile | planar pushing, simulation 15Hz; hardware 기본 20 trials, 5초/full occlusion 각 10 | 고정 object/pusher 형상, AprilTag pose+occlusion 설정. 일반 RGB VLA나 여러 task의 contact utility로 일반화하지 않음 |

**연구자 판단:** 논문 사이의 평균 성공률 차이는 센서의 인과 효과가 아니다. Backbone·pretraining·action space·controller·시작 상태·실패 집계가 함께 다르다. ForceVLA2의 ACP 비교가 있다는 사실과, 우리 질문에 필요한 동일 policy/controller factorial 비교가 확보됐다는 주장은 별개다.

## 5. 공개 code/data의 실제 상태

모두 2026-10-23의 정적 확인이다. GitHub/Hugging Face API와 작은 text/JSON 파일만 읽었다. Dataset payload·checkpoint를 받거나 외부 코드를 실행하지 않았다.

| 자산 | 확인 결과 | 남은 한계 |
|---|---|---|
| [ForceVLA repository](https://github.com/ft-robotic/ForceVLA/tree/79de88fdd0651d957a2b5212cae8995159c5ad65) | commit `79de88fd…`, source·training config 존재. [입력/출력 변환](https://github.com/ft-robotic/ForceVLA/blob/79de88fdd0651d957a2b5212cae8995159c5ad65/src/openpi/policies/forcevla_policy.py)과 [model](https://github.com/ft-robotic/ForceVLA/blob/79de88fdd0651d957a2b5212cae8995159c5ad65/src/openpi/models/pi0_force.py) 확인 | `sample_actions` L309의 `prefix_out_fix`와 달리 L336–338은 `prefix_out is None` 확인 직후 그 값을 concatenate에 넣는다. **정적 불일치이며 실행 실패를 측정한 결과는 아니다.** 사용 전 수정/qualification 필요 |
| [ForceVLA dataset](https://huggingface.co/datasets/qiaojunyu/ForceVLA-real-data/tree/6070cbef017e95d695fc804e6fb28cc8baabb1cd) | ungated file index 존재. Plug subset `meta/info.json`: state 13D(포함 force), action 7D, fps 30, 51 episodes; train-only split 명시 | model의 `state[:7]` / force `state[7:13]`와 연결. 단순 state-only baseline에도 force가 남을 수 있음. 14D 예제 주석은 이 metadata와 다름. Hidden-mechanics test split·controller·checkpoint 묶음은 미확보 |
| [TaF-VLA repository](https://github.com/mrHuangyz/TaF-VLA/tree/49b2388ab0ba85054211e28500af5aff4879c415) | commit `49b2388a…`, 51 files, samples·videos·data visualization script. README가 full tactile dataset 링크 제공 | 검사한 tree에 policy training/inference 구현은 확인되지 않음. Repository 존재만으로 전체 재현 가능 판정 불가 |
| [TaF dataset](https://huggingface.co/datasets/jiamig/taf-dataset/tree/239c8ee8156bf11eb6d6c11c004f9a8721528d9d) | ungated file index 7,289 entries 확인 | Tactile-force 사전학습 데이터 공개와 10k manipulation episodes·policy checkpoint 전체 공개는 별개 |
| [ForceVLA2 project](https://sites.google.com/view/force-vla2/home) / [ContactBench project](https://jingyi-xiang.github.io/contactbench/) | 전자는 code/dataset coming soon이며 code link가 GitHub homepage; 후자는 code/assets/simulation coming soon | 실제 task implementation·checkpoint release를 확인하지 못함. 논문상의 open-source 표현으로 대체 불가 |
| AT-VLA / FD-VLA / ForceDelta | AT-VLA project 접근은 Google login으로 제한. 나머지는 exact-title/project 탐색에서 해당 공식 구현을 식별하지 못함 | **공개 없음**으로 단정하지 않음. 현재 검토에 사용할 pinned implementation은 미확보 |

## 6. Task 하나를 골라도 곧바로 센서 필요성을 증명할 수는 없다

문헌상 가장 구체적인 후보는 **ContactBench의 doorknob unlocking threshold 변화**다. 기본 회전량 60°에서 시각적으로 구분되지 않는 72°/80° 조건으로 바꾸며, 모든 방법의 기본 task 능력이 높은 상태에서 평가한다. RDP와 FTP-1은 같은 tactile 추가라는 표현으로도 다른 적응 행동을 보인다. 이 현상은 이미 [§V-D, Table IV/Fig. 11](https://arxiv.org/html/2610.24512v1)에 보고돼 새 발견으로 주장하지 않는다.

**아래는 연구자 해석이며 논문의 실험 결과가 아니다.** 숨은 threshold가 다르다는 사실만으로 서로 다른 행동이 *반드시* 필요하지는 않다. 모두 충분히 크게 돌리는 보수적 정책이 공통으로 성공할 수 있다면, 센서는 필수가 아니라 시간/힘 비용을 줄이는 수단일 수 있다. 현재 확인한 근거는 그러한 공통 정책의 허용 여부·최악 비용을 배제하지 않는다. RGB/proprio의 충분한 history에서 unlock을 감지할 가능성도 먼저 비교해야 한다.

따라서 재개에는 다음 계약이 필요하다.

1. **주장 범위:** 같은 task·controller에서 contact feedback의 추가 가치인지, 센서와 controller를 함께 바꾸는 전체 시스템 이득인지 고정한다. 전자는 live input·distilled input·history-only·controller-only를 같은 action interface에서 비교한다.
2. **결정이 달라야 하는 이유:** 공통 보수적 행동과 단순 history/proprio feedback을 강한 baseline으로 둔다. 모든 조건에 통하는 안전한 행동이 충분하면 필요성 주장을 기각하고 비용 절감 질문으로 축소한다. 허용 힘·overshoot·termination 비용은 측정 근거 없이 만들어 넣지 않는다.
3. **다른 예측:** 초기 일부 조건에서 정한 진단이 미관측 mechanics/task에서 어떤 개입이 유리한지 예측해야 한다. 기존 observability/uncertainty 지표·contact coverage·고전 feedback만으로 같은 선택을 하면 새 진단 방법을 채택하지 않는다. 아직 지표나 수치 threshold를 freeze한 것은 아니다.
4. **공정 비교:** 학습량·force supervision 접근·초기화·센서 위치/동기화·action/command rate를 고정하거나 명시적 요인으로 바꾼다. Oracle mechanics는 분석용으로만 사용한다. Failure를 포함한 성공률·힘 위반·완료/중단 시간·추가 센싱 비용을 기록한다. 성공 trial만의 평균도 보조 지표로 분리한다.
5. **실행 자산:** 실제 task/variation, sensor calibration/log, base-competent checkpoint, normalizer, controller·clock, evaluator를 revision에 연결한다. 현재 이 묶음은 **없다**. 새 runtime 실험은 구축 후 로컬 Docker에서만 수행한다.

## 7. 완료 범위와 인계

GAP-R2는 처음 요구한 입력·supervision·controller·coverage·rate·task·trial·release 비교와 후보 판정을 완료했다. 문헌상 사례는 확보했지만 **새 기여와 실행 준비는 확보하지 못했다**. 센서 통합을 포기한다는 결론도, 분야 전체에 공백이 없다는 결론도 아니다.

새 근거 없이 CONTACT의 같은 공개 페이지를 반복 확인하거나 큰 학습을 시작하지 않는다. [GAP-W2](../../TODO.md)의 GEOMETRY부터 직접 선행 3–5편을 대조하며, VLA의 navigation 판단과 실제 충돌 위험으로 연결되는지 검토한다. 기존 C1–C6·D1–D3·E1/E2 판정은 유지한다. Manifest/tier/사용자 reading status는 변경하지 않는다.

검증: tier generator compile·재생성, source ledger의 건수/ID/reference 검사, repository audit, `git diff --check` 통과. 전체 1,037편·5,185개 표준 노트·322개 활성 reading row 유지, audit 오류·경고 0. Manifest·tier·active/history reading CSV의 SHA256은 작업 전과 같다. 기존 미커밋 변경을 보존했다.
