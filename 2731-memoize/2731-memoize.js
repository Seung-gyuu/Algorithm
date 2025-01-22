/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    // Cache to store val of function calls 
    const cache = {};
    let callCount = 0;

    // Memoized function to check if the result is already cached
    function memoizedFunction(...args) {
        // Convert arguments to a string 
        const key = JSON.stringify(args);
        // If this combination of arguments hasn't been called before, calculate and cache the result
        if (!(key in cache)){
            callCount++; // Increment call count 
            // Save the result of the function call for this combination of arguments
            cache[key] = fn(...args);
        }
        return cache[key];
    }
    
    memoizedFunction.getCallCount = function() {
        return callCount;
    };
    return memoizedFunction;
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */