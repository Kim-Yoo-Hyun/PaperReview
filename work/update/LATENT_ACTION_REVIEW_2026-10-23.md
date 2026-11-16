# GAP-L2 — VLA latent action의 supervision·decoder·전이 조건 검토

- 검토일: 2026-10-23 KST
- 작업: [TODO GAP-L2](../../TODO.md)의 비실험 문헌·공개 interface 대조
- Canonical 질문: [GAP-LATENT](../../synthesis/04_vla_generalist.md#gap-latent-2026)
- 근거: [버전·확인 구간·code/HF revision ledger](../sources/latent_action_review_2026-10-23.json)

## 1. 판정

**GAP-L2 문헌 검토는 완료했다. 일반적인 latent-action supervision·decoder·proxy 비교는 독립 신규 주제로 채택하지 않는다. 물리 조건에 따른 supervision 배분 질문은 REVISE / 진단 후보 HOLD로 남긴다.** GPU만 확보하면 바로 시작할 단계는 아니다. 현재 부족한 것은 선행과 갈리는 예측 및 그 예측을 시험할 구체적인 물리 조건·데이터 구성이다.

| 처음 생각할 수 있는 주장 | 이번 확인으로 바뀐 판단 |
|---|---|
| 소량의 행동 라벨을 latent 사전학습에도 쓰면 유리하다 | LAOM이 동일 라벨 재사용을 이미 비교. 일반 주장 **NO-GO** |
| Action similarity로 로봇 간 latent를 정렬한다 | VILA의 view alignment에 이어 2026-09 직접 선행이 cross-embodiment와 label/decoder budget을 비교. 일반 방법 **NO-GO** |
| Probe가 좋아도 실제 정책이 실패할 수 있다 | What Matters의 proxy 순위 분석과 새 로봇의 decoder/replay/closed-loop 분리 실험이 존재. 현상 재보고만으로 **NO-GO** |
| 관측 가능한 물리 변화의 종류에 따라 라벨을 representation과 decoder 중 어디에 쓰는 것이 유리한지 예측한다 | 이번 확인 범위에서 동일한 통제 비교는 특정하지 못함. **새로움이 입증된 것은 아니며 HOLD** |

여기서 NO-GO는 해당 넓은 문장을 새 기여로 쓰지 않는다는 뜻이다. 영상 기반 행동 학습 분야 전체를 닫는 판정이 아니다. 기존 C/D/E 후보도 재개하지 않는다.

## 2. 범위와 근거의 깊이

지정 4편 **LAOM·VILA·ViPRA·What Matters**와 직접 선행 **VLM Task-Centric·Action-Similarity Transfer**의 필요한 본문/부록 구간을 대조했다. Registry의 **LAPA `pr-0938`·UniVLA `pr-0882`**는 공식 abstract·identity로 연결했다. 총 8편 중 지정 구간을 읽은 6편과 abstract 기반 배경 2편을 구분하며 전체 정독으로 세지 않는다. 이전 GAP-V2와 중복되는 논문 수를 누적 신규 발견 수로 합산하지 않는다.

LAOM은 ICML 2025, VILA는 CVPR 2026, ViPRA는 ICLR 2026 공식 기록을 확인했다. 나머지 직접 선행 3편은 확인 범위에서 preprint다. 세부 방법은 명시한 arXiv 버전을 기준으로 읽었으며 camera-ready와의 완전한 일치를 주장하지 않는다. 특히 **VILA arXiv v1과 CVF supplement는 동일하지 않다**. CVF 공식 검색 결과에는 π₀.₅·SmolVLA baseline 설정이 추가로 보인다. CVF 본문·supplement 직접 열기는 403이어서 이 추가 부분은 검색 색인 확인에 그쳤다. 따라서 “VILA 최종판에는 VLA 비교가 없다”는 결론을 내리지 않는다. [CVF 공식 기록](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Learning_to_Act_Robustly_with_View-Invariant_Latent_Actions_CVPR_2026_paper.html), [공식 supplement](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Jeong_Learning_to_Act_CVPR_2026_supplemental.pdf)

공개 GitHub 4개 revision, 관련 source/config/doc 16개 파일의 지정 구간, HF 4개 repository의 파일 목록·revision을 확인했다. 원격 source text는 정적으로 읽었고 코드·모델을 실행하지 않았다. PDF local cache, dataset/checkpoint payload, dependency 설치, 학습·rollout·Git 게시를 수행하지 않았다. 공식 등록은 하지 않아 registry와 사용자 읽기 상태도 유지한다.

## 3. 직접 비교

| 논문·확인 구간 | Supervision과 실제 제어 경로 | 평가가 답하는 범위와 비교 시 주의점 |
|---|---|---|
| [LAOM v5](https://arxiv.org/html/2502.00379v5), §3–5·7, App. D–F; [ICML](https://proceedings.mlr.press/v267/nikulin25a.html) | 영상 LAM → 관측에서 latent를 예측하는 BC → action decoder. 보조 action loss와 최종 decoder에 **같은 라벨 subset** 사용 | DCS distractor 제어 및 leave-one-embodiment-out 예비 실험. Target labels가 decoder/보조 supervision에 들어가므로 완전한 zero-shot robot transfer가 아님. 큰 latent의 probe 개선도 downstream 이득과 분리 |
| [VILA v1](https://arxiv.org/html/2601.02994v1), §3·4.1–4.3·5.2·6, App. A.3/A.5 | GT action sequence로 view 간 weighted contrastive/structure alignment. 현재 영상에서 latent를 예측하는 encoder가 downstream diffusion policy를 조건화 | Camera holdout 및 Stack Three→Coffee adaptation. 새 task 적응은 target demonstration으로 encoder와 policy를 함께 조정. Camera 변화의 결과를 동일 task의 friction/controller 변화 결과로 확장하지 않음 |
| [ViPRA v2](https://arxiv.org/html/2511.07732v2), §4–5.2, App. C/D; [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/707e34efcabd2b9375f7a64019600aa8-Abstract-Conference.html) | 행동 라벨 없는 video/latent pretraining 후 실제 action label로 FM adaptation. App. D는 **backbone도 업데이트**하며 history·language·noisy action을 사용 | SIMPLER·LIBERO Long·실제 manipulation. 초기 video prior, history, head, 학습량이 함께 다른 결과를 representation 단독 효과로 보지 않음. ‘고정 latent와 작은 decoder만 학습’이라는 축약은 부정확 |
| [What Matters v1](https://arxiv.org/html/2608.19613v1), §III-B·IV-C·V-A/D–H·VI | DAP/LAP와 physical labels까지 mid-training에 쓰는 JAP 계열을 분리. Backbone tuning, head 교체, normalization을 직접 비교 | Proxy는 coarse screening에 유용하지만 최적 모델 순위를 보장하지 않음. LIBERO-Plus는 주로 **RobotInit**; 그 영상은 Stage I/II corpus에 포함. Stage III 이후 zero-shot을 전 단계 미노출로 해석하지 않음 |
| [VLM Task-Centric v1](https://arxiv.org/html/2601.22714v1), §2–4·7 | Prompt-conditioned pretrained VLM feature를 FDM target으로 사용. LAM 단계의 실제 action label 없이 distractor를 억제하되 최종 adaptation에는 labels 사용 | MetaWorld MT10. UniVLA 등의 **LAM 구성 재구현** 비교이며 공개 VLA 전체 시스템 비교가 아님. LAOM 제목을 보편적 label-필수 정리로 읽을 수 없음 |
| [Action-Similarity Transfer v1](https://arxiv.org/html/2609.19846v1), §III–VI 및 unseen-embodiment/hyperparameter 부록 | 같은 labels의 regression 대 similarity supervision, EE/joint 좌표, decoder 데이터량, π₀/작은 DiT 비교 | 두 학습 로봇의 task swap과 완전히 새 UR5를 구분. Decoder fit·기록 latent replay가 가능해도 frozen policy의 closed-loop 성공은 0/300. 저자도 visual conditioning만을 원인으로 확정하지 않음 |

두 registry 기반은 “영상으로부터 행동 표현을 학습해 VLA에 전달”하는 동기가 이미 연구 흐름이라는 근거다. [LAPA 공식 abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html), [UniVLA 공식 abstract](https://www.roboticsproceedings.org/rss21/p014.html). 이번에 두 논문의 모든 실험 조건을 다시 읽은 것은 아니다.

## 4. 결과를 바꾸는 세 가지 구분

### 라벨 예산: unique labels와 사용 횟수

라벨 비용의 기본 단위는 `dataset / source episode / timestep range / action convention`의 **합집합**이다. 같은 labels를 두 단계에서 재사용했다고 annotation 비용을 두 배로 세지 않는다. 반대로 보조 loss의 labels만 줄이고 decoder가 전체 labels를 쓰면 전체 pipeline의 label 절감은 아니다. Action-Similarity Transfer §V-B는 이 차이를 직접 비교한다. [해당 본문](https://arxiv.org/html/2609.19846v1#S5.SS2)

추가로 사전학습·model selection용 probe가 읽은 labels, source/target robot의 labels, NVS/flow/VLM prior와 해당 연산 비용을 따로 기록해야 한다. 이미 action이 기록된 robot demonstration에서 labels를 가리는 실험과 action이 애초에 없는 human video에 새 annotations를 만드는 비용은 다르다.

### Decoder: oracle latent, 예측 latent, 실제 실행

학습용 `z_teacher = IDM(o_t, o_{t+h})`는 미래 영상을 보지만 배포용 `z_policy = π(o_≤t, instruction)`는 보지 않는다. 따라서 teacher latent의 action probe, predicted latent의 command error, 실제 closed-loop success를 별도로 기록한다. 이 구분 자체는 위 선행에 이미 있다. 새 기여는 어떤 조건에서 어느 구간이 병목이 되는지를 **평가 전에 예측**해야 한다.

또한 논문마다 latent를 반드시 거치는 병목인지, backbone 학습 target인지, downstream policy의 conditioning feature인지 다르다. What Matters의 DAP/LAP/JAP 구분을 따르고, ViPRA FM을 LAOM과 같은 고정 `z → a` decoder 실험으로 취급하지 않는다. [What Matters §IV-C](https://arxiv.org/html/2608.19613v1#S4.SS3), [ViPRA §4.3·App. D](https://arxiv.org/html/2511.07732v2#S4.SS3)

### Split: 무엇이 어느 단계에서 새로운가

`camera / scene / object / task / robot / dynamics / controller`별로 영상 노출, labels 노출, normalization 통계, model-selection 사용 여부를 나눈다. LIBERO-Plus의 위 설정은 정당한 Stage-III generalization 질문이지만 전체 pipeline의 미노출 dynamics 시험은 아니다. 또한 What Matters의 실제 로봇 결과는 같은 200 demonstrations에서 여러 checkpoint의 학습 진행을 비교한다. 이를 적은 demonstrations로 같은 성능에 도달했다는 곡선으로 바꾸면 안 된다. [저자 project의 evaluation protocol·training curves](https://carldegio.github.io/latent_action.github.io/)

## 5. 공개 구현과 자원 경계

아래는 특정 revision의 **정적 확인**이다. 패키지 설치·checkpoint load·native runtime의 성공을 의미하지 않는다. 파일별 hash와 확인 위치는 ledger에 있다.

| 저장소 | 확인된 연결 | 실행 구성에서 더 필요한 것 |
|---|---|---|
| [LAOM `e133195`](https://github.com/dunnolab/laom/tree/e13319533e7b3d5fd974a8a46f4c4892547f30ec) | `Config.__post_init__`가 pretraining/decoder의 labeled path를 묶는다. Decoder는 frozen actor의 예측 latent로 학습. `ActionDecoder.forward(obs_emb, latent_act)`의 **obs_emb는 실제로 사용하지 않음** | Native benchmark는 DCS. Labels sampler는 `original_traj_idx`를 보존하지만 잘라낸 `start_idx`를 저장하지 않아 짧은 clip의 원본 range는 별도 기록 필요. 제공 예제 path를 실험 split으로 재사용하지 않음 |
| [VILA `5f34a3b`](https://github.com/joon-stack/vila-code/tree/5f34a3b5cf4d70b585282c66df1bd88fa72e98b3) | `labeled_loss_coef=0`이어도 GT action sequence가 contrastive/Gram loss를 만든다. `LAOMEncoder`는 현재 영상→예측 latent; finetune config는 freeze=false | 공개 data는 Lift. HF에 Lift/SO101 weights가 보이지만 encoder loader가 요구하는 인접 `config.yaml`은 해당 HF 목록에 없음. 실제 학습 config와 weight 대응 확인 필요; 저장소 preset으로 임의 대체하지 않음 |
| [ViPRA `216c5da`](https://github.com/sroutray/vipra/tree/216c5da91a929ece664a888121e45f6c216a14bb) | 공개 기본 continuous sampler는 image/text에서 FM action을 생성하며 latent-action token을 먼저 생성하지 않는다. 미래 state를 생성하는 별도 함수와 기본 호출을 구분 | Pretrained 7B·tokenizer·VQGAN 파일 목록 확인. LIBERO script는 14-step/7D chunk·별도 normalized JSONL/자산 경로를 요구. 논문 및 project의 action rate와 closed-loop 재계획률을 혼용하지 않음 |
| [What Matters / LAM `03dd812`](https://github.com/XizoB/LAM/tree/03dd8120854110f0cf4fc6eb441a6ad963cb97a6) | Stage 1/2와 Stage 3 loader 분리. LAP head가 latent statistics로 복원 후 MLP decoding. Reference는 latent 64, LIBERO action 7D×8이며 논문 추천 설정과 구분 | HF에는 Stage 1/2 자산군 확인; Stage 3 weight는 확인되지 않음. Latent stats·robot action stats·time sampling을 분리하고 checkpoint와 맞춰야 함. README의 portable path는 재현성 검증이 아님 |

LAOM의 이름에 `obs_emb`가 있다는 것과 실제 입력 효과는 다르다. VILA의 변수명 `unlabeled`·`debug_action_sequences`도 supervision 부재의 증거가 아니다. 이름·설정 값 하나 대신 **loss 또는 action까지의 실제 계산 경로**를 확인해야 한다.

전체 사전학습을 반복하는 계획은 만들지 않았다. ViPRA App. C의 대규모 GPU 사전학습과 LAM의 다단계 학습을 고려하면, 후속 연구가 성립할 때도 공개 checkpoint를 먼저 활용할 수 있는지 확인하는 편이 합리적이다. 이번 HF 조사는 목록 확인이며 payload의 호환성·학습 이력은 미검증이다. 최신 Action-Similarity 연구의 실행 repository는 본문·정확한 제목 검색에서 특정하지 못했으며 **미공개라고 단정하지 않는다**.

## 6. 남길 수 있는 질문과 반증 계약 초안

**연구자 가설:** 동일 robot·task·시점에서 관측 가능한 물리 응답이 바뀔 때, 영상 표현에 필요한 제어 정보가 남아 있는 변화와 표현 자체가 그 정보를 버리는 변화를 구별할 수 있다면, 같은 target labels를 decoder에만 재사용할지 representation까지 조정할지 결정하는 데 도움이 될 수 있다.

단순히 friction을 새 benchmark 축으로 넣는 것만으로는 약하다. 평가 전에 두 설명이 다른 예측을 내고, 더 싼 보정·동일 정보의 baseline보다 적은 적응 비용을 요구해야 한다. 현재는 이 조건을 만족하는 실제 사례가 없어 HOLD다.

| 계약 항목 | 구체화할 내용 |
|---|---|
| 첫 범위 | 한 embodiment·하나의 action convention·고정 camera에서 하나의 물리 축만 개입. Camera-only 변화는 대조군. Controller gain 단위 보정과 contact physics를 처음부터 섞지 않음 |
| 관측 가능성 | 공통 observation/history/proprio에 두 물리 조건을 구분할 단서가 있는지 명시. Hidden simulator parameter를 제안 정책에만 주지 않음. 불가능한 RGB-only 문제를 만든 뒤 supervision 실패로 주장하지 않음 |
| 비교 A/B | A: frozen representation + target decoder. B: 같은 target label IDs로 representation 보조 supervision + decoder. Backbone·head·latent width·video pool·target adaptation data를 맞춤. B의 추가 계산도 비용에 포함 |
| 강한 대안 | 같은 labels의 direct BC/action head, supervised IDM relabeling, matched pretrained visual encoder, 단순 action normalization/controller 보정, 공통 history/proprio conditioning. Action-similarity와 regression은 이미 있는 baseline으로 사용 |
| 공정 예산 | `unique label union`, 유효 transition 수·trajectory 수, 총 GPU 시간과 target environment interaction을 별도 축으로 보고. 동일 총 compute 비교와 동일 update 수 비교를 구분; 추가 사전학습 이득을 무료로 계산하지 않음 |
| 사전 예측 | Mapping 보정만 필요한 경우 A와 단순 baseline이 충분해야 한다. 제어 단서의 표현 손실이 문제라면 B의 이득이 teacher probe 개선에 그치지 않고 predicted command와 held-out success까지 이어져야 한다. 어느 경우인지 판단하는 규칙은 test dynamics를 보기 전에 고정 |
| Holdout/metric | Train/calibration/test를 episode·scene·물리 조건 단위로 분리. Source 성능 보존, target success, failure type, 적응 label·compute 비용을 함께 보고. 같은 rollout의 프레임을 독립 trial로 세지 않음 |
| 기각 | 단순 normalizer/controller/history로 차이가 해소됨; head 용량·추가 compute로 설명됨; oracle teacher에서만 이득; prior study의 일반 decoder bottleneck을 반복함; 사후적으로만 실패를 설명함. 이 경우 독립 신규 방법 중단 |

“관측은 같지만 효과가 다르다”만 남으면 [E1의 정상 정렬 이후 effect 정보 요건](../research_candidates/2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json)과 합쳐 판단한다. D1의 state input, E2의 chunk timing, SYSID의 history 보정 문제로 바뀌는 경우도 기존 후보의 gate를 우회하지 않는다.

이 초안은 executable manifest나 실행 승인이 아니다. 최소한 task/physics intervention·실제 policy input·정규화·데이터 분할·checkpoint 연결이 구체화되면 작은 Docker pilot으로 참/거짓을 시험할 수 있다. **실험 전에 효과 입증을 요구하는 것은 아니다.** 문헌만으로 성공 가능성을 확정하지 않는다.

## 7. Buildup 절차의 완료 경계

[기존 buildup guide](../../research/IDEA_BUILDUP_GUIDE.md)의 순서에 맞춘 진행 상태다. 단계 0–3의 공백·필요성·문헌 집합·interface 비교를 수행했고, 단계 4–6의 좁힌 질문·직접 선행 대조·주장–증거 계약을 초안으로 작성했다. 단계 7은 공개 source의 정적 검사까지 완료했으며 정책 효과 pilot은 미실행이다. 단계 8의 자체 채택 심사는 REVISE / HOLD이고 **외부 연구자 피드백은 받지 않았다**. 문서 작성 완료를 모든 buildup gate 통과로 표시하지 않는다.

## 8. 다음 행동과 검증

- **GAP-L2 DONE:** 비교·기각 기준·공개 interface 경계 기록 완료. Latent 진단 후보의 상태는 HOLD이며 가설 성숙도는 `CURATION-HYPOTHESIS`다.
- **다음 READY 작업은 META-W1:** 이미 확인된 Splat-Nav의 T-RO publication / IROS presentation metadata를 같은 identity 안에서 정합한다.
- Latent 후속은 위 관측 가능한 물리 사례와 선행과 갈리는 예측을 확보할 때 재개한다. 반복 검색이나 checkpoint 존재 확인만으로 자동 재개하지 않는다. 새 method family를 택하면 이번 조사에서 발견된 LAOF·WALA·LAFP 등 인접 선행도 본문으로 추가 대조해야 한다; 이들은 이번 핵심 6편 정독 범위에 포함하지 않았다.
- 유지보수 검증 결과는 작업 종료 시 아래에 기록한다.

### 유지보수 검증

`python3 -m py_compile work/scripts/build_reading_tiers.py`, `python3 work/scripts/build_reading_tiers.py`, `python3 work/scripts/audit_repository.py`, `git diff --check`를 통과했다. 전체 audit의 오류·경고는 0이다.

- Registry 1,037편, CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242, active tracker 322 / history 47, 표준 notes 5,185개를 유지했다.
- Manifest·tier·active/history tracker 4개 파일의 SHA256이 시작 시점과 일치한다. Ledger의 title/arXiv identity·registry match, code 16개 파일 hash와 4개 revision, HF 4개 목록의 수를 확인했다.
- 관련 문서의 로컬 링크 404개가 유효하다. 전체 audit는 Markdown 5,330개·링크 9,828개를 검사했다.
- 시작 시 dirty 163개 중 관련 문서 8개를 갱신했고 나머지 155개는 SHA256으로 보존을 확인했다. 새 파일은 이 report와 source ledger 2개다. 기존 PDF note 수정은 보존했다.
