const fs = require('fs')

const games = fs.readFileSync('input.txt', 'utf8').split('\n').map(line => line.replace('\r', '').replace(/Game \d+:/, '').split(';'))
games.forEach(game => game = game.map(line => line.split(',') ))

for (let i = 0; i < games.length; i++)
    games[i] = games[i].map(line => line.split(','))

const maxAmounts = {
    red: 12,
    green: 13,
    blue: 14
}

let sumOfImpossibleGamesIndexes = (games.length * (games.length + 1)) * 0.5
let powerSum = 0

for (let i = 0; i < games.length; i++) {
    const game = games[i]
    let isPossible = true
    const minBalls = {
        red: 0,
        green: 0,
        blue: 0
    }

    for (let j = 0; j < game.length; j++) {
        const set = game[j]
        
        for (let k = 0; k < set.length; k++) {
            let cubes = set[k]
            const [amount, colour] = cubes.trim().split(' ')
            minBalls[colour] = Math.max(minBalls[colour], amount)

            if (isPossible && amount > maxAmounts[colour]) {
                sumOfImpossibleGamesIndexes -= i + 1
                isPossible = false
            }
        }
    }

    powerSum += Object.values(minBalls).reduce((a, b) => a * b)
}

console.log(`Part 1 answer: ${sumOfImpossibleGamesIndexes}`);
console.log(`Part 2 answer: ${powerSum}`)
