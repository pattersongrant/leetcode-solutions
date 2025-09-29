class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        
        var indices: [Int: Int] = [:] //nums[i] : i
        
      
        for i in 0..<nums.count {
            if let j = indices[target - nums[i]] {
                return [j, i]
            }
            indices[nums[i]] = i
        }



        return [-1]
    }
}