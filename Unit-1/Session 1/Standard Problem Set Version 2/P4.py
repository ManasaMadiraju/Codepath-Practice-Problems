def get_last(items):
    for i in items:
        if not items:
            return None
        return items[-1]
    

if __name__ == '__main__':
    items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
    print(get_last(items))

    items = []
    print(get_last(items))
