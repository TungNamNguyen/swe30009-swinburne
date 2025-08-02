import os
folder_path = r"C:\Desktop\SWE30009\SUT\MUTANTS"
os.makedirs(folder_path, exist_ok=True)
for n in range(1, 31):
    file_name = f"kth_largest_element_mutant_{n}.py"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        pass
folder_path
