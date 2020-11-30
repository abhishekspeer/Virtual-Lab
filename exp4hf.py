import random

# Standardization of NaOH solution:
def standardiseNaoH():
    """
    Taking 0.25N 10 ml oxalic acid.
    Using N1V1 = (.25)(10ml) = N2V2, with random V2 == float(10,30)
    """
    volume_oxalic = 10.00
    normality_oxalic = 0.25
    volume_NaOH = random.uniform(10.00,30.00)
    normality_NaOH = (volume_oxalic * normality_oxalic)/volume_NaOH # adding extra variable for context
    rounded_normality_NaOH = round(normality_NaOH,2)
    print("Normality of Standardized NaOH is: " + str(rounded_normality_NaOH))
    
    return rounded_normality_NaOH


# Titration of the weak acid(acetic acid) using the standardized NaOH solution
def titrationWeakAcid():
    """
    Taking 25 ml oxalic acid with pKa 1.23 and N == float(.10,2.00)
    standardiseNaoh() for normality
    """
    pKa_weakAcid = 1.23 
    volume_weakAcid = 25.00
    normality_weakAcid = random.uniform(0.10, 2.00)
    normality_NaOH = standardiseNaoH()
    volume_NaOH = (volume_weakAcid*normality_weakAcid)/normality_NaOH
    rounded_volume_NaOH = round(volume_NaOH,2)
    print("Volume of NaOH thus obtained against weak acid is: " + str(rounded_volume_NaOH))
    
    return rounded_volume_NaOH

# Driver
"""
Note: call the functions multiple times for multiple trials
"""

titrationWeakAcid() 



