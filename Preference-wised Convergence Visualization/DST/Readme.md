We are showing the convergence process of DST along the specific preferences, as per **Reviewer 3Yt8's** comment: *"Quantitatively, I would be interested in seeing, e.g., a pareto plot of collected treasure and time spent for the Deep Sea Treasure environment, evaluated at algorithm convergence and for different preference vectors. "*.

This file is about the details of the convergence process of our DG-MORL algorithm in the DST environment. We pick 10 representative weight vectors that direct to **different** treasures when given the optimal policy set. This helps to evaluate the convergence, i.e. when the 10 curves all converge to different values, the training process converge.
Similar to the experiment conducted in https://github.com/MORL12345/DG-MORL/tree/main/Pareto%20Front%20Approximation%20Process/DST , the evaluation frequency is uneven, this is for the sake of showing the learning process and we have given the clear scale on the x-axis to help to understand.

# Time penalty convergence curve
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Preference-wised%20Convergence%20Visualization/DST/time%20penalty%20convergence.png)

# Treasure collected convergence curve
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Preference-wised%20Convergence%20Visualization/DST/treasure_collected_convergence.png)

For both the time penalty curve and the treasure collected curve, it is clear that the 10 curves converge to different values (the correct values). 
Most of the curves converge at the 12000th step. However, there exists some fluctuation, this is because the solution spaces for the preference weight in the middle are quite narrow. The whole training process converges after 28000 steps.

# Utility convergence curve
![figurea](https://github.com/MORL12345/DG-MORL/blob/main/Preference-wised%20Convergence%20Visualization/DST/utility_convergence.png)

Unfortunately, due to the limited time, we can only conduct the visualization once, we can do a repeat experiment with the random seeds we mentioned in the paper in the future and add them to the revised manuscript. 
