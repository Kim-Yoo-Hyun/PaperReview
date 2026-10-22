# C2 공개 평가·데이터 정적 감사

- 확인일: **2026-10-21 KST**
- 범위: source text·AST의 literal task 선언·공개 dataset 파일 목록. 외부 Python module을 import/실행하지 않았고 trajectory를 재생하거나 성능을 측정하지 않았다.
- Revision·SHA256·검토 범위: [C2_SOURCE_AUDIT.json](./C2_SOURCE_AUDIT.json).
- 연구 판단: [C2_REVIEW.md](./C2_REVIEW.md). 아래 발견은 기존 benchmark의 오류를 입증한 것이 아니라 **C2 질문으로 전용할 때의 조건**이다.

**후속 상태:** 아래는 초기 정적 감사 기록이다. 이후 [Docker 1차 검증](../../experiments/vla_rl_c2_first_pass/RESULTS.md)에서 400개 episode metadata, training instruction 200개, 실제 HDF5/planner 12쌍과 training route trace 50개를 검사했다. 초기의 payload 미확인 항목은 해당 결과로 갱신되었으며, 완전한 reward/coverage와 native runtime은 미충족으로 종료했다. [빌드업 판단](./C2_BUILDUP_RESULT.md).

## 1. SIMPLER-IN: 조건과 evaluator의 의미

검토 revision: `478fad54689126e4303bdc6bcb3c8e064e5934ab`.

