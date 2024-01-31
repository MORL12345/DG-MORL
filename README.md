# Demonstration-Guided Multi-Objective Reinforcement Learning (DG-MORL)
This is the implementation repository for review. 

Multi-objective reinforcement learning (MORL) is increasingly relevant due to its resemblance to real-world scenarios requiring trade-offs between multiple objectives. Catering to diverse user preferences, traditional reinforcement learning faces amplified challenges in MORL. To address the difficulty of training policies from scratch in MORL, we introduce demonstration-guided multi-objective reinforcement learning (DG-MORL). This novel approach utilizes prior demonstrations, aligns them with user preferences via corner weight support, and incorporates a self-evolving mechanism to refine suboptimal demonstrations. Our empirical studies demonstrate DG-MORL's superiority over existing MORL algorithms, establishing its robustness and efficacy, particularly under challenging conditions. We also provide an upper bound of the algorithm's sample complexity.

We upload the general version of the implementation. The user need to tailor it to the specific experiment they want to do. The dependencies are exported to DGMORL.yml
To reconstruct the running environment on your machine:
Please do:

conda env create -f DGMORL.yml

You can go to /Algorithm/DG_MORL.py to run the experiment of DST and Minecart.
To run the MO Hopper experiment, just go to /Algorithm/DG_MORL_continuous.py 

The initial demos are in /Algorithm/initial demos (Minecart and MO Hopper). The DST initial demonstrations are hard-coded in the script /Algorithm/DG_MORL.py 

This implementation is adapted from the work of Alegre et al. "Sample-Efficient Multi-Objective Learning via Generalized Policy Improvement Prioritization"
Lucas N. Alegre, Ana L. C. Bazzan, Diederik M. Roijers, Ann Nowé, Bruno C. da Silva
AAMAS 2023
Paper: https://arxiv.org/abs/2301.07784
