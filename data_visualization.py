import random

import numpy as np
from matplotlib import pyplot as plt

metrics = ["EU", "Demo_num_estimation", "Roll_back_span_estimation", "ablation", "quality", "threshold"]
base_path = "Algorithm/Result"
alg_names = [
    "DGMORL",
    # "GPI_PD",
    # "GPI_LS",
    # "ablation"
]
env_name = "Minecart"
postfix = "Roll-back Step Evaluation"
time_steps = str(10000)
metric = metrics[2]
spans = [2, 10, 15, 42]
# spans = [3, 100, 300, 42]
# spans = [1, 2, 3, 5, 42]
thresholds = [0.8, 0.9, 1]
demo_nums = [2,
             3,
             5,
             42]
seeds = [
    2,
    7,
    15,
    42,
    78,
]
DG_MORL_EUs = []
DG_MORL_EUs_0 = []
DG_MORL_EUs_1 = []
DG_MORL_EUs_2 = []
DG_MORL_EUs_ablation = []
GPI_PD_EUs = []
GPI_LS_EUs = []
if metric == "EU" or metric == "ablation" or metric == "quality":
    seeds = seeds
if metric == "Demo_num_estimation":
    seeds = demo_nums
if metric == "Roll_back_span_estimation":
    seeds = spans

for seed in seeds:
    for alg_name in alg_names:

        file_name = base_path + "/" + alg_name + "/" + env_name + "/" + metric + "/" + "_" + str(seed) + ".npy"

        if alg_name == "DGMORL":
            if metric == "quality":
                file_name = base_path + "/" + alg_name + "/" + env_name + "/quality/" + "good/" + "_" + str(
                    seed) + ".npy"
                DG_MORL_EU_0 = np.load(file_name)
                DG_MORL_EUs_0.append(DG_MORL_EU_0)
                file_name = base_path + "/" + alg_name + "/" + env_name + "/quality/" + "medium/" + "_" + str(
                    seed) + ".npy"
                DG_MORL_EU_1 = np.load(file_name)
                DG_MORL_EUs_1.append(DG_MORL_EU_1)

                file_name = base_path + "/" + alg_name + "/" + env_name + "/quality/" + "bad/" + "_" + str(
                    seed) + ".npy"
                DG_MORL_EU_2 = np.load(file_name)
                DG_MORL_EUs_2.append(DG_MORL_EU_2)
            if metric == "threshold":
                file_name = base_path + "/" + alg_name + "/" + env_name + "/threshold/" + "8/" + "_" + str(
                    seed) + ".npy"
                DG_MORL_EU_0 = np.load(file_name)
                DG_MORL_EUs_0.append(DG_MORL_EU_0)
                file_name = base_path + "/" + alg_name + "/" + env_name + "/threshold/" + "9/" + "_" + str(
                    seed) + ".npy"
                DG_MORL_EU_1 = np.load(file_name)
                DG_MORL_EUs_1.append(DG_MORL_EU_1)

                file_name = base_path + "/" + alg_name + "/" + env_name + "/threshold/" + "10/" + "_" + str(
                    seed) + ".npy"
                DG_MORL_EU_2 = np.load(file_name)
                DG_MORL_EUs_2.append(DG_MORL_EU_2)

            if metric == "ablation":
                file_name = base_path + "/" + alg_name + "/" + env_name + "/EU/" + "_" + str(seed) + ".npy"
            DG_MORL_EU = np.load(file_name)
            DG_MORL_EUs.append(DG_MORL_EU)
        elif alg_name == "GPI_PD":
            if metric == "ablation" or metric == "quality" or metric == "threshold":
                file_name = base_path + "/" + alg_name + "/" + env_name + "/EU/" + "_" + str(seed) + ".npy"
            GPI_PD_EU = np.load(file_name)
            GPI_PD_EUs.append(GPI_PD_EU)
        elif alg_name == "GPI_LS":
            if metric == "ablation":
                file_name = base_path + "/" + alg_name + "/" + env_name + "/EU/" + "_" + str(seed) + ".npy"
            GPI_LS_EU = np.load(file_name)
            GPI_LS_EUs.append(GPI_LS_EU)
            print(file_name)
            print(GPI_LS_EU)
        elif alg_name == "ablation":
            file_name = base_path + "/DGMORL/" + env_name + "/" + metric + "/" + "_" + str(seed) + ".npy"
            DG_MORL_EU_ablation = np.load(file_name)
            DG_MORL_EUs_ablation.append(DG_MORL_EU_ablation)

