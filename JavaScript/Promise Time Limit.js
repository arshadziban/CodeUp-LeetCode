/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
function timeLimit(fn, t) {
    return async function (...args) {
        return new Promise((resolve, reject) => {
            // Set timeout to reject after t milliseconds
            const timeoutId = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);

            // Call the original function
            fn(...args)
                .then((res) => {
                    clearTimeout(timeoutId); // Cancel timeout
                    resolve(res);
                })
                .catch((err) => {
                    clearTimeout(timeoutId); // Cancel timeout
                    reject(err);
                });
        });
    };
}

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */