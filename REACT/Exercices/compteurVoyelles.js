function compterVoyelles(string){
    cpt = 0;
    for(let i = 0; i < string.length; i++){
        if(string[i] === 'a' || string[i] === 'e' || string[i] === 'i' || string[i] === 'o' || string[i] === 'u' || string[i] === 'y'){
            cpt++;
        }
    }
    return cpt;
}

console.log(compterVoyelles("zineddine"));