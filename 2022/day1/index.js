import readDataFile from '../utils/readDataFile.js';

const data = await readDataFile('./day1/data.txt');
const sum = (arrOfNum) => arrOfNum.reduce((acc, curr) => acc + +curr, 0);

const highestCalorie = data.split('\n\n').reduce((acc, curr) => {
  const sumElfCalories = sum(curr.split('\n'));
  return (acc > sumElfCalories) ? acc : sumElfCalories;
});

const summedCaloriesPerElf = data.split('\n\n').map((test) => {
  return sum(test.split('\n'));
}).sort((a, b) => b - a).slice(0, 3);
