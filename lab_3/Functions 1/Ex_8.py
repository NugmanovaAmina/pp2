def spy_game(nums : list):
    str_version_of_nums = "".join([str(x) for x in nums])
    return False if str_version_of_nums.find("007") == -1 else True