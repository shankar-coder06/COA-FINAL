document.getElementById('convertButton').addEventListener('click', () => {
  const fromChoice = document.getElementById('fromChoice').value;
  const toChoice = document.getElementById('toChoice').value;
  const inputNumber = document.getElementById('inputNumber').value;
  const resultDisplay = document.getElementById('resultDisplay');

  if (fromChoice === toChoice) {
    resultDisplay.innerHTML = "Cannot convert to the same form. Please select different types.";
    resultDisplay.style.display = 'block';
    return;
  }

  fetch('/conversion', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ fromChoice, toChoice, inputNumber })
  })
  .then(response => response.json())
  .then(data => {
    resultDisplay.innerHTML = `Conversion result: ${data.result}`;
    resultDisplay.style.display = 'block';
  })
  .catch(error => {
    resultDisplay.innerHTML = "An error occurred during the conversion.";
    resultDisplay.style.display = 'block';
  });
});
