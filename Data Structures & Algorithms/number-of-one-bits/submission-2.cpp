class Solution {
public:
    int hammingWeight(uint32_t n) {
        int result = 0;
        for(int i = 0; i < 32; i++){
            if(n % 2 == 1){
                result += 1;
            }
            n = n >> 1;
        }
        return result;
    }
};
