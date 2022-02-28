var selector = document.getElementById('video-selector')
var video = document.getElementById('video')
var confirm = document.getElementById('confirm')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function static_video_url(id) { return "/static/results/" + String(id) + '.webm' }

selector.addEventListener('change', ev => {
    $('#select-modal').modal('show')
})

function send_data(where, data, onsuccess) {
    $.ajax({
        type: "POST",
        url: where,
        data: JSON.stringify(data),
        headers: {'X-CSRFToken': csrftoken},
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: res => onsuccess(res),
        failure: err => console.error(err)
    })
}

var speed = document.getElementById('speed-value') 
var fine = document.getElementById('fine-value')
var plate = document.getElementById('plate')
var image = document.getElementById('image')
function set_data(key, data) {
    speed.value = data['speed']
    fine.value = data['fine']
    plate.textContent = data['name plate']
    image.setAttribute('src', '/static/results/' + String(key) + '.jpg')
}

var not_current = null
function create_table_row(value, id, plate, speed) {
    var tr = document.createElement('tr')
    tr.setAttribute('val', value)
    tr.setAttribute('select', id)
    var th = document.createElement('th')
    th.innerText = current
    var td1 = document.createElement('td')
    var currentdate = new Date(); 
    var datetime = currentdate.getDate() + "/"
                    + (currentdate.getMonth()+1)  + "/" 
                    + currentdate.getFullYear() + ' '
                    + currentdate.getHours() + ":"  
                    + currentdate.getMinutes() + ":" 
                    + currentdate.getSeconds();
    td1.textContent = datetime
    var td2 = document.createElement('td')
    td2.textContent = plate
    var td3 = document.createElement('td')
    td3.textContent = speed

    tr.append(th, td1, td2, td3)

    tr.addEventListener('click', ev => {
        var data = results[value]
        not_current = data

        set_data(id, data)

        document.getElementById('main').style.display = 'none'
        document.getElementById('result').style.display = 'block'
    })
    return tr
}

var video_flag = true
function videoend(ev) {
    if (video_flag) {

        send_data(window.location, {'selected': selector.value}, res => {
            results[current] = res
            var tr = create_table_row(current, selector.value, res['name plate'], res['speed'])
            tbody.appendChild(tr)
            video.setAttribute('src', "/static/results/" + String(selector.value) + '_.webm')
            video.setAttribute('controls', true)
            video.removeAttribute('autoplay')
            current = current + 1
    
            $('#result-modal').modal('show')
        })

        video_flag = false

    }

}

var tbody = document.getElementById('table-body')
var results = {}
var current = 1
confirm.addEventListener('click', ev => {
    $('#select-modal').modal('hide')
    video.setAttribute('src', static_video_url(selector.value))
    video.removeAttribute('controls')
    video.setAttribute('autoplay', true)

    video_flag = true
    video.addEventListener('ended', videoend)
})

document.getElementById('great').addEventListener('click', ev => {
    $('#result-modal').modal('hide')
})

document.getElementById('back').addEventListener('click', ev => {
    document.getElementById('result').style.display = 'none'
    document.getElementById('main').style.display = 'block'
})


document.getElementById('report').addEventListener('click', ev => {
    document.getElementById('number-here').innerHTML = plate.innerHTML
    $("#report-modal").modal('show');
})

document.getElementById('report-modal-btn').addEventListener('click', ev => {
    $("#report-modal").modal('hide');
    not_current['comment'] = document.getElementById('comment').value
    send_data(window.location,{'type': 'report', 'data': not_current },res=>{})

})