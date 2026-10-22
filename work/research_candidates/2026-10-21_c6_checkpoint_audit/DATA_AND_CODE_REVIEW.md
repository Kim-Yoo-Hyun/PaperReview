# C6 공개 code·data 심사

- 2026-10-21 KST. [검사 전 gate](./DATA_GATE.md)를 따라 수행했다.
- 외부 원본과 source는 Docker 내부에서만 읽었다. Host에는 provenance/구조 요약을 남겼다.
- Source 정적 검사, 데이터 구조 검사, native policy 실행을 구분한다. 마지막 항목은 수행하지 않았다.

## Repository 감사

전체 git tree와 선택한 text source를 읽었다. Full tree가 있다고 모든 file의 의미나 data payload를 확인한 것은 아니다. Commit·file별 hash는 [CODE_SOURCES.json](./CODE_SOURCES.json), [ARTIFACT_AUDIT.json](./ARTIFACT_AUDIT.json)에 있다.

| Repository | 고정 commit 앞 12자 / 확인 범위 | 결론과 한계 |
|---|---|---|
| [google-deepmind/active_ops](https://github.com/google-deepmind/active_ops) | `5c7b24515ada`, 9 files | 실제 selector, policy kernel, notebook가 있다. `bandit.py:74–77`은 준비된 return에서 sample한다. README의 공개 예제는 cartpole 76 policies이며 VLA가 아니다. Pickle 3개의 파일 목록/크기만 확인, payload 미검사 |
| [AbrarAnwar/seq-eval](https://github.com/AbrarAnwar/seq-eval) | GitHub web와 API 모두 404 | 공식 paper가 제시한 주소를 재검사했지만 source/data를 얻지 못했다. 삭제·비공개·미공개 중 원인을 단정하지 않는다 |
| [AgibotTech/aloe](https://github.com/AgibotTech/aloe) | `aafb7e81cf34`, README·index | Project webpage다. 학습 구현이나 RL checkpoint ledger 공개를 이 주소에서 확인하지 못했다 |
| [dworldeval/dworldeval.github.io](https://github.com/dworldeval/dworldeval.github.io) | `7dee38b65d96`, README·index | Project website와 미디어가 중심이다. Video 편집용 Python file 존재를 evaluator 학습 코드로 간주하지 않는다 |
| [showlab/World-VLA-Loop](https://github.com/showlab/World-VLA-Loop) | `1d1738260bd7`, README | 저자가 source code 준비 중으로 표기한다. 미디어 파일명은 완전한 RL run/checkpoint/outcome 기록이 아니다 |
| [haowwang/offline_policy_eval_manipulation](https://github.com/haowwang/offline_policy_eval_manipulation) | `45bbad6756ae`, 4 files | 실제 value 학습 code와 processed dataset 안내가 있다. 문서의 episode schema는 embedding·label·success·time이며 같은 VLA의 checkpoint lineage는 식별되지 않는다. Drive tensor payload는 미검사 |
| [irom-princeton/rapid-policy-evaluation](https://github.com/irom-princeton/rapid-policy-evaluation) | `e9e6cb567f87`, 3 files | Paired real/sim, additional sim, heldout real의 interface가 구현되어 있다. Tree에는 실험·예제 자료가 있다. 이번에는 payload를 전수 읽거나 C6용 연속 RL join을 입증하지 않았다 |
| [dasnyder5/nscore](https://github.com/dasnyder5/nscore) | `68c0a3453248`, 5 files | `step()` 기반 sequential test, multi-policy notebook, RL comparison script가 있다. RL script는 pairwise 비교에 global error budget을 나눈다. LBM/RL 파일 목록을 확인했으며 전체 raw outcome payload는 미검사 |

총 **8개 주소 중 7개 접근 성공 / 26개 text source / 441,388 bytes**다. Source를 내려받아 읽은 것이 upstream package 설치나 알고리즘 재현을 의미하지 않는다. N-SCORE는 기성 baseline으로 유용하지만 공개된 LBM 비교 또는 일반 RL return을 VLA online post-training 이력으로 전환할 수 없다.

## RACE 실제 JSON payload

- URL: [data.json](https://changyeon.site/race/data.json)
- 54,809 bytes, SHA256 `8ee38c394708937b41fccbe5f84cb76e21a021ca61bc5b827430973788a648a1`
- 고정 release/commit URL이 아니므로 hash가 재검사 identity다. 서버 `Last-Modified`: 2026-10-16 UTC.
- Top-level: `provenance`, `notes`, `real`, `simulation`.

| 부분 | 실제 구조 | 해석 |
|---|---|---|
| `real.vla.raw` | 27행: 3 tasks × 9 steps. Task/step 중복 0 | `success_rate`와 4개 offline score의 집계. Trial array·seed·reset ID는 없다 |
| `real.dp.raw` | 30행: 3 tasks × 10 epochs. Task/epoch 중복 0 | `successes`, `trials`, `success_rate`와 score. 성공 횟수와 분모가 있어도 개별 trial의 초기 조건·순서·paired outcome은 복원되지 않는다 |
| `simulation` | 3 reference-source 묶음의 method별 mean/interval | Task/run/checkpoint/trial의 원본 평가 행렬이 아니다 |

`raw`는 그래프의 정규화 전 checkpoint 수치라는 의미다. **Robot trial raw log라는 뜻으로 읽지 않는다.** 본문과 project는 BC/fine-tuning checkpoint를 평가한다. 이 자료를 RL reward exploitation의 직접 증거로 사용할 수 없다. Project도 VLA plotting bundle이 9 checkpoints/task임을 밝힌다. 보이지 않는 10번째 값을 추정하거나 57개 점을 1,800개의 개별 trial로 세지 않았다. [Project protocol](https://changyeon.site/race/)

첫 summary 확장 때 두 family에 모두 `step`을 가정해 한 번 `KeyError`가 났다. 실제 DP schema의 `epoch`를 확인해 고쳤고 최종 audit는 exit 0이다. 원본을 수정하거나 missing 값을 채우지 않았다.

## 데이터 gate 판정

| 필수 연결 | 이번 결과 |
|---|---|
| 동일 native VLA의 RL update/checkpoint lineage | 미확보. RACE는 task별 fine-tuning 집계, 다른 공개 예제는 다른 문제 설정 |
| 학습 reward/evaluator version 및 training-data overlap | C6에 필요한 연결 미확보 |
| Checkpoint별 independent evaluation trial과 비용 | RACE 집계에는 없음. 다른 repo의 payload 전체 부재를 주장하지 않음 |
| 독립 reference와 selector-visible outcome 분리 | 현 자료로 구성하지 않음 |

따라서 **data gate 미통과**다. 이를 “모든 공개 데이터에 없다” 또는 “방법이 효과 없다”로 일반화하지 않는다. 기존 통계 방법을 cartpole에서 다시 돌리는 것은 이 gate를 해결하지 않으므로 수행하지 않았다. 현재의 신규성 판정은 source 접근 실패와 독립적으로, 이미 존재하는 formulation과 방법에 근거한다.
