import numpy as np

cohesion = []
for itr in [2,
            7, 15, 42,
            78
            ]:
    name = "Algorithm/Result/DGMORL/Minecart/Roll_back_span_estimation/ori_data/_15_" + str(itr) + ".npy"
    a = np.load(name)
    cohesion.append(a)
    print(f"a:{a}")

mean_ = np.mean(cohesion, axis=0)
max_ = np.max(cohesion, axis=0)
min_ = np.min(cohesion, axis=0)
save_to = "Algorithm/Result/DGMORL/Minecart/Roll_back_span_estimation/_15"
np.save(save_to, mean_)
for i in range(len(mean_)):
    print(
        f"i:{i + 1}\nmean:{np.round_(mean_[i], 2)}\nmax:+{np.round_(max_[i] - mean_[i], 2)}\nmin:{np.round_(min_[i] - mean_[i], 2)}")
    print("----------------------------")
