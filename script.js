function answer(correct){

    let result=document.getElementById("result");

    if(correct){

        result.innerHTML="✅ Correct! Never click unknown links.";
        result.style.color="green";
    }

    else{

        result.innerHTML="❌ Wrong! Unknown links may be phishing attacks.";
        result.style.color="red";
    }

}