class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if(!nums){return false}
        let set = new Set(nums)
        if(set.size !=nums.length){return true}
        return false
    }
}
