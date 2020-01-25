def extract(nums, index):
    beginningValue = nums[index]
    resultString = ''

    # if true, the last value is not consecutive with the previous values
    if index == len(nums) - 1:
        return resultString + '{0}'.format(nums[index])

    while index < len(nums) - 1 and nums[index] == nums[index + 1] - 1:
        index += 1

    endValue = nums[index]

    if endValue - beginningValue >= 2:
        resultString += '{0}-{1}'.format(beginningValue, endValue)
    else:
        resultString += '{0},{1}'.format(beginningValue, endValue)

    # if true, your last element is consecutive with the others 
    # short-circuit; no more to do here
    if index == len(nums) - 1:
        return resultString

    # increment the index and pick up range-extraction from that point
    resultString += ',{}'.format(extract(nums, index + 1))
    
    return resultString

def extractRange(nums, index = 0):
    numsSet = set(nums)
    uniqueList = list(numsSet)
    uniqueList.sort()
    return extract(uniqueList, index)