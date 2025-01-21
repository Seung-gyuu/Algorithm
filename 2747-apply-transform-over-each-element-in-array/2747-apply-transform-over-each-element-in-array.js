/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let return_arr = []
    for(i = 0 ; i <= arr.length - 1 ; i ++){
        return_arr[i] = fn(arr[i], i)
    }

    return return_arr
    
};