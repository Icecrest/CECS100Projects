tuition = 8000
for i in [1, 2, 3, 4, 5]:  # parse a list for years 1-5
    tuition *= 1.03  # increment tuition
    print("Tuition for year", i, "-",format(2*tuition, ".2f"))
