def pitch_proximity_counts(file_name):
    #takes in pitch matrix data containing first-order markov chains and
    #generates counts of the total of small intervals (0-3 semitones) and
    #the total number of intervals in general

    with open(file_name) as matrix:
        data = matrix.readlines()

    #initialize the count so the iterating loop can add to it
    small_intervals = 0; total_intervals = 0

    for i in range(len(data)):
        line = data[i]
        chain = line.split(',')
        first = int(chain[0])
        final_pitch_list = chain[1][:-2].split()

        for j in range(len(final_pitch_list)):
            if abs(int(final_pitch_list[j]) - first) in range(0, 4):
                small_intervals += 1
            total_intervals +=1

    counts = [small_intervals, total_intervals]
    return counts



def step_declination_counts(file_name):
    #takes in pitch matrix data containing first-order markov chains and
    #generates counts for small descending and large ascending intervals

    #unison intervals are excluded

    with open(file_name) as matrix:
        data = matrix.readlines()

    #initialize variables for the loop
    small_descending = 0; large_ascending = 0; small_intervals = 0;
    large_intervals = 0

    for i in range(len(data)):
        line = data[i]
        chain = line.split(',')
        first = int(chain[0])
        final_pitch_list = chain[1][:-2].split()

        for j in range(len(final_pitch_list)):
            if int(final_pitch_list[j]) - first > 0:
                if int(final_pitch_list[j]) - first > 3:
                    large_ascending += 1
                    large_intervals += 1
                elif int(final_pitch_list[j]) - first in range(1, 4):
                    small_intervals += 1
            elif int(final_pitch_list[j]) - first < 0:
                if int(final_pitch_list[j]) - first < -3:
                    large_intervals += 1
                elif int(final_pitch_list[j]) - first in range(-3, 0):
                    small_descending += 1
                    small_intervals +=1
                
    intervals = [small_descending, large_ascending, small_intervals,
                 large_intervals]
    return intervals



def step_inertia_counts(file_name):
    #takes in pitch matrix data containing second-order markov chains and
    #generates counts for the following small interval types: A -> A, D -> A,
    #A -> D, D -> D

    #unison intervals are excluded

    with open(file_name) as matrix:
        data = matrix.readlines()

    #initialize the variables so the iterating loop can add to them
    a_a = 0; d_a = 0; a_d = 0; d_d = 0

    for i in range(len(data)):
        line = data[i]
        chain = line.split(',')
        intervals = chain[0]
        first = int(intervals[:2]); last = int(intervals[2:])
        final_pitch_list = chain[1][:-2].split()

        if last - first in range(1, 4):
            for j in range(len(final_pitch_list)):
                if int(final_pitch_list[j]) - last in range(1, 4):
                    a_a += 1
                elif int(final_pitch_list[j]) - last in range(-3, 0):
                    a_d += 1
        elif last - first in range(-3, 0):
            for j in range(len(final_pitch_list)):
                if int(final_pitch_list[j]) - last in range(1, 4):
                    d_a += 1
                elif int(final_pitch_list[j]) - last in range(-3, 0):
                    d_d += 1

    counts = [a_a, d_a, a_d, d_d]
    return counts



def post_skip_counts(file_name):
    #takes in pitch matrix data containing second-order markov chains and
    #generates counts for the number of large intervals followed by intervals
    #in the opposite direction

    #unison intervals are excluded

    with open(file_name) as matrix:
        data = matrix.readlines()

    #initialize variables for the iterating loop
    a_d = 0; d_a = 0

    for i in range(len(data)):
        line = data[i]
        chain = line.split(',')
        intervals = chain[0]
        first = int(intervals[:2]); last = int(intervals[2:])
        final_pitch_list = chain[1][:-2].split()

        #separating counts based on the initial interval
        if last - first > 3:
            for j in range(len(final_pitch_list)):
                if int(final_pitch_list[j]) - last < 0:
                    a_d += 1
        elif last - first < -3:
            for j in range(len(final_pitch_list)):
                if int(final_pitch_list[j]) - last > 0:
                    d_a += 1

    interval_list = [a_d, d_a]
    return interval_list



def arch_values(file_name):
    #takes in list of pitches and generates average pitch height for successive
    #11-note phrases

    with open(file_name) as matrix:
        data = matrix.readlines()

    #initialize pitch sums for the iterating loop
    first = 0; second = 0; third = 0; fourth = 0; fifth = 0; sixth = 0;
    seventh = 0; eighth = 0; ninth = 0; tenth = 0; eleventh = 0

    #initialize actual counts for each note in the phrase
    one = 0; two = 0; three = 0; four = 0; five = 0; six = 0; seven = 0;
    eight = 0; nine = 0; ten = 0; eleven = 0;

    #cut the whole list into 11-note phrases (plus whatever remainder)
    pitch_lists = [data[0].split()[i:i + 11] for i in range(0,
                   len(data[0].split()), 11)]

    #subtract 60 (the MIDI value for middle-C) for comparison with Huron's study
    for i in range(len(pitch_lists)):
        for j in range(len(pitch_lists[i])):
            if j == 0:
                first += (int(pitch_lists[i][j]) - 60)
                one += 1
            elif j == 1:
                second += (int(pitch_lists[i][j]) - 60)
                two += 1
            elif j == 2:
                third += (int(pitch_lists[i][j]) - 60)
                three += 1
            elif j == 3:
                fourth += (int(pitch_lists[i][j]) - 60)
                four += 1
            elif j == 4:
                fifth += (int(pitch_lists[i][j]) - 60)
                five += 1
            elif j == 5:
                sixth += (int(pitch_lists[i][j]) - 60)
                six += 1
            elif j == 6:
                seventh += (int(pitch_lists[i][j]) - 60)
                seven += 1
            elif j == 7:
                eighth += (int(pitch_lists[i][j]) - 60)
                eight += 1
            elif j == 8:
                ninth += (int(pitch_lists[i][j]) - 60)
                nine += 1
            elif j == 9:
                tenth += (int(pitch_lists[i][j]) - 60)
                ten += 1
            elif j == 10:
                eleventh += (int(pitch_lists[i][j]) - 60)
                eleven += 1

    sums = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth,
            tenth, eleventh]
    counts = [one, two, three, four, five, six, seven, eight, nine, ten, eleven]

    heights = [i/j for i, j in zip(sums, counts)]
    return heights
