document.addEventListener('DOMContentLoaded', ()=>{

    // JavaScript kod

    let generate = document.getElementById('generateInput');
    const inputShortUrl = document.getElementById('inputShortUrl')
    generate.addEventListener('change', ()=>{
        if (generate.checked) {
            inputShortUrl.classList.add('hidden')
        } else {
            inputShortUrl.classList.remove('hidden')
        }
    })

    const showUrlQrc = document.querySelectorAll('.url_qr')
    const btnShowUrlQr = document.querySelectorAll('.btn-check')
    btnShowUrlQr.forEach((btn, index)=>{
        btn.addEventListener('change', ()=>{
            if (btn.checked) {
                showUrlQrc.forEach((element)=>{
                    element.classList.remove('active')
                })
                showUrlQrc[index].classList.add('active')
            }
        })
    }) 



    document.getElementById('copyButton').addEventListener('click', function () {
        var content = document.getElementById('short_url');
        var contentDomain = document.getElementById('domain');
        var textToCopy = content.innerText || content.textContent;
        var textToCopyDomain = contentDomain.innerText || contentDomain.textContent;
        let shortUrl = `${textToCopyDomain}${textToCopy}`
        navigator.clipboard.writeText(shortUrl)
        this.classList.add('clicked');
        setTimeout(() => {
            this.classList.remove('clicked');
        }, 1000);
    });
    
    function setHrefAndDownload() {
        const link = document.createElement('a');
        const qrCodeImage = document.getElementById('qr_code');
    
        link.href = qrCodeImage.src;
        link.download = 'qr_code.png';
        link.click();
    }

    document.getElementById('download').addEventListener('click', function () {
        const link = document.createElement('a');
        const qrCodeImage = document.getElementById('qr_code');
    
        // Ensure the image is loaded
        if (qrCodeImage.complete) {
            // If the image is already loaded
            setHrefAndDownload();
        } else {
            // If the image is not loaded, wait for the onload event
            qrCodeImage.onload = function () {
                setHrefAndDownload();
            };
        }
    });

    document.getElementById('shareQr').addEventListener('click', function () {
        const qrCodeImage = document.getElementById('qr_code');
        const dataUrl = qrCodeImage.src;
        if (navigator.share) {
          navigator.share({
            title: 'QR Code',
            text: 'Check out this QR Code',
            url: dataUrl
          })
            .then(() => console.log('Shared successfully'))
            .catch((error) => console.log('Error sharing:', error));
        } else {
          const newWindow = window.open(dataUrl);
          if (!newWindow) {
            alert('Pop-up blocked. Please allow pop-ups for this website and try again.');
          }
        }
    })

    var infoApi = (API)=>{
        fetch(API, {
            method: "get",
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            var urlCounter = document.getElementById('url_counter').innerText = data['counter']
        })
        .catch((error) => {
            console.log('Error:', error);
        });
    }
    const APIInfo = 'http://127.0.0.1:8000/info/api/'
    infoApi(APIInfo)


    var postApi = (API, data, csrf)=>{
        fetch(API, {
            method: "post",
            headers: {
                'X-CSRFToken': csrf,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },

            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            var qrCode = document.getElementById('qr_code')
            qrCode.src = `${data['qr_code']}`
            var downloadImg = document.getElementById('download').href = `${data['qr_code']}`
            var urlCounter = document.getElementById('url_counter').innerText = data['counter']
            var shortUrl = document.getElementById('short_url').innerText = data['url_short']
            var message = document.getElementById('message').innerText = data['message']
            if (data['status'] == 200) {
                const typeLinkBtn = document.getElementById('responseCard').classList.add('active');
            } else{
                const typeLinkBtn = document.getElementById('responseCard').classList.remove('active');
            }
        })
        .catch((error) => {
            console.log('Error:', error);
        });
    }





    document.getElementById('postForm').addEventListener('submit', function (event) {
        event.preventDefault()

        var urlLong = document.getElementById('urlLongInput').value;
        var urlShort = document.getElementById('urlShortInput').value;
        var generate = document.getElementById('generateInput').checked;
        var select1 = document.querySelector('.form-select1 option:checked').text;
        var select2 = document.querySelector('.form-select2 option:checked').text;
        var data = {
            url_long: urlLong,
            url_short: urlShort,
            generate: generate,
            select_1: select1,
            select_2: select2
        };
        if(generate){
            if (urlLong) {
                var requirement_long = document.getElementById('requirement_long').innerText = '';
                var API = 'http://127.0.0.1:8000/create/url/api/'
                var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
                postApi(API, data, csrf)
            } else {
                var requirement_long = document.getElementById('requirement_long').innerText = 'Please enter your long URL';
            }
        } else{
            if (urlLong) {
                var requirement_long = document.getElementById('requirement_long').innerText = '';
                if (urlShort.trim() !== '' && urlShort.length >= 6) {
                    var requirement_short = document.getElementById('requirement_short').innerText = '';
                    var API = 'http://127.0.0.1:8000/create/url/api/'
                    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
                    postApi(API, data, csrf)
                } else{
                    var requirement_short = document.getElementById('requirement_short').innerText = 'At least 6 characters must be entered';
                }
            } else {
                var requirement_long = document.getElementById('requirement_long').innerText = 'Please enter your long URL';
            }
        }
    });









})