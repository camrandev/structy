/**helper function to make a frequency table*/
function freqTable(string) {
  let freqTable = {};
  for (const char of string) {
    char in freqTable ? freqTable[char]++ : (freqTable[char] = 1);
  }
  return freqTable;
}

function anagrams (s1, s2) {
  let s1Table = freqTable(s1);
  let s2Table = freqTable(s2);

  for (const key in s1Table) {
    if (s1Table[key] != s2Table[key]) return false;
  }

  for (const key in s2Table) {
    if (s2Table[key] != s1Table[key]) return false;
  }

  return true;
};
