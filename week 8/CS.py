import pandas as pd
import matplotlib.pyplot as plt
data = {"temperature": [23, 23, 21, 20, 19, 15, 12, 23,
                        25, 30], "movement": [1, 0, 1, 1, 1, 1, 0, 0, 1, 1]}
df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(df['temperature'], marker='o', label='Temperature')
plt.ylabel('Temperature')
plt.title('Temperature and Movement over Time')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df['movement'], marker='o', label='Movement')
plt.xlabel('Time (index)')
plt.ylabel('Movement')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
