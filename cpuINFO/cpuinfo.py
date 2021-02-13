import psutil

print("Núcleos físicos", psutil.cpu_count(logical=False))
print("Núcleos totales", psutil.cpu_count(logical=True))

cpufreq = psutil.cpu_freq()
print(f"Máxima frequencia: {cpufreq.max:.2f}Mhz")
print(f"Mínima frequencia: {cpufreq.min:.2f}Mhz")
print(f"Frequencia actual: {cpufreq.current:.2f}Mhz")

print("CPU usado por núcleo:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
	print(f"Núcleo {i}: {percentage}%")
print(f"Total % de núcleos usados: {psutil.cpu_percent()}%")