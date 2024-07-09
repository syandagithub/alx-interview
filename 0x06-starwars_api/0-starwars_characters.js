#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

async function getCharacterNames(characterURL) {
  try {
    const response = await request.get(characterURL);
    const characterData = JSON.parse(response.body);
    return characterData.name;
  } catch (error) {
    console.error(error);
    return null; 
  }
}

async function getMovieCharacters(movieID) {
  try {
    const response = await request.get(`${API_URL}/films/${movieID}`);
    const movieData = JSON.parse(response.body);
    const characterPromises = movieData.characters.map(getCharacterNames);
    const characterNames = await Promise.all(characterPromises);
    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error(error);
  }
}

if (process.argv.length > 2) {
  getMovieCharacters(process.argv[2]);
}
