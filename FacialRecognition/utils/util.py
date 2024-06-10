def read_securityList(securityList_path):
    security_list = open(securityList_path, "r").read().split("\n")
    security_dict = {}
    for line in security_list:
        line = line.split(",")
        if len(line) == 2:
            if line[0] == "black":
                security_dict[line[1]] = "black"
            elif line[0] == "white":
                security_dict[line[1]] = "white"
    return security_dict