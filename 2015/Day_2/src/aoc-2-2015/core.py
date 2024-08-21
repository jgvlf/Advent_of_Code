def main() -> None:
    inputs: list[tuple[int, ...]] = read_lines()
    size_of_parcel: int = get_qtd_wrapping_paper(inputs, 0)
    ribbon_qtd: int = get_ribbon_qtd(inputs, 0)
    print(f"Total Wrapping Paper Size Required: {size_of_parcel}ft²;\nTotal Ribbon Required: {ribbon_qtd}ft.")


def get_qtd_wrapping_paper(inputs: list[tuple[int, ...]], init_size_of_parcel: int):
    for data in inputs:
        areas: list[int] = calculate_surface_area(data)
        size: int = wrappin_paper_size(areas)
        init_size_of_parcel += size
    return init_size_of_parcel


def get_ribbon_qtd(inputs: list[tuple[int, ...]], init_ribbon_qtd: int) -> int:
    for data in inputs:
        size: int = present_ribbon_measure(data)
        init_ribbon_qtd += size
    return init_ribbon_qtd


def present_ribbon_measure(data: tuple[int, ...]) -> int:
    minor_perimeter: int = 2 * data[0] + 2 * data[1]
    ribbon_bow_size: int = data[0] * data[1] * data[2]
    return minor_perimeter + ribbon_bow_size


def calculate_surface_area(dim: tuple[int, ...] = (2, 3, 4)) -> list[int]:
    surface_areas: list[int] = list()
    for i in range(len(dim)):
        if i < 2:
            area = dim[i] * dim[i+1]
            surface_areas.append(area)
        else:
            area = dim[i] * dim[0]
            surface_areas.append(area)
        surface_areas.sort()
    return surface_areas


def wrappin_paper_size(areas: list[int]) -> int:
    minor_side = areas[0]
    size = sum([num * 2 for num in areas]) + minor_side
    return size


def read_lines() -> list[tuple[int, ...]]:
    with open("assets/input.txt", "r") as f:
        to_numbers: list[tuple[int, ...]] = list()
        for lines in f.readlines():
            remove_special_char: str = lines.replace("\n", "")
            remove_char: list[int] = [int(num) for num in remove_special_char.split("x")]
            remove_char.sort()
            only_numbers: tuple[int, ...] = tuple([int(num) for num in remove_char])
            to_numbers.append(only_numbers)
        return to_numbers




