function memoize(fn) {
    const cache = new Map();
    let callCount = 0;

    const memoizedFn = (...args) => {
        const key = JSON.stringify(args); // Unique key per argument set
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        callCount++;
        return result;
    };

    memoizedFn.getCallCount = () => callCount;
    return memoizedFn;
}

// Core functions
const sum = (a, b) => a + b;
const factorial = (n) => n <= 1 ? 1 : n * factorial(n - 1);
const fib = (n) => n <= 1 ? 1 : fib(n - 1) + fib(n - 2);

// Main executor
function runActions(fnName, actions, values) {
    let fn;
    if (fnName === "sum") fn = sum;
    else if (fnName === "factorial") fn = factorial;
    else if (fnName === "fib") fn = fib;

    const memoizedFn = memoize(fn);
    const result = [];

    for (let i = 0; i < actions.length; i++) {
        if (actions[i] === "call") {
            result.push(memoizedFn(...values[i]));
        } else if (actions[i] === "getCallCount") {
            result.push(memoizedFn.getCallCount());
        }
    }

    return result;
}