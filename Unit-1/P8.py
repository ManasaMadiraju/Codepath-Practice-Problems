def print_todo_list(task):
    count = 0
    print("Pooh's To Dos:")
    for i in task:
        count+=1
        print(f"{count}. {i}")
    print("\n")

if __name__ == '__main__':
    task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(task)

    task = []
    print_todo_list(task)