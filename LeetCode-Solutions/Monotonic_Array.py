def monotonic(nums: list[int]) -> bool:
    return (nums == sorted(nums) or nums == sorted(nums,reverse=True))


print(monotonic([1,2,2,3]))
print(monotonic([6,5,4,4]))
print(monotonic([1,3,2]))
        
