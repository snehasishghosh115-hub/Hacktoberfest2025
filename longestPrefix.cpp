class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        int size = strs.size();
        string prefix=strs[0];
    
        for(int i=1;i<size;i++)
        {
            string current=strs[i];
            string temp = "";
            for (int j =0; j<min(prefix.size(), current.size()); j++)
            {
                if(prefix[j]==current[j])
                {
                    temp+=current[j];
                }
                else
                {
                    break;
                }


            }
           prefix=temp;
           if(prefix.empty()) return "";
        }
return prefix;
    }
};
