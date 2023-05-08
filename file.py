import secret


def find_user_watch(user_id):
    """find user data"""
    output_data = ""
    with open(secret.watch_file_path, "r") as f:
        for line in f:
            if (str(user_id) + "$") in line:
                output_data = line.replace("\n", "")
        f.close()
    if not output_data:
        return False
    return (output_data.split("$")[1]).split(",")


def add_user_watch(data):
    """add new user"""
    data_write = str(data.pop(0)) + "$" + ",".join(data) + "\n"
    with open(secret.watch_file_path, "a") as f:
        f.write(data_write)
        f.close()


def update_user_watch(data):
    """update user data"""
    all_data = []
    with open(secret.watch_file_path, "r") as f:
        for line in f:
            if line.find(str(data[0]) + "$") == -1:
                all_data.append(line.replace("\n", ""))
        f.close()
    all_data.append(data.pop(0) + "$" + ",".join(data))
    with open(secret.watch_file_path, "w") as f:
        f.write("\n".join(all_data))
        f.close()
