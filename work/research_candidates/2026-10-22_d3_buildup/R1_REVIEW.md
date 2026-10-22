# D3-R1 — 사건 관측·행동 능력·단순 대안의 공개 근거 심사

- 검토일: 2026-10-22 KST. [L1의 재개 조건](./TASK_POLICY_AUDIT.md#7-연구-가치와-다음-판단)을 추가 공개 자료로 심사했다.
- **공개 근거 심사 DONE / 재개 gate NOT_MET.** Raw 자료의 식별 경로는 진전됐지만, 동일 instance의 사건–관측 대응과 변경 목표 수행 능력은 확보하지 못했다.
- **연구 REVISE / full-task 실험·학습 HOLD_RESEARCH 유지.** 현재 공개 근거만으로 독립적인 VLA/RL 방법에 투자할 가치는 입증되지 않았다. 상태 인식과 실행 능력을 분리하는 진단 질문은 조건부 보존한다.
- 산출물: [source ledger](./r1_sources_2026-10-22.json), [필요 증거 명세](./R1_EVIDENCE_REQUIREMENTS.json), [문서 검증](VALIDATION.md#stage-2). 새 실행 코드나 모델은 만들지 않았다.

## 1. 세 조건의 결과

| R1 조건 | 이번에 새로 확인한 근거 | 판정 |
|---|---|---|
| A. 동일 instance의 Cooked 사건 전후 관측/상태 | 기존 annotation 200개와 같은 stem의 raw HDF5 200개. 기록·재생·영상 변환 source의 연결과 시간 정렬 주의점 | **PARTIAL / 미충족.** 파일 존재는 실제 state label·RGB pair가 아님 |
| B. 언어 LL의 continuation·mitigation 능력 | P2 저자 상세 평가에서 대상·task·평가 코드 공개 범위 확인. 별도 P4 언어 정책의 hotdog 동작 기록 발견 | **NOT_ESTABLISHED.** 어느 것도 같은 hotdog의 조리 후 복귀/열원 차단 성공을 입증하지 않음 |
| C. 단순 재계획과 matched 비교 | 기존 contract에 사건 시간 정렬·관측 누출·기본 능력·목표 변경의 교란을 보완 | **DESIGN_ONLY.** 비교는 정의했지만 runnable qualification이나 결과가 없음 |

`DONE`은 이 검토를 마쳤다는 뜻이다. A–C 통과나 D3 가설 검증을 뜻하지 않는다. 정책 실행은 0회이며 실제 외부 연구자 피드백도 없다.

## 2. 사건–관측 연결: 원자료 위치를 구체화했지만 pair는 미확보

### 2.1 파일 identity의 진전

공식 dataset 안내는 raw HDF5를 OmniGibson replay용 자료로 지정한다. 고정 revision `f9d2901112993d75684223820eec70722806c2c4`의 `task-0045/` metadata를 읽고, L1이 기록한 annotation 200개의 파일 stem과 대조했다. **200/200 일치**, 한쪽에만 있는 stem 0개다. 이는 파일명 대응 검사이며 HDF5 내용과 annotation의 frame 정렬 검증은 아니다. [공식 설명](https://behavior.stanford.edu/challenge/dataset.html), [고정 raw 목록](https://huggingface.co/datasets/behavior-1k/2026-challenge-rawdata/tree/f9d2901112993d75684223820eec70722806c2c4/task-0045).

후속 evidence packet의 **identity 예시**로 정렬상 첫 파일을 지정한다. 정책 성적을 보고 선택하지 않았으며 pilot case로 채택한 것도 아니다.

| 항목 | 확인 상태 |
|---|---|
| Raw path | `task-0045/episode_00450010.hdf5` |
| Annotation path | `annotations/task-0045/episode_00450010.json` |
| Raw remote size | 29,282,328 bytes; payload 미열람 |
| Raw LFS SHA-256 metadata | `f246d992ff9089a917469e4fd0e61786a5b1639598f4685e4ded9d8d25b2f549`; 실제 payload 검증 아님 |
| `task_instance_id`, HDF5 내부 `demo_N`, object binding | **미확인** |
| LeRobot `episode_index`·video offset·frame 대응 | **미확인**; 파일명의 숫자를 episode index로 대체하지 않음 |
| Cooked 전이 frame·실제 RGB cue·feasible continuation | **미확인** |

### 2.2 현재 source가 보여 주는 경로와 한계

분석 commit은 L1과 같은 `7d6718cb8ac5f249bb3c610c23713627d97da1ef`다. 실제 배포 dataset을 이 commit으로 만들었다는 주장은 하지 않는다.

1. **기록:** HDF5 writer는 초기 serialized state, step별 state/size, scene/config/code hash metadata를 기록하는 경로를 갖는다. 따라서 state-grounded pair를 얻을 경로는 있다. 그러나 특정 raw 파일에 어떤 object-state schema가 저장됐는지는 payload를 읽지 않아 모른다. [writer L490](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/envs/hdf5_data_wrapper.py#L490).
2. **내부 episode 선택:** 현재 replay script는 HDF5의 `demo_N` 중 기본으로 마지막 group, 별도 옵션으로 가장 긴 group을 고른다. 같은 파일이라도 group 선택이 다르면 주석/영상과 달라질 수 있다. [selection L165](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/scripts/learning/replay_obs.py#L165).
3. **시간 정렬:** playback은 state 복원 뒤 물리 step과 관측을 수행하고, LeRobot writer는 앞 observation과 다음 step의 action/outcome을 묶는다. 조리 임계값 부근에서는 단순한 `state[i] ↔ RGB[i]` 대응을 가정할 수 없다. 실제 recorded schema·frame convention을 확인해야 한다. 특정 배포 영상에 off-by-one 버그가 있다고 판정한 것은 아니다. [playback L787](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/envs/data_wrapper.py#L787), [conversion L337](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/envs/lerobot_data_wrapper.py#L337).
4. **배포 provenance:** 공개 `meta/info.json`에 `omnigibson_git_hash` key가 없다. `codebase_version=v3.0`은 LeRobot format 값이며 OmniGibson commit이 아니다. 현재 writer에 hash 저장 코드가 있다는 사실로 배포 파일의 provenance를 채우면 안 된다. [배포 metadata](https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/blob/4f50b44796641a4d526a19d9aeadc8aa51e2f2c2/meta/info.json).

**A 판정:** 자료가 없다고 결론내린 것은 아니다. 자료의 위치와 필요한 해석 경로를 확보했다. 이번 비실험 범위에서는 raw state·영상 payload를 열지 않았으므로 사건 정답과 정책이 보는 cue를 연결한 증거는 없다. 일반 시연 영상이나 turn-on 주석을 그 증거로 대체하지 않는다. 관측 가능성을 확인하지 않은 상태에서 VLA가 사건을 놓쳤다고 평가할 수 없다.

## 3. 공개 정책 결과: 성능 수치의 적용 범위를 좁힘

### 3.1 P2 상세 결과는 hotdog continuation 평가가 아니다

L1의 `hanbin5/pi07-ll-b1k-200k` model card를 저자의 [상세 issue #5](https://github.com/inner-king/policy/issues/5)와 대조했다. 다음은 **저자 보고**이며 독립 재현 결과가 아니다.

- 15 validation episode는 `cook_a_frozen_pie`, `cook_broccolini`, `cook_a_brisket`, `thawing_frozen_food`, `freeze_fruit`의 각 3개다. **`cook_hot_dogs`는 이 평가에 없다.** Training task에 포함된 것과 구분한다.
- `turn off 0/3`은 **burner** 대상이다. Microwave turn-off 실패율로 인용하면 안 된다.
- Microwave는 turn-on 3/3, close 3/3, open 0/3으로 보고했다. 이는 해당 시작 상태의 skill 결과이며 조리 후 같은 hotdog를 꺼낼 수 있다는 증거가 아니다. 작은 실패 표본으로 영구적인 불가능을 판정하지도 않는다.
- 263개 구간 중 상태 판정이 제한적으로 가능한 108개만 수치 표에 들어간다. 나머지 145개에는 place-on/in 54개가 포함되며 해당 보고에서 판독이 남아 있다. `43/108`을 전체 조리/복귀 성공률로 쓰지 않는다.
- 저자는 `replay_oracle.py`, `run_replay_oracle.sh`와 해당 평가에 사용한 server version이 `ec298b7…` 공개 branch에 아직 없다고 명시한다. Repository tree에도 그 평가 코드/개별 결과가 확인되지 않는다. **학습·기본 serving source 확인과 skill 평가 구현 재현 가능성은 다르다.**

이 추가 자료는 P2를 ‘불가능한 정책’으로 기각하기 위한 근거가 아니다. D3-E1에 필요한 microwave 열기·해당 hotdog 회수·fridge 복귀·열원 차단 능력을 **현재 수치로 인증할 수 없다는 근거**다.

### 3.2 P4: 별도 π0.5 언어 skill 정책도 post-event witness를 제공하지 못함

추가 후보 `inner-king/policy`, branch `ers345/pi05`를 발견했다. 코드 `56c3ee92042ac08f29adf3a50bf9c970db75f8dc`, 문서 `6a0ec7c744e9a0dc67aad04fe7391269ec62745f`를 구분한다. 서버는 요청의 `prompt`를 `_policy.infer`에 전달한다. 다만 이 연결만으로 동적 지시 version/cancel과 행동 효과를 인정하지 않는다. [server L72](https://github.com/inner-king/policy/blob/56c3ee92042ac08f29adf3a50bf9c970db75f8dc/pi05/src/scripts/serve_policy_b1k.py#L72).

저자의 [issue #11](https://github.com/inner-king/policy/issues/11)은 `hotdog_put_micro`에서 9차 성공·10차 실패를 보고한다. 공개 suite는 `cook_hot_dogs`, instance 86, `cook_hot_dogs_ep9080.npz`, skill 8의 **전자레인지에 넣기**를 지정한다. 이는 조리 전 동작이며, 조리 뒤 꺼내거나 fridge로 돌려놓는 witness가 아니다. 이 instance/episode를 앞 raw 예시 `00450010`과 같은 것으로 합치지 않는다. [suite L118](https://github.com/inner-king/policy/blob/56c3ee92042ac08f29adf3a50bf9c970db75f8dc/pi05/src/scripts/rollout_new12.sh#L118).

평가는 train scene에서 demonstration을 재생해 skill 시작 상태를 만들며 이동 skill은 학습 범위 밖이다. 보고된 성공·실패를 reset부터의 full-task 성능이나 수정 지시에 대한 generalization으로 해석할 수 없다. 공개 문서는 학습 checkpoint를 repo에 넣지 않으며 기존 장비의 Drive 경로를 사용한다고 명시한다. 검토한 공개 source에서 사용할 checkpoint release를 식별하지 못했다. **P4는 discovery/WAITING_SOURCE이며 P2 대체 primary로 승격하지 않는다.** [README](https://github.com/inner-king/policy/blob/6a0ec7c744e9a0dc67aad04fe7391269ec62745f/pi05/README.md#L172).

## 4. 추가 직접 비교: 평가 설계도 신규성으로 과장하지 않음

기존 [closest work](./CLOSEST_WORK.md)의 SwitchVLA·Hi Robot·RePlan-Bot 등 판정을 유지한다. 새로 확인한 두 논문은 2026 arXiv이며 공식 top-tier acceptance는 확인되지 않았다. Peer-reviewed baseline과 구별하고 **이번에는 dossier에만 기록**했다. Registry·읽기 tier는 바꾸지 않았다.

| 논문 / 읽은 version | 확인한 범위 | D3에 주는 의미와 차이 |
|---|---|---|
| [One Word, Different Action: A Real-Robot Benchmark for Language-Conditioned Embodied Reasoning](https://arxiv.org/html/2609.05260v2), v2, 2026-09-13 | 같은 physical anchor·후보 행동에서 의미 보존/변경, atomic/복합 constraint를 대조. v2 §V의 실제 평가 모델은 text LLM 4개 | 지시가 달라지면 행동도 달라져야 한다는 진단 자체는 이미 다룬다. 현재 v2 결과를 RGB 기반 VLA의 연속 행동/비가역 사건 평가로 인용하지 않음. v1의 RGB 언급을 v2 실험으로 섞지 않음 |
| [LIBERO-MAX: Do Robot Policies Adapt When the World Changes?](https://arxiv.org/html/2609.36518v1), v1, 2026-09-29 | 같은 prefix의 Base/Dynamic 비교와 trigger/query coverage. [공개 spec](https://github.com/liberomax/LIBERO-MAX/blob/01625e290b1aa07511bdc820781e635e851353cc/docs/BENCHMARK_SPEC.md#L26)도 두 arm의 instruction·기존 goal 고정을 명시 | Paired event 진단·기본 실패 분리·cadence 통제 자체를 D3 신규성으로 주장할 수 없음. 이 공개 track은 Cooked 기반 목표 가능성 변경을 제공하지 않으므로 D3 event pair를 대신하지 못함 |

LIBERO-MAX의 고정 revision `01625e2…`에서 README/spec와 결과 composition source를 읽었다. 전체 runner·보고 결과를 재현하거나 원자료를 검증한 것은 아니다. One Word v2의 공식 code/data release는 읽은 논문/abstract에서 식별하지 못했다. 제목의 ‘real-robot’을 모든 모델 출력의 closed-loop robot 실행으로 확대하지 않는다.

## 5. 단순 대안 이후에 남아야 할 질문

아래는 **연구자 해석과 미구현 비교 설계**다. 기존 [QUALIFICATION_SPEC](./QUALIFICATION_SPEC.json)의 B0–B4를 대체하지 않고 필요한 통제를 보완한다.

### 5.1 State를 알면 ‘uncook 불가능’ 판정은 간단하다

고정 object ID와 허용 행동에서 `Cooked=true`가 불변이며 새 목표가 그 object의 `Cooked=false`를 요구한다면, predicate contradiction 검사만으로 목표 불가능을 판정할 수 있다. 이 한 bit의 규칙에 RL이나 새 planner가 필요하다는 근거는 없다. 모든 post-event 목표를 거부하는 것은 C3의 feasible 목표까지 거부하므로 별도 false-refusal 오류다.

단순 baseline은 `estimated Cooked ∈ {true, false, unknown}`을 사용한다. `unknown`을 임의로 false/true로 바꾸지 않고, 모든 방법에 똑같이 허용된 inspection 또는 uncertainty report를 선택할 수 있어야 한다. Oracle Cooked는 평가·상한 진단에만 쓰며 일반 baseline에 몰래 주지 않는다. 남는 연구 질문은 **허용된 history/inspection으로 상태를 추정하고 단순 재계획을 수행한 후에도, 충분한 행동 능력을 갖춘 VLA에서 전환 실패가 남는가**다.

### 5.2 비교를 무효화할 교란과 수정

| 교란 | 최소 대조 / 해석 경계 |
|---|---|
| 원래부터 microwave를 못 열거나 hotdog를 못 집음 | 동일한 continuation 시작 상태·checkpoint에서 정답 subtask executor의 능력을 먼저 확인. 미충족이면 switching 효과 추정을 보류 |
| ‘uncooked’라는 단어만 보고 항상 거부 | 같은 goal을 사건 전·후 모두 제시하고, post-event에서도 가능한 goal을 포함. 의미 보존 paraphrase 대조도 사용 |
| 사건 전이면 무조건 복귀 가능하다고 가정 | 잔열과 추출 시간 때문에 아직 uncooked라도 목표를 달성 못 할 수 있음. **pre-event feasible도 witness가 필요** |
| 요청 도착 시간/메타데이터가 Cooked 정답을 누출 | `t_event`·GT predicate를 policy에 전달하지 않음. 사건 전후 offset 분포와 goal 배치를 사전 고정; 특정 단어/시간을 label 대용으로 못 쓰게 대조 |
| 서로 다른 prefix와 pose에서 전/후 성능 차이 | 전/후 비교만으로 비가역성의 인과 효과를 단정하지 않음. 각 고정 사건 상태 안에서 같은 세계·prefix를 공유하는 no-change/semantic-change/meaning-preserving arm 비교가 필요 |
| Queue를 비우거나 새 instruction을 전달한 이득 | 모든 baseline에 같은 version/cancel/ack 규약. 과거 wiring 오류 수정 이득을 새 방법의 효과로 세지 않음 |
| 분석하는 동안 simulator 시간을 멈춤 | 모든 arm에서 같은 sim-time·wall-time 처리. Heating, queued action, inspection 비용과 첫 새 action까지의 지연을 기록 |
| 다른 planner·tool·depth·oracle 상태를 추가 | B2/B3는 동일 RGB/proprio/history·skill executor·행동 집합·예산. 추가 정보 조건은 별도 ablation |

### 5.3 결과를 읽는 규칙

- **새 목표 성공**, **불가능 판정**, **추가 손상/열원 완화**, **feasible goal의 오거부**를 분리한다. 불가능한 원 요구에 대한 안전한 중단을 원 goal 성공으로 바꾸지 않는다.
- Frame·episode를 독립 표본으로 부풀리지 않는다. 같은 instance/object/prefix의 결과는 paired unit이며, unseen instance 평가는 별도 split이 필요하다. Native sample size·threshold는 아직 선정하지 않았다.
- Event에 도달하지 못한 episode와 인프라 오류를 기록한다. 성공한 subset만 골라 headline 성능으로 보고하지 않는다. Qualified subset의 conditional 진단은 분모와 coverage를 함께 제시한다.
- 단순 predicate planner+같은 LL이 설명하면 신규 방법은 종료하고 평가 지식만 남긴다. Cue가 불충분하면 정보 한계로 수정하고, executor가 부족하면 조작 능력 문제로 분리한다. VLA/RL 개선으로 미리 해석하지 않는다.

## 6. Buildup 절차에서 이번에 끝낸 범위

[기존 8단계 가이드](../../../research/IDEA_BUILDUP_GUIDE.md#5-문헌에서-아이디어로-넘어가는-8단계)에 맞춰 2–3단계의 자산/증거를 보완했고, 4–6단계의 대안 설명·직접 충돌·공정 비교/기각 조건을 강화했다. 7단계는 공개 source·기존 보고의 정적 점검만 완료했다. 8단계는 내부 투자 판단까지다. Native 검증과 실제 외부 피드백은 계속 미완료다.

이번 판단을 바꾼 근거는 단순한 GPU 부족이 아니다. **사용 가능한 skill 수치를 목표 task에 적용할 수 없고, 비교의 핵심 사건을 아직 관측과 연결하지 못하며, 일반적인 진단 설계에도 가까운 선행이 있다.** 따라서 문헌이 더 쌓였다는 이유로 GO를 주지 않는다.

## 7. 다음 행동과 재개 조건

**D3-R1 공개 조사 작업은 종료한다.** 현재 확인한 자료를 반복 조회하는 문서 단계나 policy adapter 구현을 다음 자동 TODO로 만들지 않는다. **D3-R2 / WAITING_EVIDENCE**는 [증거 명세](./R1_EVIDENCE_REQUIREMENTS.json)에 맞는 새 packet이 생겼을 때 판정하는 항목이다.

필요한 것은 다음 세 묶음이다.

1. 한 고정 episode/instance/object에 대해 기록 source version·HDF5 group·state/영상 시간 대응·Cooked 전후 GT와 policy-visible cue를 확인한 packet. Raw 파일 존재만으로 충족하지 않는다.
2. 공개 checkpoint의 식별자와 해당 상태에서 필요한 continuation/mitigation을 수행할 능력 근거. 모든 task에서 높은 성공률이나 D3 효과의 사전 입증을 요구하는 것은 아니다. 단 한 번의 실패로 불능 판정을 내리지 않는다.
3. Instruction version/queue·독립 새 goal 평가를 갖춘 matched 비교 자격. 설계 문서와 실제 검증 기록을 분리한다.

새 공개 snapshot·skill 결과가 나오면 비실험 심사가 가능하다. 자료를 직접 추출하거나 competence를 검증하려면 이후 명시된 범위의 **현재 컴퓨터 Docker** 작업과 runtime qualification이 필요하다. 이번에는 수행하지 않았다. GPU 확보만으로 B/C를 충족하지 않으며 D4나 이전 후보로 자동 전환하지 않는다.

**투자 판단:** 독립 VLA+RL 방법 개발은 현재 추천하지 않는다. 비가역 사건의 관측·가능한 대안 목표·기본 실행 능력을 함께 확보할 수 있을 때에 한해 작은 진단 연구로 재개할 가치가 남는다. 이 결론은 연구 가설을 실험적으로 반증한 결과가 아니다.
