import pytest
import student


@pytest.mark.parametrize('child_count', [1, 2, 5, 10, 14, 19, 200])
@pytest.mark.parametrize('candy_count', [0, 1, 3, 5, 17, 23, 29, 51, 99, 131, 292, 1000])
def test_candy_per_child(child_count, candy_count):
    actual = student.leftover_candy(candy_count=candy_count, child_count=child_count)

    assert (candy_count // child_count) * child_count + actual == candy_count
