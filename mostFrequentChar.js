//create an object that will hold keys of the letters
// each key will have two values: count, first index

//set a variable outside of the function called firsAppeared to track the appearence

//loop over the string parameter. On each iteration take the following actions
//if the character exists in the in the mapping object, increment its count
//if the character does not exist, increment its count and set its firstAppeared
//attribute to the current index

//check if the current count is greater than the current max AND if index of the current
//letter is less than the currentMaxIndex

//if so, change the current max char to the current char, and the current max index
//to the current chars first appeared values

//return the most frequent char

function mostFrequentChar(s) {
  const table = {};
  let mostFreqChar;
  let mostFreqCharCount = -Infinity;

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    if (char in table) {
      table[char].count++;
    } else {
      table[char] = { count: 1, firstAppeared: i };
    }

    curr = table[char];
  }

  for (const key in table) {
    let curr = table[key];
    if (curr.count > mostFreqCharCount) {
      mostFreqCharCount = curr.count;
      mostFreqChar = key;
    }

    if (curr.count === mostFreqCharCount) {
      if (curr.firstAppeared < table[mostFreqChar].firstAppeared) {
        mostFreqCharCount = curr.count;
        mostFreqChar = key;
      }
    }
  }
  console.log(mostFreqChar);
  return mostFreqChar;
}

module.exports = {
  mostFrequentChar,
};
