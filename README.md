# Demonstration guided multi-objective reinforcement learning (DG-MORL).
This is the implementation repository for review. 

Multi-objective reinforcement learning (MORL) is increasingly relevant due to its resemblance to real-world scenarios requiring trade-offs between multiple objectives. Catering to diverse user preferences, traditional reinforcement learning faces amplified challenges in MORL. To address the difficulty of training policies from scratch in MORL, we introduce demonstration-guided multi-objective reinforcement learning (DG-MORL). This novel approach utilizes prior demonstrations, aligns them with user preferences via corner weight support, and incorporates a self-evolving mechanism to refine suboptimal demonstrations. Our empirical studies demonstrate DG-MORL's superiority over existing MORL algorithms, establishing its robustness and efficacy, particularly under challenging conditions. We also provide an upper bound of the algorithm's sample complexity.

We upload the general version of the implementation. The user need to tailor it to the specific experiment they want to do. The dependencies are exported to DGMORL.yml
To reconstruct the running environment on your machine:
Please do:
'conda env create -f DGMORL.yml'
