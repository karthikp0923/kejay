const poemButton = document.querySelector('#poem-button');
const poemText = document.querySelector('#poem-text');
const poems = [
  "Life is like looking for your phone. Most of the time, its in your hand.",
  "I wandered lonely as a cloud\nThat floats on high o'er vales and hills,\nWhen all at once I saw a crowd,\nA host, of golden daffodils;",
  "The trouble with having an open mind is that people will insist on coming along and trying to put things in it."
];

poemButton.addEventListener('click', () => {
  const randomIndex = Math.floor(Math.random() * poems.length);
  poemText.innerHTML = poems[randomIndex];
});
