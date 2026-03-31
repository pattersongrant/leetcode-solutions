class FirstUnique {
public:
    FirstUnique(vector<int>& nums) {
        n = nums; 
        count = nums.size(); 
        for (int i = 0; i < nums.size(); ++i) { 
            auto it = map.find(nums[i]);
            if (it == map.end()) { 
                map.insert({nums[i], i}); 
            }
            else { 
                it->second = -1; 
            }
        }
    }
    
    int showFirstUnique() {
        for (int i = 0; i < n.size(); ++i) { 
            auto it = map.find(n[i]); 
            if (it != map.end()) {
                if (it->second != -1) { 
                    return n[i];
                }
            }
        }
        return -1;
    }
    
    void add(int value) {
        auto it = map.find(value); 
        if (it != map.end()) {
            it->second = -1;
        }
        else { 
            map.insert({value, static_cast<int>(n.size())});
        }
        n.push_back(value);

    }
private: 
    vector<int> n;
    unordered_map<int, int> map; 
    int count; 
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */