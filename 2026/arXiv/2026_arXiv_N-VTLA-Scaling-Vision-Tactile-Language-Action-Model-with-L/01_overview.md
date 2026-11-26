# N₀-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 v1 PDF 4–10, 13–14쪽, §§3–5, Fig. 9 확인. [서지·게재 상태](https://arxiv.org/abs/2607.23782)

- Year/Venue: 2026 / arXiv
- Authors: NeoteAI Team, Fudan TEAI Team
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, tactile sensing, Flow Matching, offline RL, advantage conditioning
- Official paper: https://arxiv.org/abs/2607.23782
- Code/Project: https://research.neoteai.com/n0-vtla/

## 연구 질문과 기여

범용 정책이 촉각을 이용해 접촉 조작을 수행하고 배포 후 수집한 성공·실패 기록에서 추가 상호작용 없이 개선될 수 있는지 묻는다.

잠재 촉각 토큰을 시각·언어 표현 및 연속 행동 전문가와 결합해 사전학습한다. 선택 단계인 ALTER는 고정된 배포 궤적에서 진행도와 국소 변화로 advantage 표지를 구성한 뒤 조건부 행동 정책을 다시 학습한다.

## 평가 범위

실물 NeoReal과 시뮬레이션의 기본 정책 평가 범위가 다르다. Fig. 9의 오프라인 개선 비교는 수건 접기, 가방 포장, 상자 접기 세 실물 과제에 한정한다. [원문 및 평가 절](https://arxiv.org/pdf/2607.23782v1#page=8)

## 선정 근거

실제 촉각을 사용하는 VLA에서 고정 배포 자료의 advantage 조건화가 주는 추가 이득을 검토할 비교 방법이다. 프리프린트로 등록했다.

## 공개 자료의 확인 범위

- 코드는 시각·촉각·언어 정책과 행동 생성 구현 · n0vtla/models_pytorch/n0vtla_policy.py에서 확인했다. [코드 배포처](https://github.com/neoteai/N0-VTLA/blob/5146e06499099fb14fcc44afdf037b6eeeeaeb89/README.md)
- 가중치는 N₀-VTLA 기반 체크포인트 · model.safetensors에서 확인했다. [가중치 배포처](https://huggingface.co/NeoteAI/n0-vtla-base/blob/efce64fbec32cdf7e951480adcab3c05e9dc18b4/model.safetensors)
- OpenNeoData_OXT는 접근 승인이 필요하다. 논문 학습·배포 궤적과 일치하는 에피소드의 공개 범위는 미확인이다. [데이터 카드](https://huggingface.co/datasets/NeoteAI/OpenNeoData_OXT)
