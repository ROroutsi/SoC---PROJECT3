import BDMapper

mapped = BDMapper.mapper()


def reducer(mapped):
    reduced = {}

    for line in mapped:

        position, result = line.strip().split(',')

        try:
            reduced.get(position)[result] += 1
        except TypeError:
            reduced[position] = {'P': 1, 'N': 0}
    '''
    with open('BDResults.csv', 'w') as f:
        f.write("position,count_positive,count_negative\n")

        for key, values in reduced.items():
            f.write(f"{key}")
            for result, result_count in values.items():
                f.write(f",{result_count}")
            f.write("\n")
	'''
    print(reduced)


reducer(mapped)
