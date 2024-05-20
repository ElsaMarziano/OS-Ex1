# OS 24 EX1
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\user\Documents\\university\\OS\\ex01\\results.csv", header=None, names=["Index", "Column1", "Column2"])
data = data.to_numpy()

l1_size = 32 * 1024
l2_size = 256 * 1024
l3_size = 6 * 1024 * 1024

plt.plot(data[:, 0], data[:, 1], label="Random access")
plt.plot(data[:, 0], data[:, 2], label="Sequential access")
plt.xscale('log')
plt.yscale('log')
plt.axvline(x=l1_size, label=f"L1 ({l1_size} bytes)", c='r')
plt.axvline(x=l2_size, label=f"L2 ({l2_size} bytes)", c='g')
plt.axvline(x=l3_size, label=f"L3 ({l3_size} bytes)", c='brown')
plt.legend()
plt.title("Latency as a function of array size \n with CPU Model: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz")
plt.ylabel("Latency (ns log scale)")
plt.xlabel("Bytes allocated (log scale)")
plt.show()
