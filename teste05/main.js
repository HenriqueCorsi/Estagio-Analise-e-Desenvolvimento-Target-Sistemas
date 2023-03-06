var user_input = 'vermelho';

function invert_word(word){
   var result = "";
   for(index = word.length - 1; index  >= 0; index--){
        result += word[index];
   }
   return result
}

console.log(`A palavra ${user_input} invertida fica ${invert_word(user_input)}`);

