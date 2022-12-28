import readDataFile from '../utils/readDataFile.js';
const data = await readDataFile('./day3/data.txt');
const alphabetLookup = {a:1,b:2,c:3,d:4,e:5,f:6,g:7,h:8,i:9,j:10,k:11,l:12,m:13,n:14,o:15,p:16,q:17,r:18,s:19,t:20,u:21,v:22,w:23,x:24,y:25,z:26};

const isUpperCase = (letter) => letter.toUpperCase() === letter

const intersection = (letter, searchArray) => {
  if (searchArray.filter(x => x === letter).length >= 1) {
    return letter;
  }
  return false;
}

const compare = (firstCompartment, secondCompartment) => {
  let resolvedLookup = 0;
  firstCompartment.forEach(letter => {
    const matchingLetter = intersection(letter, secondCompartment)
    if (matchingLetter) {
      if (isUpperCase(letter)) {
        resolvedLookup = alphabetLookup[matchingLetter.toLowerCase()] + Object.keys(alphabetLookup).length;
      } else {
        resolvedLookup = alphabetLookup[matchingLetter.toLowerCase()];
      }
    }
  });
  return resolvedLookup;
}

const rucksacks = data.split('\n');
let resolvedCount = 0;
rucksacks.map((compartment => {
  const compartmentLength = compartment.length / 2;
  const firstCompartment = compartment.slice(0, compartmentLength);
  const secondCompartment = compartment.slice(compartmentLength, compartment.length);
  resolvedCount += compare(firstCompartment.split(""), secondCompartment.split(""));
}));

console.log(resolvedCount);
