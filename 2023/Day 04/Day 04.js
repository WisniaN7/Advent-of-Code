const fs = require('fs')

const tickets = fs.readFileSync('input.txt', 'utf8').split('\n').map(line => line.replace(/Card\s+\d+:/g, '').trim().split('|'))
let points = 0
let cards = {}

tickets.forEach((ticket, i) => cards[i + 1] = 1)

tickets.forEach((ticket, i) => {
    let [winning, owned] = ticket
    i = i + 1
    
    winning = winning.trim().split(/\s+/g).map(num => parseInt(num))
    owned = owned.trim().split(/\s+/g).map(num => parseInt(num))

    const scored = owned.filter(num => winning.includes(num)).length

    if (scored > 0)
        points += Math.pow(2, scored - 1)

    for (let j = i + 1; j <= i + scored; j++)
        cards[j] += cards[i]
})

console.log(`Part 1 answer: ${points}`);
console.log(`Part 2 answer: ${Object.values(cards).reduce((a, b) => a + b, 0)}`);
