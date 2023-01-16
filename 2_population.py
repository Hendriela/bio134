#%% Rabbits and foxes

F = 100
R = 1000
# R = R + float(R * 0.05) - float(R * F * 0.0002)
print(int(R))

for x in range(1, 1543):
    r_new = R + R * 0.05 - R * F * 0.0002
    F = float(F - F * 0.1 + R * F * 0.0001)
    R = r_new
print(int(R))
print(int(F))

# hourly change
n_rabbit = 1000
n_fox = 100
days = 200
factor = 24 * 60
hours = days * factor


print("After", days, "days, the population sizes are:")

for i in range(0, hours):
    n_rabbit_new = n_rabbit + ((n_rabbit * 0.05) / factor) - (0.0002 * (n_fox) * (n_rabbit) / factor)
    n_fox_new = n_fox - ((n_fox * 0.1) / factor) + (0.0001 * (n_fox) * (n_rabbit)) / factor
    n_rabbit = n_rabbit_new  # setting the calculated as new base
    n_fox = n_fox_new  # setting the calculated as new base

print(int(n_rabbit), "Rabbits")
print(int(n_fox), "Foxes")

rab = 1000
for i in range(40):
    rab += rab*0.05
print(int(rab))