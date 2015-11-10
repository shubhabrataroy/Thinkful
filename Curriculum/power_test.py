# Source: http://stackoverflow.com/questions/15204070/is-there-a-python-scipy-function-to-determine-parameters-needed-to-obtain-a-ta
# Input: p1: metric in control group
#        p2: metric in treatment group
#        power: represents the probability that you’ll get a false negative. A power of 0.80 means that there is an 80% chance that if there was an effect, we would detect it (or a 20% chance that we’d miss the effect)
#        sig: statistical significance of the test
# Output: Required sample size

from scipy.stats import norm

def sample_power_probtest(p1, p2, power=0.8, sig=0.05):
    z = norm.isf([sig/2]) #two-sided t test
    zp = -1 * norm.isf([power]) 
    d = (p1-p2)
    s =2*((p1+p2) /2)*(1-((p1+p2) /2))
    n = s * ((zp + z)**2) / (d**2)
    return int(round(n[0]))

if __name__ == '__main__':

    n = sample_power_probtest(0.50, 0.75, power=0.9, sig=0.05)
    print n  #14752