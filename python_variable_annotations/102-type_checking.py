from typing import List, Tuple, TypeVar

T = TypeVar('T')  # Generic type variable

def zoom_array(lst: Tuple[T, ...], factor: int = 2) -> Tuple[T, ...]:
    zoomed_in: List[T] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)

array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)  # Changed from 3.0 to 3 (int)
