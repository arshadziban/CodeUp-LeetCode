function cancellable(fn, args, t) {
    // Set the timeout to call the function after t milliseconds
    const timeoutId = setTimeout(() => {
        fn(...args);
    }, t);

    // Return a cancel function that clears the timeout
    return function cancelFn() {
        clearTimeout(timeoutId);
    };
}
