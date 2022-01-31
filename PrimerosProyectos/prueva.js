function stringPermutations(str){
    var array = getPermutations(str);
    array = removeDuplicates(array);
    return array.sort();
}

function getPermutations(str){
    var permutatios = [],
        nextWord = [],
        chats = [];

    if (typeof str ==='string')chars = str.split('');
    else if (typeof str === 'number'){
        str = str + "";
        chars = str.split('');
    } 
    permutate(chars);
    
    return permutatios;

    function permutate(chars){
        if (chars.length === 0)permutatios.push(nextWord.join(''));
        for(var i=0; i< chars.length; i++){
            chars.push(chars.shift());
            nextWord.push(chars[0]);
            permutate(chars.slice(1));
            nextWord.pop();
        }
    }
}

removeDuplicates = array => array.filter((item, index)=>array.indexOf(item) == index)

s = "CBA"

console.log(stringPermutations(s));
