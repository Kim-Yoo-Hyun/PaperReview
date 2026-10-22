# C4 데이터와 공개 구현 감사

- Checked: 2026-10-21 KST
- Raw evidence: [DATA_AUDIT.json](./DATA_AUDIT.json), [CODE_AUDIT.json](./CODE_AUDIT.json).
- Data payload은 Docker에서 파싱했다. Code는 pinned source를 정적으로 읽었고 실행하지 않았다. Metadata 존재와 모델 실행 가능성을 구분한다.

## 1. 데이터에서 식별 가능한 것

### Robometer: `robometer/rbm-1m-ood`

- Revision: `3f3ee69ecc0ee0db627684da7d599ec26d08175c`.
- 공개 manifest가 가리키는 작은 Parquet/JSON metadata 17개를 읽었다. [고정 release](https://huggingface.co/datasets/robometer/rbm-1m-ood/tree/3f3ee69ecc0ee0db627684da7d599ec26d08175c)
- LeRobot data 18,261 row와 episode metadata 571 row, task table 41 row가 있다. Episode별 quality는 successful 233, failure 166, suboptimal 172다. 18,261개를 독립 trial로 세지 않는다.
- Frame fields: `data_source`, `episode_index`, `frame_index`, `id`, `index`, `is_robot`, `partial_success`, `quality_label`, `task_index`, `timestamp`.
- `timestamp`는 모든 episode에서 0부터 시작하고 10Hz 간격의 clip time이다. `episode_index` 역시 export index이므로 policy update step이라고 해석하지 않는다.
- `partial_success`는 이 export의 모든 frame에서 빈 문자열이다. `policy_id`, checkpoint hash, reward version, training round, action/log-probability는 확인한 column에 없다.
- 같은 repository의 `train/metadata.parquet`는 1,160 row·104 task string·11 source를 담는다. LeRobot export 571 episode와 규모/구성이 다르다. 실제 episode identity와 view join을 확인하지 않고 합쳐 표본 수를 늘리지 않는다.
- `export_summary.json`의 split은 `eval`, LeRobot `meta/info.json`은 `train: 0:571`이다. 폴더 이름을 reward-model 학습/평가의 독립성 증거로 사용하지 않는다.

Code의 policy-ranking sampler는 non-RoboArena trajectory를 task와 `quality_label`로 묶는다. USC Franka loader도 folder의 task·optimality·attempt를 읽는다. 따라서 **`policy_ranking`이라는 이름이 곧 학습 checkpoint 간 비교 dataset이라는 이전 기대는 성립하지 않았다.** 원 수집자의 별도 로그가 없다고 단정하지 않으며, 이번에 확인한 공개 export로는 join을 만들 수 없다는 뜻이다. [Sampler](https://github.com/robometer/robometer/blob/352d160389daa964788de1ec933d1925f3a6de4f/robometer/data/samplers/eval/progress_policy_ranking.py), [Loader](https://github.com/robometer/robometer/blob/352d160389daa964788de1ec933d1925f3a6de4f/dataset_upload/dataset_loaders/usc_franka_policy_ranking_loader.py)

### RoboReward: `teetone/RoboReward`

- Revision: `469b9af76e8539e8d2ac553b081307738fd92ca5`. Train/val/test JSONL을 전부 읽었다. [고정 release](https://huggingface.co/datasets/teetone/RoboReward/tree/469b9af76e8539e8d2ac553b081307738fd92ca5)
- Train 45,072 / val 6,232 / test 2,831, 총 54,135 row. 세 split 모두 `file_name`, `task`, `reward`, `gpt5_mini_check` 네 필드다.
- Test의 score 1/2/3/4/5는 각각 689/641/556/418/527 row다. Test의 `robo_arena/` prefix는 1,000 row다. 이는 video–task row 수이며 독립 physical episode 수라고 확정하지 않는다.
- Train의 labels 전체를 독립 인간 판정으로 간주하지 않는다. 저자는 synthetic relabeling/clipping을 사용하고 test를 human-verified로 설명한다. 이번 파싱은 그 설명을 검증하는 human reannotation이 아니다. [Dataset card](https://huggingface.co/datasets/teetone/RoboReward)
- `gpt5_mini_check`는 제공된 정답 점수의 일관성을 평가한 설명이다. Query 전에 selector에 제공하면 test/train label 정보가 새는 경로다. `file_name`의 source·camera·변형 표기도 image-only feature의 대체물로 쓰지 않는다.
- Policy/checkpoint·수집 순서·RL round·reward prediction·reward version·action은 이 release의 row에 없다. Filename의 A/B 등의 표기를 근거 없이 정책 version으로 해석하지 않는다.

## 2. 통과한 전제와 실패한 전제

| 전제 | 결과 | 해석 |
|---|---|---|
| 실제 성공·실패를 구분하는 metadata가 공개됨 | 통과 | 정적 reward 평가 후보가 존재 |
| Task/robot source를 구분할 정보가 있음 | 부분 통과 | Source와 실제 embodiment/calibration은 같지 않음 |
| 같은 native VLA의 RL update 전후 policy identity | 미충족 | 후보의 시간순 shift 진단을 구성할 근거 없음 |
| 당시 reward prediction/version과 query 이전 정보 | 미충족 | 현재 reward를 나중에 돌린 점수로 당시 악용을 입증할 수 없음 |
| 독립 outcome과 reward training contamination join | 부분/미확정 | Human-verified test라는 출처 설명과 모든 모델에 대한 독립성은 별개 |
| Action/state/success semantics를 연결한 native rollout | 미충족 | Reward video dataset을 그대로 VLA RL replay로 쓸 수 없음 |

관측된 정적 자료 `D={(video, instruction, label)}`는 서로 다른 policy update 과정에서 똑같이 만들어질 수 있다. 예를 들어 특정 실패가 학습 중 증가한 경우와, 여러 정책·카메라의 실패를 모아둔 경우를 이 필드만으로 구별할 수 없다. 따라서 무작위 row split을 early/late policy라고 부르거나 static accuracy 변화로 RL 이득을 결론 내리지 않는다. 이는 데이터 식별성에 대한 연구자 판단이며 정책 효과를 측정한 실험 결과가 아니다.

## 3. 구현 계약 감사

| Repository / 고정 commit | 확인한 경로 | C4에 주는 제약 |
|---|---|---|
| `ripl/progressor` / `1482845dab2b55816708633494b4a52163f44c91` | `DrM/train_mw.py`, `metaworld_env.py`, online dataloader | Expert + replay KL 업데이트가 실제 함수로 존재. `.cuda()` 사용. 본문식/공개 구현 차이는 [문헌 검토](./LITERATURE_REVIEW.md) 참조 |
| `USC-Lira/language_active_learning` / `a4b3681674c8839e889d4f34f07ac720454c1c8a` | `next_traj.py`, `info.py` | 이미 주어진 trajectory embedding pool에서 query index를 반환. Native VLA RL update code로 간주하지 않음 |
| `CMU-IntentLab/uncertainty_aware_policy_steering` / `f7bad4d7cd6d5e4350751a958ba9bb146a99ecec` | README, `policy/sim_policy.py` | Checkpoint·world model·calibration·action correction을 함께 요구. Wrapper는 CUDA 사용. Binary reward label budget과 직접 교환 불가 |
| `robometer/robometer` / `352d160389daa964788de1ec933d1925f3a6de4f` | Finetune 안내, dataset loaders, policy-ranking sampler | Reward adaptation 경로는 있으나 검수 acquisition의 완성된 공정 실험이 자동 제공되는 것은 아님 |
| `robometer/robometer-policy-learning` / `d5fd0b350d08a69ea6c87af3a1c43a0450593c15` | Real-robot 안내, DSRL LIBERO config, async reward wrapper | `pi0_libero` checkpoint 경로와 chunk execution 20 설정 존재. Async success window가 종료에도 관여하므로 reward 교정과 episode 길이가 함께 달라질 수 있음 |
| `Lumina04/CARE` / `17391c6912eb60d0c91deb816b24b6ae927c861d` | README / tree | Math·Knights-and-Knaves training 경로. Robotics 실험/변환 검증을 제공한다는 근거가 아님. Acquisition 전체 구현을 재현한 것은 아님 |

[Robometer termination wrapper](https://github.com/robometer/robometer-policy-learning/blob/d5fd0b350d08a69ea6c87af3a1c43a0450593c15/robometer_policy_learning/envs/async_reward_relabel_wrapper.py#L403), [DSRL config](https://github.com/robometer/robometer-policy-learning/blob/d5fd0b350d08a69ea6c87af3a1c43a0450593c15/robometer_policy_learning/configs/dsrl_libero_config.yaml), [PROGRESSOR update](https://github.com/ripl/progressor/blob/1482845dab2b55816708633494b4a52163f44c91/DrM/metaworld_env.py#L401).

후보 실행 경로는 존재한다. 하지만 현재 Docker는 Linux ARM64·약 7.65GiB 메모리이며 CUDA가 없다. Metadata parsing 성공은 π0 + reward model + RL learner 실행 검증이 아니다. Code의 CUDA 가정만으로 모든 CPU port가 불가능하다고 단정하지도 않는다. 이번에는 novelty/data gate가 먼저 실패해 모델 다운로드나 환경 이식·학습을 시작하지 않았다.
