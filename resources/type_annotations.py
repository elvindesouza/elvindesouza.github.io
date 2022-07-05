"""
Simple demonstration of type hinting, and using mypy.

Elvin deSouza
"""


def filter_integers(list_ints: list[int]) -> list[int] | None:
    """
    takes a list of integers and returns a subset list of integers
    where values are greater than 5
    if there are no values greater than 5, returns NoneType
    """
    list_ret: list[int] = []
    for i in list_ints:
        if i > 5:  # arbitrary condition
            list_ret.append(i)
    if len(list_ret) == 0:
        return None
    return list_ret


if __name__ == "__main__":
    input_list: list[int] = [1, 2, 3, 4, 5, 6]
    filtered = filter_integers(input_list)
    for i in filtered:
        print(
            i
        )  # mypy will catch the issue here! filtered can be list[int] or NoneType!
