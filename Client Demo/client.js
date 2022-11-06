const content = document.getElementById("content")
const fileform = document.getElementById("file")
base_url = "https://localhost:8000/api"

if (fileform){
    fileform.addEventListener('submit', handleFileForm)
}

function handleFileForm(event){
    console.log(event)
    event.preventDefault()
    console.log("hello")
    const fileEndpoint = `${base_url}/formteams`
    // const formData = newFormData(fileform)
    
    // content.innerHTML = "<p>Hello World</p>"
    // const options = {
    //     method: "POST",
    //     enctype: "multipart/form-data"
    // }
    // fetch(base_url, options)
    // .then(response=>{
    //     consolve.log(response)
    //     return response.json()
    // })
    // .then(response=>{
    //     console.log(response)
    // })
    // .catch(err=>{
    //     console.log('err', err)
    // })
    var formdata = new FormData(fileform);
    // formdata.append("file", fileInput.files[0], "/D:/Coding/Projects/Dream11-py/Fantasy-Sports-Team-Maker/backend/Main/sample.csv");
    console.log(formData)
    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };

    fetch("http://localhost:8000/api/formteams", requestOptions)
    .then(response => response.text())
    .then(result => {
        console.log(result)
        content.innerHTML = "<p>Hello world</p>"
    })
    .catch(error => console.log('error', error));
}