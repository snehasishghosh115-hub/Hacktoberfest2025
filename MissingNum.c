int missingNumber(int* nums, int numsSize) {
    int result= numsSize;
    for(int i=0; i<numsSize ; i++)
    {
        result = result + i - nums[i];

    }
    return result ;
}
