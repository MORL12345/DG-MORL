This repository is to show the abosulte performance of our DG-MORL algorithm comparing with the baseline algorithms we used in our work, i.e. GPI-PD and GPI-LS.
The term "absolute performance" is a comparison between the maximum performance achievable and the performance of the evaluated algorithms. 
We used the metric of "maximum utility loss" (MUL) to measure absolute performance which is also used in the work of Alegre et al. [1].
The MUL of a policy set $\Pi$ is: $MUL(\Pi)=max_{\bf{w}\in{\mathcal{W}}}(v_{\bf{w}}^{*}-max_{\pi\in\Pi}v_{\bf{w}}^{\pi})$.

where $v_{\bf{w}}^{*}$ is the return value of the preference weight $\bf{w}$ of the best policy, $v_{\bf{w}}^{\pi}$ is the return value of the preference weight $\bf{w}$ of policy $\pi$, $\mathcal{W}$ is the weight simplex, $\bf{w}$ is the preference weight vector, and $\pi$ is the policy from $\Pi$.

In the three benchmark environments we used, DST and Minecart have a known Pareto front, therefore it is easy to get the maximum achievable utility. The maximum achievable utility for DST is 5.5098 while it is 0.2881 for Minecart. We show the result of MUL in DST and Minecart in the following figures.

![figurea](https://github.com/MORL12345/DG-MORL/blob/main/MUL/MUL%20DST.png)

![figurea](https://github.com/MORL12345/DG-MORL/blob/main/MUL/MUL%20minecart.png)

As the MO Hopper does not have a known Pareto front we cannot know the true maximum achievable utility, we consequently trained 5 single-objective TD3 (SO-TD3) agents using the preference weights as [1, 0], [0.75, 0.25], [0.5, 0.5], [0.25, 0.75], [0,1]. Each SO-TD3 agent is trained for 1.5 million (M) steps, therefore the training budget is 5*1.5M = 7.5M steps. Compared to the SO-TD3 agents, our algorithm is only trained by 0.15M steps, which takes only the 2% training budget.
It is therefore a fair approximation of the maximum achievable for MO Hopper environment in our context. By iterate through the preference weight simplex, and using the corresponding policy from the policy set issued by the SO-TD3 agents, we can get the approximated maximum achievable utility of MO Hopper, which is 225.5106. Moreover, as GPI-PD is state-of-the-art MORL algorithm, therefore the comparison between our algorithm and GPI-PD can to some degree reflect the gap between the maximum achievable utitliy when using MORL algorithm. 
We show the result of MUL in MO Hopper in the following figures.

![figurea](https://github.com/MORL12345/DG-MORL/blob/main/MUL/MUL%20MO%20Hopper.png)

[1] Alegre, L. N., Bazzan, A. L., Roijers, D. M., Nowé, A., & da Silva, B. C. (2023, May). Sample-Efficient Multi-Objective Learning via Generalized Policy Improvement Prioritization. In Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems (pp. 2003-2012).
