function pairProduct(numbers, targetSum) {
  for (let i = 0; i < numbers.length; i++) {
    let num1 = numbers[i];
    for (let j = i + 1; j < numbers.length; j++) {
      let num2 = numbers[j];
      if (num1 * num2 === targetSum) return [i, j];
    }
  }
}
