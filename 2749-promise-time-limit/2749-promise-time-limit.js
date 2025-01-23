/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    // Purpose: ensures fn completes within a given time limit `t`
    // If the function `fn` takes longer than `t`, 
    // it will reject with the message "Time Limit Exceeded". 
    // Otherwise, it resolves with the result of `fn`.
    
    return async function(...args) {
        // Create a new Promise to handle the function execution with time limit
        return new Promise ((resolve, reject) =>{
            // Set a timeout that will reject the promise if time limit is exceeded
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
            
            fn(...args).then(result => {
                // If `fn` resolves successfully, clear the timeout and return the result
                clearTimeout(timer);  
                resolve(result);  
            }).catch(err => {
                // If `fn` fails, clear the timeout and propagate the error
                clearTimeout(timer); 
                reject(err);  
            });
        });
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */