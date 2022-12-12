const button = document.getElementById("yak");
const img = document.getElementById("img");
console.log("a");
class Request{
    constructor(url){
        this.url = url;
    }

    async get(){
        const req = await fetch(this.url);
        const response = await req.text();
        console.log(response);
        return response;
    }
}   

const request = new Request("/yak");

button.addEventListener("click",yak);
function yak(e){
    request.get()
    .then(response => {
        if(response == "yakıldı"){
            button.innerText = "Söndür";
            img.src = "pic_bulbon.gif";
        }
        else if(response == "söndü"){
            button.innerText = "Yak";
            img.src = pic_bulboff.gif;
        }
    })
    .catch(err => console.log(err));
}
