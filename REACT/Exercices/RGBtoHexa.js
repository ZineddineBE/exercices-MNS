function RGBtoHexa(r,g,b){
    if (r == 0){
        rHex = "00";
    } else if(r > 255){
        rHex = "FF"
    } else{
        rHex = r.toString(16);
    }

    if (g == 0){
        gHex = "00";
    } else if(g > 255){
        gHex = "FF"
    } else{
        gHex = g.toString(16);
    }

    if (b == 0){
        bHex = "00";
    } else if(b > 255){
        bHex = "FF"
    } else{
        bHex = b.toString(16);
    }

    const hexa = (rHex + gHex + bHex).toUpperCase();
    return hexa
}

console.log(RGBtoHexa(255, 255, 300));