# musicanalysis
1st-Order Markov Chain.maxpat was used for the purposes of analyzing pitch proximity and step declination, and generated matrixes of interval sizes and frequencies. 

2nd-Order Markov Chain.maxpat was used to analyze step inertia and post-skip reversal by generating matrixes of second-order pitch frequencies.

Pitch List.maxpat tracked every pitch played within the melody and output those results into a list.

music_analysis.py contained five different functions for each principle, which all received these matrixes as input and manipulated them accordingly to provide counts. 
