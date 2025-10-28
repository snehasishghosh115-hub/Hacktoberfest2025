
function printNumbers(n, current = 1) {
    if (current > n) return; 
    
    let output = '';
    if (current % 3 === 0) output += 'Fizz';
    if (current % 5 === 0) output += 'Buzz';
    if (output === '') output = current;

    console.log(output);

    printNumbers(n, current + 1); 
}


printNumbers(20);
