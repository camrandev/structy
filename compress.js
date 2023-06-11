const compress = (s) => {

  //start with two pointers, both set to 0
  //iterate over the provided string, incrementing one pointer as you go

  //inside the loop
    //check if the current + next char are the same
    //once they are not
      //copy the string from p1 to p2
      //push the length of the copy + the character at p1 to the new string
      //set p1 and p2 equal to the current position of p2 + 1
      //repeat
  let result = ''
  let p1 = 0
  let p2 = 0

  for (p1; p1 < s.length; p1++) {

    while (s[p1] === s[p1+1]) {
      p1++
    }

    let segment = s.slice(p2, p1 + 1)
    count = segment.length === 1 ? "" : segment.length
    result = result + `${count}`+ `${s[p2]}`
    p1, p2 = p1+1
  }
  return result


};

console.assert(compress('ccaaatsss'), '2c3at3s')

module.exports = {
  compress,
};

