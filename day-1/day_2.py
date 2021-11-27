import numpy as np

# import expenses file into a numpy array
expenses = np.fromfile('expense_report.csv', dtype=np.intc, sep='\n')

# self-explanatory
exitFlag = False
for i in range(0, len(expenses)):
    for j in range(i+1, len(expenses)):
        for k in range(i+2, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print('Entry #1 :', expenses[i], 'Entry #2 :',
                      expenses[j], 'Entry #3 :', expenses[k])
                print('product :', expenses[i]*expenses[j]*expenses[k])
                exitFlag = True
                break
        if exitFlag:
            break
    if exitFlag:
        break
