//turn each array into an object
//loop over one of the objects, if the item is in the other object push it to results

//Time: O(2n) -> O(n)
//Space: O(3 + .5n) -> O(n)

//TODO: reattempt, using a set

function invertToObject(arr) {
  const result = {};
  for (let i = 0; i < arr.length; i++) {
    let el = arr[i];
    result[el] = i;
  }

  return result;
}

const intersection = (a, b) => {
  const objA = invertToObject(a);
  const objB = invertToObject(b);
  let results = [];

  for (const key in objA) {
    if (key in objB) {
      results.push(+key);
    }
  }

  return results;
};
