let currentInput = document.querySelector('.currentInput');
let answerScreen = document.querySelector('.answerScreen');
let buttons = document.querySelectorAll('button');
let eraseButton = document.querySelector('#erase');
let clearButton = document.querySelector('#clear');
let evaluateButton = document.querySelector('#evalute');
let realTimeSceenValue = []
clearButton.addEventListener("click",()=> {
    realTimeSceenValue = [''];
    answerScreen.innerHTML = 0;
    currentInput.className = 'currentInput';
    answerScreen.className = 'answerScreen';
    answerScreen.style.color = "rgba(150,150,150, 0.87)";
    buttons.forEach((btn) => {
        btn.addEventListener("click",() => {
            if(!btn.id.match('erase')){
                realTimeSceenValue.push(btn.value)
                currentInput = realTimeSceenValue.join('');
                if(btn.classList.contains('num-btn')){
                    answerScreen.innerHTML = eval(realTimeSceenValue.join(''));
                }
            }
            if(btn.id.match('erase')){
                realTimeSceenValue.pop();
                currentInput.innerHTML = realTimeSceenValue.join('');
                answerScreen.innerHTML = eval(realTimeSceenValue.join(''));
            }
            if(btn.id.match('evaluate')){
                currentInput.className = 'currentInput';
                answerScreen.className = 'answerScreen';
                answerScreen.style.color = "white";
            }
            if(typeof eval(realTimeSceenValue.join(''))=='undefined'){
                answerScreen.innerHTML = 0
            }
        })
    })
   

})