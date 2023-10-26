const fibonacci = (n) => {
  if (n <= 0) {
    return 0;
  } else if (n === 1) {
    return 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
};
const n = 10;
console.log(`Fibonacci(${n}) = ${fibonacci(n)}`);
