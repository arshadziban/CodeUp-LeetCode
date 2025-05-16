function createCounter(init) {
  let current = init;

  return {
    increment: function() {
      return ++current;
    },
    decrement: function() {
      return --current;
    },
    reset: function() {
      current = init;
      return current;
    }
  };
}