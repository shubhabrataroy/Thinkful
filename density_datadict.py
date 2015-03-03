import collections
population_dict = collections.defaultdict(int)
area_dict = collections.defaultdict(int)
density_dict = collections.defaultdict(int)

with open('/home/sroy/Desktop/Thinkful/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[7] = int(line[7])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]
            area_dict[line[0]] += line[7]
for j in range(len(population_dict.keys())):
    density_dict.update({population_dict.keys()[j]:float(population_dict[population_dict.keys()[j]]/area_dict[population_dict.keys()[j]])})
