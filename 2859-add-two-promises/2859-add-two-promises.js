/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  // Wait for the first promise to resolve and store the result in `value1`
  const value1 = await promise1;
  
  // Wait for the second promise to resolve and store the result in `value2`
  const value2 = await promise2; 

  return value1 + value2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */