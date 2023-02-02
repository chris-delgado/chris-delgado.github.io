---
layout: post
title: freeCodeCamp JavaScript Projects
image: "/posts/freeCodeCamp.png"
tags: [JavaScript, freeCodeCamp]
---
# JavaScript Algorithms and Data Structures Projects
freeCodeCamp's JavaScript Algorithms and Data Structures course provides a comprehensive and in-depth curriculum for learning JavaScript, with a focus on algorithms and data structures. The course covers topics such as basic programming concepts (variables, data types, loops, and functions), advanced algorithms (searching and sorting), and data structures (arrays, linked lists, stacks, and trees). 

The course provides hands-on experience through coding challenges and projects, allowing students to apply what they have learned and build a portfolio of work. Below are my code blocks for the five projects required to complete this course.

## Palindrome Checker
A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

This functions returns true if the given string is a palindrome. Otherwise, it returns false.
```javascript
function palindrome(string) {
  let regexPattern = /[^A-Za-z0-9]/g;
  let str = string.replace(regexPattern, "").toLowerCase();
  for (let i = 0; i < str.length/2; i++) {
    if (str[i] === str[str.length-(i+1)]) {
      continue;
    } else {
      return false;
    }
  }
  return true;
}
```

## Roman Numeral Converter
Converts the given number into a roman numeral.
```javascript
function romanHelper(quo, base) {
  let ans = '';
  let romanNum = '';

  switch(base) {
    case 1000:
      romanNum = 'M';
      break;
    case 900:
      romanNum = 'CM';
      break;
    case 500:
      romanNum = 'D';
      break;
    case 400:
      romanNum = 'CD';
      break;
    case 100:
      romanNum = 'C';
      break;
    case 90:
      romanNum = 'XC';
      break;
    case 50:
      romanNum = 'L';
      break;
    case 40:
      romanNum = 'XL';
      break;
    case 10:
      romanNum = 'X';
      break;
    case 9:
      romanNum = 'IX';
      break;
    case 5:
      romanNum = 'V';
      break;
    case 4:
      romanNum = 'IV';
      break;
    case 1:
      romanNum = 'I';
      break;
  }

  if (quo > 0) {
    for (let i = 0; i < quo; i++) {
      ans += romanNum;
    }
  }

  return ans;
}

function convertToRoman(num) {
  let quo;
  let rem = num;
  let ans = '';
  let bases = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

  for (let i = 0; i < bases.length; i++) {
    quo = Math.floor(rem / bases[i]);
    rem = rem % bases[i];
    ans += romanHelper(quo, bases[i]);
  }

  return ans;
}
```

## Caesars Cipher
One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.

A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. Thus A ↔ N, B ↔ O and so on.

This function takes a ROT13 encoded string as input and returns a decoded string.
```javascript
function rot13(str) {
  // Capital letters are ASCII codes 65 - 90
  let charCode;
  let ans = '';

  for (let i = 0; i < str.length; i++) {
    charCode = str.charCodeAt(i);
    if (charCode >= 65 && charCode < 65 + 13) {
      ans += String.fromCharCode(charCode + 26 - 13);
    } else if (charCode >= 65 + 13 && charCode <= 90) {
      ans += String.fromCharCode(charCode - 13);
    } else {
      ans += str[i];
    }
  }
  return ans;
}
```

## Telephone Number Validator
Returns true if the passed string looks like a valid US phone number.
```javascript
function telephoneCheck(str) {
  // uses a non-capturing group (?: ... ) to group the alternative patterns: either 3 digits inside parentheses, or just 3 digits.
  let regexPattern = /^1?\s?(?:\(\d{3}\)|\d{3})\s?-?\d{3}\s?-?\d{4}$/;
  return regexPattern.test(str);
}
```

## Cash Register
A cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.

Returns {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change.

Returns {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due.

Otherwise, returns {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key.

```javascript
function checkCashRegister(price, cash, cid) {
  let diff = cash - price;
  let values = [.01, .05, .1, .25, 1, 5, 10, 20, 100]
  let change = [];
  let status;
  let amt;
  let closedRegister;
  let cidCopy = cid.map(innerArray => innerArray.slice());

  for (let i = cid.length-1; i >= 0; i--) {
    if (diff >= values[i] && cid[i][1] > 0) {
      if (cid[i][1] >= diff) {
        amt = Math.floor(diff / values[i]) * values[i];
        diff = (diff - amt).toFixed(2);
        change.push([cid[i][0], amt]);
        cid[i][1] = (cid[i][1] - amt).toFixed(2);
      } else {
        diff = (diff - cid[i][1]).toFixed(2);
        change.push([cid[i][0], cid[i][1]]);
        cid[i][1] = (cid[i][1] - diff).toFixed(2);
      }
    }
  }

  // Check if register is empty
  for (let i = 0; i < cid.length; i++) {
    if (cid[i][1] == 0) {
      closedRegister = 1;
      continue;
    } else {
      closedRegister = 0;
      break;
    }
  }

  // STATUS
  if (diff == 0.00 && closedRegister) {
    status = "CLOSED";
    change = cidCopy;
  } else if (diff == 0.00) {
    status = "OPEN";
  } else {
    status = "INSUFFICIENT_FUNDS";
    change = [];
  }

  return {"status": status, "change": change};
}
```
