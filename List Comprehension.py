# List comprehension

# Verion One

My_name = ['Muhamad', 'Mulki', 'Armansyah']
del My_name[0]
print(My_name)

My_name = ['Muhamad', 'Mulki', 'Armansyah']
del My_name[:]
print(My_name)

My_name = ['Muhamad', 'Mulki', 'Armansyah']
del My_name[0:2]
print(My_name)

My_name = ['Muhamad', 'Mulki', 'Armansyah']
del My_name[0::2]
print(My_name)

# Version Two

My_name = ['Muhamad', 'Mulki', 'Armansyah']
My_name_new = My_name[0:1]
print(My_name_new)

My_name = ['Muhamad', 'Mulki', 'Armansyah']
print(My_name[0::2])
