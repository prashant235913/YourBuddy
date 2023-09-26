const questionBox = document.querySelector('.question-box');
const resultBox = document.querySelector('.result-box');
const guessedCharacter = document.getElementById('guessed-character');

document.querySelectorAll('.answer-btn').forEach(button => {
	button.addEventListener('click', () => {
		questionBox.style.display = 'none';
		resultBox.style.display = 'block';

		const answer = button.classList.contains('yes') ? 'Dora the Explorer' : 'Superman';
		guessedCharacter.textContent = answer;
	});
});
