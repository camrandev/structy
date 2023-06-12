// class Node {
//   constructor(val) {
//     this.val = val;
//     this.next = null;
//   }
// }

//time complexity: O(n)
//space complexity: O(n)
const linkedListValues = (head) => {
  let result = [];
  let curr = head;

  while (curr) {
    result.push(curr.val);
    curr = curr.next;
  }

  return result;
};
