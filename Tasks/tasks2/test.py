def file_names(file_names):
    max_len = len(max(file_names, key=len))
    return [delete_dublicate(i).ljust(max_len, "_") for i in
            file_names]


def delete_dublicate(text):
    result = []
    s = set()
    for t in text:
        if t not in s:
            result.append(t)
            s.add(t)

    return "".join(result)


