import readDataFile from '../utils/readDataFile.js';
const data = await readDataFile('./day2/data.txt');

// scores for hand played
const PAPER = {
  beats: 'rock',
  id: 'paper',
  loses: 'scissors',
  score: 2,
};
const ROCK = {
  beats: 'scissors',
  id: 'rock',
  loses: 'paper',
  score: 1,
};
const SCISSORS = {
  beats: 'paper',
  id: 'scissors',
  loses: 'rock',
  score: 3,
};

const HAND_MAPPING = {
  A: ROCK,
  B: PAPER,
  C: SCISSORS,
  X: ROCK,
  Y: PAPER,
  Z: SCISSORS,
  'paper': PAPER,
  'rock': ROCK,
  'scissors': SCISSORS,
};

// scores for round outcome
const DRAW = {
  id: 'draw',
  score: 3,
};
const LOSE = {
  id: 'lose',
  score: 0,
};
const WIN = {
  id: 'win',
  score: 6,
};

const FIX_MAPPING = {
  X: LOSE,
  Y: DRAW,
  Z: WIN,
}

const scoring = (handA, handB) => {
  const resolvedHandA = HAND_MAPPING[handA];
  const resolvedHandB = HAND_MAPPING[handB];
  if (resolvedHandA.id === resolvedHandB.id) {
    return resolvedHandB.score + DRAW.score;
  }
  if (resolvedHandA.id === resolvedHandB.beats) {
    return resolvedHandB.score + WIN.score;
  }
  return resolvedHandB.score + LOSE.score;
}

const rounds = data.split('\n');
const part1 = rounds.reduce((acc, round) => {
  const [handA, handB] = round.split(' ');
  acc += scoring(handA, handB);
  return acc;
}, 0);

const part2Scoring = (handA, handB) => {
  const fixedOutcome = FIX_MAPPING[handB];
  const resolvedHandA = HAND_MAPPING[handA];
  if (fixedOutcome.id === 'draw') {
    return resolvedHandA.score + fixedOutcome.score;
  }
  if (fixedOutcome.id === 'win') {
    return HAND_MAPPING[resolvedHandA.loses].score + fixedOutcome.score;
  }
  return HAND_MAPPING[resolvedHandA.beats].score + fixedOutcome.score;
}
const part2 = rounds.reduce((acc, round) => {
  const [handA, handB] = round.split(' ');
  acc += part2Scoring(handA, handB);
  return acc;
}, 0);
