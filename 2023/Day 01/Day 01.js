const fs = require('fs')

const input = fs.readFileSync('./input.txt', 'utf8').split('\n')
let sum = 0

input.forEach(str => {
    str = str.replace(/\D+/g, '')
    str = str[0] + str.at(-1)
    sum += parseInt(str)
});

console.log(`Part 1 answer: ${sum}`);

sum = 0
const digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

input.forEach(str => {
    const strDigits = []

    for (let i = 0; i < str.length; i++) {
        digits.forEach((digit, j) => {
            if (str.slice(i).startsWith(digit)) strDigits.push(j + 1)
        })

        if (parseInt(str[i])) strDigits.push(parseInt(str[i]))
    }

    sum += strDigits[0] * 10 + strDigits.at(-1)
});

console.log(`Part 2 answer: ${sum}`)
