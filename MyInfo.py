import os.path

while True:
    save_path = input("Enter the directory to save a file")
    if os.path.exists(save_path):
        break
    else: # dir does not exist
        print('That directory does not exist, please try again')

file = input("What is the name of the file?")
exact_file = file + ".txt"
full_path = os.path.join(save_path, exact_file)
print('will use:', full_path)

f = open(full_path, "w+")
name = input("Please enter your name: ")
addr = input("Enter your address")
ph = input("Enter your phone number")
line = name + ',' + addr + ',' + ph + '\n'
f.write(line)
print('wrote to', full_path)
f.close()
f = open(full_path)
print(f.read())
f.close()