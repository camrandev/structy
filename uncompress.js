//remember to solve with brute force first
//two pointers problem
//use multiple pointers to target the start and end of the desired sequence

//p1 tracks the number
//p2 tracks the letters
//use slice from p1 to p2 to generate the proper # of letters
//set p1 to p2, repeat

//goal here is to find the each sequence of number-letter, and then print letter number times
//set both pointers equal to 0

//loop over each character in the string
//increment p2 until p2 is equal to a letter
//slice from p1 until p2, this is your number

//set the string to be returned to itself concatenated with the character printed number times
//set p1 to p2, and repeat the process

function isLetter(char) {
  if (char.toLowerCase() >= "a" && char.toLowerCase() <= "z") return true;
  return false;
}

function repeatCharacter(string='', character, numRepeats) {
  let result = string;
  for (let i = 0; i < numRepeats; i++) {
    result =result + character;
  }
  return result;
}

function uncompress(s) {
  let p1 = 0;
  let p2 = 1;
  let toReturn = "";

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    if (isLetter(char)) {
      let num = s.slice(p1, i);
      toReturn = repeatCharacter(toReturn, char, num);
      p1 = i + 1;
    } else {
      continue;
    }
  }
  return toReturn;
}


module.exports = {
  uncompress, isLetter, repeatCharacter
};
