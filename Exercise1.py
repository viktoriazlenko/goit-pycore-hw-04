#The function reads a file with employee names and their salaries, calculates the total salary and the average salary, and returns both values.

def total_salary(path): #path - it's the path to the file with salaries
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]

            salaries_dict = {} #dictionary to store employee names and their salaries
            for line in lines:
                name, salary = line.split(',')
                salaries_dict[name] = int(salary)

            calculated_salary = 0 #variable to store the total salary
            for name, salary in salaries_dict.items():
                calculated_salary += salary 
            
            salary_average = int(calculated_salary / len(salaries_dict)) #variable to store the average salary, calculated by dividing the total salary by the number of employees

        return calculated_salary, salary_average
    except FileNotFoundError:
        print(f"File {path} not found.")
    except ValueError:
        print(f"File {path} contains invalid data.")
    except Exception as e:
        print(f"An error occurred: {e}")
    

print(f"Total salary: {total_salary('salaries.txt')[0]}, Average salary: {total_salary('salaries.txt')[1]}")

