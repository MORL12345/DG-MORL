This repository is about **Reviewer 3Yt8's** comment - *"Quantitatively, I would be interested in seeing, e.g., a pareto plot of collected treasure and time spent for the Deep Sea Treasure environment, evaluated at algorithm convergence and for different preference vectors. "*. We are showing the Pareto front approximation.

We have put the Pareto front approximation process during the training in DST. The true Pareto front is found at 5000 steps, for the case of simplicity, we only visualize the Pareto approximation process up to this point. However, this does not mean the training process is fully converged as finding the true Pareto front cannot guarantee that each preference weight is correctly aligned with the solution on the Pareto front. Please refer to https://github.com/MORL12345/DG-MORL/tree/main/Preference-wised%20Convergence%20Visualization/DST to see the detailed convergence over each objective of DST. Also, we would like to show the detailed process of the Pareto front approximation, therefore the visualization is not periodically done but conducted at steps 50, 500, 1500, and 5000. The visual figures also include the Pareto front approximations derived from the initial demonstrations, depicted as black triangles.

# Pareto front Approximation @ 50th step
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Pareto%20Front%20Approximation%20Process/DST/Step_50.png)

This is a very early stage, the agent has rare knowledge about the task. All the solutions it gives are at (0, -100). This means that the agent cannot collect any treasure and wander around in the environment.

# Pareto front Approximation @ 500th step
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Pareto%20Front%20Approximation%20Process/DST/Step_500.png)

The agent discovers two optimal solutions on the true Pareto front. Note that these two solutions are the most easily found ones as they are very near to the initial position of the agent.

# Pareto front Approximation @ 1500th step
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Pareto%20Front%20Approximation%20Process/DST/Step_1500.png)

At this stage, the agent has approximated 80% of the true Pareto front. This also shows that our algorithm is very sample efficient as in such a limited training budget it can recover most of the optimal solutions.

# Pareto front Approximation @ 5000th step
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Pareto%20Front%20Approximation%20Process/DST/Step_5000.png)

The agent has discovered the true Pareto front.

We have shown how the true Pareto front in DST is found by our agent in a very short period. 
Please refer to https://github.com/MORL12345/DG-MORL/tree/main/Preference-wised%20Convergence%20Visualization/DST for further details about the training process.
