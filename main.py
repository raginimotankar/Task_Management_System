from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task
#Create a task
task1=create_task("Complete Your Assignment","Finish TASK MANAGEMENT SYSTEM")
#Display the task
print("Task1:",task1)
#Edit the task
edit_task(task1,new_title="Updated Assignment",new_description="Review and submit to Rashmi mam")
#Display the updated task
print("Updated Task1:",task1)
#Categorize the task
categorize_task(task1,"Zappkode Academy")
#Display the categorize task
print("Categorize Task1;",task1) 