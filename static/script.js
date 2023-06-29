let input = document.querySelector("input");

input.addEventListener('input', async function(){
    let response = await fetch('/?search=' + input.value)
    console.log(response)
    let show = await response.text();
    document.querySelector('.content').innerHTML = show;

}

)