x = np.arange(1, len(DG_MORL_EUs[0]) + 1)
if metric == "EU":
    y_DG = np.mean(DG_MORL_EUs, axis=0)
    max_DG = np.max(DG_MORL_EUs, axis=0)
    min_DG = np.min(DG_MORL_EUs, axis=0)

    y_PD = np.mean(GPI_PD_EUs, axis=0)
    max_PD = np.max(GPI_PD_EUs, axis=0)
    min_PD = np.min(GPI_PD_EUs, axis=0)

    y_LS = np.mean(GPI_LS_EUs, axis=0)
    max_LS = np.max(GPI_LS_EUs, axis=0)
    min_LS = np.min(GPI_LS_EUs, axis=0)

    plt.plot(x, y_DG, label='DG-MORL (ours)', color='red', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG, min_DG, color='red', alpha=0.3)

    plt.plot(x, y_PD, label='GPI-PD+GPI_LS', color='blue', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_PD, min_PD, color='blue', alpha=0.3)

    plt.plot(x, y_LS, label='GPI-LS', color='green', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_LS, min_LS, color='green', alpha=0.3)

if metric == "ablation":
    y_DG = np.mean(DG_MORL_EUs, axis=0)
    max_DG = np.max(DG_MORL_EUs, axis=0)
    min_DG = np.min(DG_MORL_EUs, axis=0)

    y_DG_ablation = np.mean(DG_MORL_EUs_ablation, axis=0)
    max_DG_ablation = np.max(DG_MORL_EUs_ablation, axis=0)
    min_DG_ablation = np.min(DG_MORL_EUs_ablation, axis=0)

    y_PD = np.mean(GPI_PD_EUs, axis=0)
    max_PD = np.max(GPI_PD_EUs, axis=0)
    min_PD = np.min(GPI_PD_EUs, axis=0)

    plt.plot(x, y_DG, label='DG-MORL', color='red', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG, min_DG, color='red', alpha=0.3)

    plt.plot(x, y_DG_ablation, label='DG-MORL (no self-evolving)', color='green', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_ablation, min_DG_ablation, color='green', alpha=0.3)

    plt.plot(x, y_PD, label='GPI-PD+GPI-LS', color='blue', linewidth=2, marker="o", markersize=4, linestyle='--')
    plt.fill_between(x, max_PD, min_PD, color='blue', alpha=0.3)

if metric == "Demo_num_estimation":
    color_map = plt.cm.get_cmap('viridis', len(demo_nums))
    for i in range(len(demo_nums)):
        if demo_nums[i] == 42:
            plt.plot(x, DG_MORL_EUs[i], label="GPI-PD+GPI-LS", color="blue", linewidth=2, marker="o", markersize=4,
                     linestyle='--')
        else:
            plt.plot(x, DG_MORL_EUs[i], label=f'DG-MORL {demo_nums[i]} demonstrations',
                     color=color_map(i / len(demo_nums)),
                     linewidth=2, marker="o", markersize=4)

if metric == "Roll_back_span_estimation":
    REFS = []
    REFS.append(np.load("Algorithm/Result/GPI_PD/Minecart/EU/_2.npy"))
    REFS.append(np.load("Algorithm/Result/GPI_PD/Minecart/EU/_7.npy"))
    REFS.append(np.load("Algorithm/Result/GPI_PD/Minecart/EU/_15.npy"))
    REFS.append(np.load("Algorithm/Result/GPI_PD/Minecart/EU/_42.npy"))
    REFS.append(np.load("Algorithm/Result/GPI_PD/Minecart/EU/_78.npy"))
    y_PD = np.mean(REFS, axis=0)
    color_map = plt.cm.get_cmap('viridis', len(spans))
    for i in range(len(spans)):
        if spans[i] == 42:
            plt.plot(x, y_PD, label="GPI-PD+GPI-LS", color="blue", linewidth=2, marker="o", markersize=4,
                     linestyle='--')
        else:
            plt.plot(x, DG_MORL_EUs[i], label=f'DG-MORL {spans[i]} roll back steps',
                     color=color_map(i / len(spans)),
                     linewidth=2, marker="o", markersize=4)
    plt.axhline(y=0.21, color='black', linestyle='--', label='Initial Demonstration')
    # plt.axhline(y=190.953561, color='black', linestyle='--', label='Initial Demonstration')

    # plt.fill_between(x, max_DG, min_DG, color='red', alpha=0.3)

