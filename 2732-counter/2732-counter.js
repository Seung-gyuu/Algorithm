/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        // The post-increment operator (n++) first returns the current value of n, and only after that does it increment the value of n.
       return n++
    };
};

// Closures: The inner function remembers the environment (the variables in the outer function's scope), even after the outer function has completed execution. This makes it perfect for creating things like counters, callbacks, or event handlers that maintain their own state.

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */