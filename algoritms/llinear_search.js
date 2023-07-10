function linearSearch(array, item) {
  for (let i = 0; i < array.length; ++i) {
    if (array[i] == item) {
      return i;
    }
  }
  return null;
}

console.log(linearSearch([18, 6, 3, 9, 4, 2, 5, 8, 31], 8));
// O(n)
