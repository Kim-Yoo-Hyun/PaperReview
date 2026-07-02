# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, open-vocabulary, Graph Reasoning
- Paper link: ./2024/CVPR/2024_CVPR_Open3DSG-Open-Vocabulary-3D-Scene-Graphs-from-Point-Clouds/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data.
- We present Open3DSG the first approach for learning to predict open-vocabulary 3D scene graphs from 3D point clouds.
- We compare our method with both zero-shot and fully-supervised baselines for 3D scene graph prediction.

## 원리적 동기
- 3D scene graphs are an emergent graph-based representation facilitating various 3D scene understanding tasks.
- In contrast to other more object-centric 3D scene representations, the key advantage of 3D scene graphs is the ability to also represent relationships between scene entities, such as ...
- We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data.

## 핵심 방법론
- We compare our method with both zero-shot and fully-supervised baselines for 3D scene graph prediction.
- As a zero-shot approach, our method is less susceptible to class imbalance.
- Here we compare the prediction performances for objects and predicates based on their frequency in the training set.
- Training samples of classes that are observed in a higher frequency are generally learned more effectively than rarer classes.
- Most scene graph methods for instance, uses a focal loss to solve the problem of class imbalance in the training set.
