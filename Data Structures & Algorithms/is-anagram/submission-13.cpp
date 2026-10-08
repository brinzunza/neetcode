class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen;
        int total = 0;

        if(s.length() != t.length()){
            return {false};
        }

        for(int i = 0; i < s.length(); i++){
            seen[s[i]] += 1;
            total += 1;
        }

        for(int i = 0; i < t.length(); i++){
            if(seen[t[i]] == 0){
                return {false};
            }
            seen[t[i]] -= 1;
            total -= 1;
        }

        if(total == 0){
            return {true};
        }

        return {false};
    }
};
