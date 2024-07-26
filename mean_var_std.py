import numpy as np

def calculate(list):

    # try method to reshape input list into 3x3 numpy array
    try:
        array = np.array(list).reshape(3, 3)
    except:
        raise ValueError("List needs to caontain 9 numbeers")

    # Getting Axis1 Stats
    ax1_mean = array.mean(axis=0)
    ax1_var = array.var(axis=0)
    ax1_dev = array.std(axis=0)
    ax1_max = array.max(axis=0)
    ax1_min = array.min(axis=0)
    ax1_sum = array.sum(axis=0)


    # Getting Axis2 Stats
    ax2_mean = array.mean(axis=1)
    ax2_var = array.var(axis=1)
    ax2_dev = array.std(axis=1)
    ax2_max = array.max(axis=1)
    ax2_min = array.min(axis=1)
    ax2_sum = array.sum(axis=1)

    # Getting flasttened Stats
    fl_mean = array.mean()
    fl_var = array.var()
    fl_dev = array.std()
    fl_max = array.max()
    fl_min = array.min()
    fl_sum = array.sum()

  # Producing the statistics in an empty list
    mean = [ax1_mean, ax2_mean, fl_mean]
    var = [ax1_var, ax2_var, fl_var]
    std_dev = [ax1_dev, ax2_dev, fl_dev]
    max = [ax1_max, ax2_max, fl_max]
    min = [ax1_min, ax2_min, fl_min]
    sum = [ax1_sum, ax2_sum, fl_sum]
    
    

    # Displaying the statistics

    calculations = {
        'Mean' : mean,
        'Variance' : var,
        'Standard Deviation' : std_dev,
        'Max' : max,
        'Min' : min,
        'Sum' : sum
    }
    
    return calculations

calculate([0,1,2,3,4,5,6,7,8])


