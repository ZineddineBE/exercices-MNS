function fizzbuzz(n){
    const array = [];
    for (let i = 1; i<n+1; i++){
        if(i%3 == 0 && i%5 == 0){
            array.push("FizzBuzz");
        }else if (i%5 == 0){
            array.push("Buzz");
        }else if (i%3 == 0){
            array.push("Fizz");
        }else{
            array.push(i);
        }
    }
    return array;
}

console.log(fizzbuzz(25));