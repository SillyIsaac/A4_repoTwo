console.log('hello world')

const helloWorldBox = document.getElementById('hello-world')
const postsBox = document.getElementById('posts-box')

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
        console.log(data)
        data.forEach(el=>
            {
                postsBox.innerHTML += `
                    ${el.title} - <b>${el.body}</b><br>`
            });
        // const data = JSON.parse(response.data)
        // console.log(data)
    },
    error: function(error){
        console.log(error)
    }
})