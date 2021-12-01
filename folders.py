import os.path

#print(__file__)
#python_folder = os.path.dirname(__file__)
python_folder = 'C:/Temp'
print(python_folder)

sum_bytes = 0
for file in os.listdir(python_folder):
    f = os.path.join(python_folder, file)
    if os.path.isfile(f):
        #print(file)
        #print(os.stat(file))
        sum_bytes += os.path.getsize(f)
        #print(os.path.getsize(file))
print('Sum space: {}'.format(sum_bytes))

# 1. Include summing space occupied for folders with their content
# Hint: use recursion...
# Step 1: create a function that iterates over files in a folder and returns the sum of the size
# Step 2: add a condition for the case of a folder - then the function should call itself for
#         the subfolder as input parameter