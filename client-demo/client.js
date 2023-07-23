const content = document.getElementById("content")
const fileform = document.getElementById("form-file")
base_url = "http://localhost:8000/api/formteams"

if (fileform){
    fileform.addEventListener('submit', handleFileForm)
}

Object.prototype.prettyPrint = function(){
    var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
    var replacer = function(match, pIndent, pKey, pVal, pEnd) {
        var key = '<span class="json-key" style="color: brown">',
            val = '<span class="json-value" style="color: navy">',
            str = '<span class="json-string" style="color: olive">',
            r = pIndent || '';
        if (pKey)
            r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
        if (pVal)
            r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
        return r + (pEnd || '');
    };

    return JSON.stringify(this, null, 3)
        .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
        .replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(jsonLine, replacer);
}

async function handleFileForm(event){
    console.log(event)
    event.preventDefault()
    console.log("hello")
    const fileEndpoint = `${base_url}/formteams`
    const formdata = new FormData(fileform)
    console.log(formdata)
    const requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
    };

    const res = await fetch("http://localhost:8000/api/formteams", requestOptions)
    const result = await res.json()
    document.getElementById('teams').innerHTML = result.prettyPrint()
    console.log(result)
}