if metric == "quality":
    y_DG_0 = np.mean(DG_MORL_EUs_0, axis=0)
    max_DG_0 = np.max(DG_MORL_EUs_0, axis=0)
    min_DG_0 = np.min(DG_MORL_EUs_0, axis=0)

    y_DG_1 = np.mean(DG_MORL_EUs_1, axis=0)
    max_DG_1 = np.max(DG_MORL_EUs_1, axis=0)
    min_DG_1 = np.min(DG_MORL_EUs_1, axis=0)

    y_DG_2 = np.mean(DG_MORL_EUs_2, axis=0)
    max_DG_2 = np.max(DG_MORL_EUs_2, axis=0)
    min_DG_2 = np.min(DG_MORL_EUs_2, axis=0)

    y_PD = np.mean(GPI_PD_EUs, axis=0)
    max_PD = np.max(GPI_PD_EUs, axis=0)
    min_PD = np.min(GPI_PD_EUs, axis=0)

    plt.plot(x, y_DG_0, label='DG-MORL good demo', color='red', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_0, min_DG_0, color='red', alpha=0.3)
    plt.axhline(y=207, color='red', linestyle='--', label='Initial Demonstration (good)')

    plt.plot(x, y_DG_1, label='DG-MORL medium demo', color='orange', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_1, min_DG_1, color='orange', alpha=0.3)
    plt.axhline(y=190.953561, color='orange', linestyle='--', label='Initial Demonstration (medium)')

    plt.plot(x, y_DG_2, label='DG-MORL bad demo', color='green', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_2, min_DG_2, color='green', alpha=0.3)
    plt.axhline(y=165.3320053, color='green', linestyle='--', label='Initial Demonstration (bad)')

    plt.plot(x, y_PD, label='GPI-PD+GPI-LS', color='blue', linewidth=2, marker="o", markersize=4, linestyle='--')
    plt.fill_between(x, max_PD, min_PD, color='blue', alpha=0.3)

if metric == "threshold":
    y_DG_0 = np.mean(DG_MORL_EUs_0, axis=0)
    max_DG_0 = np.max(DG_MORL_EUs_0, axis=0)
    min_DG_0 = np.min(DG_MORL_EUs_0, axis=0)

    y_DG_1 = np.mean(DG_MORL_EUs_1, axis=0)
    max_DG_1 = np.max(DG_MORL_EUs_1, axis=0)
    min_DG_1 = np.min(DG_MORL_EUs_1, axis=0)

    y_DG_2 = np.mean(DG_MORL_EUs_2, axis=0)
    max_DG_2 = np.max(DG_MORL_EUs_2, axis=0)
    min_DG_2 = np.min(DG_MORL_EUs_2, axis=0)

    y_PD = np.mean(GPI_PD_EUs, axis=0)
    max_PD = np.max(GPI_PD_EUs, axis=0)
    min_PD = np.min(GPI_PD_EUs, axis=0)

    plt.plot(x, y_DG_0, label='DG-MORL threshold 0.8->0.98', color='red', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_0, min_DG_0, color='red', alpha=0.3)
    # plt.axhline(y=207, color='red', linestyle='--', label='Initial Demonstration (good)')

    plt.plot(x, y_DG_1, label='DG-MORL threshold 0.9->0.98', color='green', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_1, min_DG_1, color='green', alpha=0.3)

    plt.plot(x, y_DG_2, label='DG-MORL threshold 1', color='orange', linewidth=2, marker="o", markersize=4)
    plt.fill_between(x, max_DG_2, min_DG_2, color='orange', alpha=0.3)
    # plt.axhline(y=165.3320053, color='green', linestyle='--', label='Initial Demonstration (bad)')

    plt.plot(x, y_PD, label='GPI-PD+GPI-LS', color='blue', linewidth=2, marker="o", markersize=4, linestyle='--')
    plt.fill_between(x, max_PD, min_PD, color='blue', alpha=0.3)

    plt.axhline(y=190.95356095771, color='black', linestyle='--', label='Initial Demonstration')

plt.title('Expected Utility of ' + env_name + " (" + postfix + ")")
# plt.title('Expected Utility of ' + env_name)
plt.xlabel('Time Step * ' + time_steps)
plt.ylabel('Expected Utility')
# plt.axhline(y=190.95356095771, color='black', linestyle='--', label='Prior Demonstration')
plt.xticks(x)
# plt.ylim(4.4, 5.6)
# plt.ylim(80, 230)
plt.legend(loc="lower right")
plt.grid(True)
plt.show()
