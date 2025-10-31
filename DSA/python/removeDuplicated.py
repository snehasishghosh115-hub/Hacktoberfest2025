int removeDuplicates(int* nums, int numsSize){
    int var,index=0;
    for(int i=0; i<numsSize; i++)
    { 
        if(var!=nums[i])
        {
          var=nums[i];
          nums[index]=var;
          printf("%d ",var);
          index++;
        }
       
    }
   
  return index;
}
