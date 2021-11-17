import os
import platform
import tempfile

print(os.environ['HOMEPATH'])
print(platform.system())
print(platform.release())
print(platform.architecture())

print(os.path.expanduser('~'))
with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as my_temp_file:
    print(my_temp_file.name)
    my_temp_file.write("Bla\n")
    my_temp_file.write("abc")
    my_temp_file.close()
    print('closed')


print(os.getcwd())
print('----------------')
print(__file__)

proj_folder = os.path.dirname(__file__)
print(proj_folder)
print('----------------')

out2_file = '../data/out.txt'
print('Abs path: ' + os.path.abspath(out2_file))

out_file = os.path.join(proj_folder, 'data', 'out.txt')
print(out_file)
print(os.path.basename(out_file))
with open(out_file, 'a') as f_out:
    f_out.write('Bla\n')
    f_out.write('Abc\n')