| 확인한 코드 | 정적 사실 | C2에서의 처리 |
|---|---|---|
| [Path reset·actor](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/envs/simpler_in_envs.py#L56) | `hidden`에 따라 source x가 −0.13/−0.20이고 활성 collision wall도 달라진다. Wall에는 collision만 생성한다. | 같은 seed라도 hidden을 바꾼 두 rollout을 instruction-only 개입이라고 부를 수 없다. 지시가 다른 물리 환경의 정보를 알려주는 진단과 구별한다. |
| [Path evaluate](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/envs/simpler_in_envs.py#L194) | `constraint_ok`는 native success와 pre/post overwall 부재의 conjunction이다. `entry_side`, wall contact는 따로 기록한다. | `constraint_ok`를 모든 task에 동일한 순수 compliance bit로 해석하지 않는다. 명령의 접근·퇴장 의미와 판정의 대응을 먼저 정의한다. |
| [Grasp evaluate](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/envs/simpler_in_envs.py#L265) | 안정 grasp 뒤 contact 평균을 장축에 투영한다. Contact가 없으면 gripper/link 위치를 대신 쓴다. | 실제 contact 근거와 fallback 근거를 구분해 label confidence를 기록한다. |
| [Place evaluate](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/envs/simpler_in_envs.py#L374) | 첫 contact 또는 success 시 landing zone을 고정한다. Final zone은 별도 값이다. | 첫 착지 조건과 최종 배치 조건을 혼용하지 않는다. |

[일반 client](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/eval/eval_client.py#L46)는 model에 image와 instruction을 넘기고 `info`를 결과로 남긴다. 확인한 호출부에서 evaluator 값의 직접 전달은 없다. 반면 [π0 client](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/eval/eval_client_pi0.py#L34)는 전체 `obs`를 state field로 전달하므로 downstream adapter까지 확인하지 않고 전체 stack의 leakage 부재를 선언할 수 없다.

[요약기](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/eval/summarize.py#L24)는 `success/n`과 `joint/success`를 출력한다. C2 primary는 `joint/n`으로 별도 정의한다. 이 변경은 새 metric 기여가 아니다.

## 2. RoboFollow Scene 3: 실제 분할 후보

검토 revision: `f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8`.

[task 선언](https://github.com/AutoLab-SAI-SJTU/RoboFollow/blob/f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8/tasks/scene3.py#L131)의 16개 literal `_reg` 호출을 정적으로 확인했다.

| Native training block | Source | Arm / destination | Route와 orientation |
|---|---|---|---|
| Right 8개 | red 2, green 3 | right / blue label 6 | via 4 또는 5 × short_front 또는 long_front |
| Left 8개 | yellow 4, blue 5 | left / green label 1 | around 2 또는 3 × short_right 또는 long_right |

**연구자 해석:** 전체 16개를 섞으면 source·arm·destination·route 표현이 함께 달라진다. 첫 C2 진단에서는 right block만 선택하여 arm과 destination을 고정한다. 이는 다양한 로봇으로의 일반화 실험이 아니다.

[Scene 3 L2 생성](https://github.com/AutoLab-SAI-SJTU/RoboFollow/blob/f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8/evaluation/scene3.py#L315)은 route의 표현/참조물과 orientation 표현을 재작성한다. `_add_task`는 원래 task의 판정 필드를 유지한다. 예를 들어 `short_front`와 `long_right`는 같은 target yaw에 대응한다. 따라서 이 L2 명칭만으로 새로운 executed triple을 학습에서 배제했다고 볼 수 없다. C2는 별도의 명시적 task membership이 필요하다.

[route evaluator](https://github.com/AutoLab-SAI-SJTU/RoboFollow/blob/f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8/evaluation/scene3.py#L626)는 들어 올린 object와 correct/wrong waypoint의 거리 조건을 확인한다. 이는 모든 시간의 접촉 금지나 전체 경로 안전성 보장이 아니다. C2는 우선 이 제한된 waypoint 의미를 사용하며 collision safety 주장으로 확장하지 않는다.

[π0.5 adapter](https://github.com/AutoLab-SAI-SJTU/RoboFollow/blob/f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8/pi05.py#L115)는 세 RGB view, 14D state, instruction을 모델에 전달한다. 이 경계에서 trajectory 판정 값은 입력에 넣지 않는다. Simulator 전체 정보 흐름의 동적 검증은 미실행이다.

## 3. 실제 파일 목록과 내용 검증을 구분

공개 [dataset metadata](https://huggingface.co/datasets/AutoLab-SJTU/robofollow-data/tree/bbb1e266ed585f1557773de5a3f1e3b4cd944f97/scene3)를 revision `bbb1e266ed585f1557773de5a3f1e3b4cd944f97`로 고정했다.

- 선택한 right block 8개 task마다 HDF5 data 50개, instruction JSON 50개, trajectory pickle 50개의 **파일명**을 확인했다.
- 이들은 서로 다른 150 demos가 아니다. 동일 episode의 서로 다른 저장 표현일 수 있다.
- `collection.json`·`complete.json` 등 부가 metadata의 존재는 task마다 다르다. 파일 목록의 차이를 곧바로 품질 차이로 해석하지 않는다.
- Payload·성공·제약 만족·누락 frame·scene/state 중복·episode 길이는 아직 확인하지 않았다. “400개 검증된 성공 demonstrations”라고 기록하지 않는다.
- Holdout task의 demonstration은 학습, reward-model fitting, normalization, hyperparameter 선택에 쓰지 않는다. 실제 episode membership과 split leakage 검사는 별도 G0 작업이다.

## 4. 설계만 확인된 4/4 분할

[C2_SPLIT_DRAFT.json](./C2_SPLIT_DRAFT.json)은 8개 native task를 아래처럼 지정한다. `o`는 red/green, `w`는 waypoint 4/5, `r`은 short_front/long_front의 binary index다. Training은 `r = o XOR w`, holdout은 나머지다.

| 구분 | 실제 task ID |
|---|---|
| Train | `r_pick2_via4_to6_short_front` |
| Train | `r_pick2_via5_to6_long_front` |
| Train | `r_pick3_via4_to6_long_front` |
| Train | `r_pick3_via5_to6_short_front` |
| Holdout | `r_pick2_via4_to6_long_front` |
| Holdout | `r_pick2_via5_to6_short_front` |
| Holdout | `r_pick3_via4_to6_short_front` |
| Holdout | `r_pick3_via5_to6_long_front` |

Training 4개에서 각 factor의 두 값은 2회씩, 각 factor pair의 네 조합은 1회씩 등장한다. **새 triple은 남기되 atomic/pair coverage를 갖는다는 조합론적 성질만 검증했다.** 실제 trajectory의 state/action support와 물리적 양방향 feasibility를 입증한 것은 아니다. Parity 관계 자체가 학습 shortcut이 될 수 있으므로 이 작은 분할 하나의 성능을 일반적인 composition 능력으로 주장하지 않는다.

이 분할은 기존 orthogonal design 원리를 적용한 진단 초안이다. 새로운 split 알고리즘이나 benchmark로 제안하지 않는다. Episode·checkpoint·환경 runtime·evaluation seed는 미고정이며, [protocol](./C2_PROTOCOL.md)의 gate가 충족될 때 실행 명세로 전환한다.
