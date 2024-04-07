console.log('hello world')

const helloWorldBox = document.getElementById('hello-world')
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')

helloWorldBox.innerHTML = 'hello world'

$.ajax({
    type: 'GET',
    url: '/hello-world',
    success: function(response){
        console.log('success', response)
        helloWorldBox.textContent = response.text
    },
    error: function(error)
    {
        console.log('error', error)
    }
})

$.ajax({
    type: 'GET',
    url: '/data/',
    success: function(response){
        console.log(response)
        const data = response.data
        setTimeout(() =>
        {
            spinnerBox.classList.add('not-visible')
            console.log(data)
            data.forEach(el=>
                {
                    postsBox.innerHTML += `
                    <div class="card mb-2">
                     
                    <div class="card-body">
                         <h5 class="card-title">${el.title}</h5>
                        <p class="card-text">${el.body}</p>
                        
                        
                    </div>
                    <div class="card-footer">
                        <div class="row">
                            <div class="col-1">
                                <a href="#" class="btn btn-primary">Details</a>
                            </div>
                            <div class="col-1">
                            <a href="#" class="btn btn-primary">Like</a>
                            </div>
                        </div>
                        
                        </div>
                </div>`
                       
                        
                    
                });
        }, 1000)
        
        // const data = JSON.parse(response.data)
        // console.log(data)
    },
    error: function(error){
        console.log(error)
    }
})