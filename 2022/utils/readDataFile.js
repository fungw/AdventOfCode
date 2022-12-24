import { readFile } from 'fs/promises';

export default async function readDataFile(fileName) {
  try {
    const data = await readFile(fileName, 'utf-8');
    return data;
  } catch (err) {
    console.log(err);
  }
}
