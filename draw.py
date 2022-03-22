import os
import matplotlib.pyplot as plt
import re

def generate_stats_from_log(experiment_name='/home/lk3696/yi_plot/loss_log.txt', line_interval=10, nb_data=950, enforce_last_line=True):
    """
    Generate chart with all losses from log file generated by CycleGAN/Pix2pix/CUT framework
    """
    #extract every lines
    with open(os.path.join(experiment_name, "loss_log.txt"), 'r') as f:
        lines = f.readlines()
    #choose the lines to use for plotting
    lines_for_plot = []
    for i in range(1,len(lines)):
        if (i-1) % line_interval==0:
            lines_for_plot.append(lines[i])
    if enforce_last_line:
        lines_for_plot.append(lines[-1])
    #initialize dict with loss names
    dicts = dict()
    dicts["epoch"] = []
    parts = (lines_for_plot[0]).split(') ')[1].split(' ')
    for i in range(0, len(parts)//2):
        dicts[parts[2*i][:-1]] = []
    #extract all data
    pattern = "epoch: ([0-9]+), iters: ([0-9]+)"
    for l in lines_for_plot:
        search = re.search(pattern, l)
        epoch = int(search.group(1))
        epoch_floatpart = int(search.group(2))/nb_data
        dicts["epoch"].append(epoch+epoch_floatpart) #to allow several plots for the same epoch
        parts = l.split(') ')[1].split(' ')
        for i in range(0, len(parts)//2):
            dicts[parts[2*i][:-1]].append(float(parts[2*i+1]))
    #plot everything
    plt.figure()
    for key in dicts.keys():
        if key != "epoch":
            plt.plot(dicts["epoch"], dicts[key], label=key)
    plt.legend(loc="best")
    plt.show()