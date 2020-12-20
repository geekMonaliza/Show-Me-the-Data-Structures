import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if not path:
        return None

    path_contents = os.listdir(path)

    files = [path + '/' + file for file in path_contents if os.path.isfile(path + '/' + file) and file.endswith(suffix)]

    folders = [folder for folder in path_contents if not os.path.isfile(path + '/' + folder)]

    for folder in folders:
        files.extend(find_files(suffix, path + '/' + folder))

    return files

# testcase1
print(find_files('.c', 'testdir'))    # ['./testdir-nested/t1.c', './testdir-nested/subdir3/subsubdir1/b.c', './testdir-nested/subdir5/a.c', './testdir-nested/subdir1/a.c']

# testcase2
print(find_files('.py', ''))   # None

# testcase3
print(find_files('', 'testdir-nested'))     # Finds list of all files in path, as suffix is ''


print(find_files('', 'testdir-nested'))     # Finds list of all files in path, as suffix is ''
