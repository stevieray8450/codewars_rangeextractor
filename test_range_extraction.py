from range_extraction import extractRange

def test_extractRange_all_consecutive_zero_start():
    assert extractRange([0, 1, 2]) == '0-2'

def test_extractRange_all_consecutive_duplicates():
    assert extractRange([1, 1, 2, 2, 2, 4, 5]) == '1,2,4,5'

def test_extractRange_all_consecutive_positive_start():
    assert extractRange([1, 2, 3]) == '1-3'

def test_extractRange_all_consecutive_small_range():
    assert extractRange([1, 2, 5, 6, 8, 9]) == '1,2,5,6,8,9'

def test_extractRange_non_consecutive_positive_end():
    assert extractRange([1, 2, 3, 7]) == '1-3,7'

def test_extractRange_all_consecutive_negative_start():
    assert extractRange([-3, -2, -1, 0]) == '-3-0'

def test_extractRange_broken_range_all_positive():
    assert extractRange([3, 4, 5, 7, 8]) == '3-5,7,8'

def test_extractRange_broken_range_all_negative():
    assert extractRange([-26, -25, -24, -20, -19, -17, -16]) == '-26--24,-20,-19,-17,-16'

def test_extractRange_broken_range_cross_zero():
    assert extractRange([-3, -2, -1, 0, 1, 3, 4, 5]) == '-3-1,3-5'

def test_extractRange_broken_range_cross_non_consecutive_end():
    assert extractRange([-2, -1, 0, 1, 3, 4, 6]) == '-2-1,3,4,6'

def test_extractRange_broken_range_cross_big_gap_end():
    assert extractRange([-35, -34, -33, 20, 21, 30, 31, 32, 33, 34, 50]) == '-35--33,20,21,30-34,50'

def test_extractRange_codewars_sampletest():
    assert extractRange([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
