/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArr = [];
    for(i = 0 ; i < arr.length ; i ++){
        let res = fn(arr[i],i);
        if(Boolean(res)){
            filteredArr.push(arr[i]);
        }        
    }
    return filteredArr 
};