function racineNumeriqueEntier(n){
    res = 0;
    for(let i = 0; i < n.toString().length; i++){
        res += parseInt(n.toString()[i]);
    }
    if(res.toString().length > 1){
        racineNumeriqueEntier(res);
    }
    return res;
}

console.log(racineNumeriqueEntier(123189));

