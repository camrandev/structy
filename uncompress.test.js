const { uncompress, isLetter, repeatCharacter } = require("./uncompress");


describe('isLetter', () => {
  test('should return true for letters and false for everything else', () => {
    expect(isLetter('a')).toBe(true);
    expect(isLetter('7')).toBe(false);
    expect(isLetter('!')).toBe(false);
  });
});

describe('repeatCharacter', () => {
  test('should return the correct string', () => {
    expect(repeatCharacter('','a', 2)).toBe('aa');
    expect(repeatCharacter('','b', 3)).toBe('bbb');
  });
});

describe('uncompress', () => {
  test('should return the correct string', () => {
    expect(uncompress("2c3a1t")).toBe('ccaaat');
    expect(uncompress("4s2b")).toBe('ssssbb');
    expect(uncompress("2p1o5p")).toBe('ppoppppp')
    expect(uncompress("3n12e2z")).toBe('nnneeeeeeeeeeeezz');
    expect(uncompress("127y")).toBe("y".repeat(127));
  });
});