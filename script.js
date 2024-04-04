function checkAnswer() {
  var answer = document.getElementById('answer').value;
  if (answer == '4') {
    document.getElementById('result').innerText = 'Correct!';
  } else {
    document.getElementById('result').innerText = 'Incorrect. Try again!';
  }
}