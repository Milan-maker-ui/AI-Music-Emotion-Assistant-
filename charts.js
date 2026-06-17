let chartInstance = null;
const form =
document.getElementById(
'emotionForm'
);

form.addEventListener(
'submit',
async function(e)
{
    e.preventDefault();
    const loading =
    document.getElementById(
    'loading'
    );

    const results =
    document.getElementById(
    'results'
    );

    loading.style.display =
    'block';
    results.classList.add(
    'hidden'
    );

    const formData =
    new FormData();
    formData.append(
    'text',
    document.getElementById(
    'text'
    ).value
    );

    try{
        const response =
        await fetch(
        '/analyze',
        {
            method:'POST',
            body:formData
        });

        const data =
        await response.json();
        loading.style.display =
        'none';
        results.classList.remove(
        'hidden'
        );

        document.getElementById(
        'emotion'
        ).innerHTML =
        '🎯 ' +
        data.emotion.toUpperCase();
        document.getElementById(
        'translatedText'
        ).innerText =
        data.translated_text;
        document.getElementById(
        'botReply'
        ).innerText =
        data.bot_reply;
        loadSongs(
        data.recommendations
        );

        loadConfidenceBars(
        data.confidence_scores
        );

        createChart(
        data.confidence_scores
        );

    }
    catch(error){
        console.error(error);
        loading.style.display =
        'none';
        alert(
        'Error occurred.'
        );
    }
});

function loadSongs(songs){
    const list =
    document.getElementById(
    'songs'
    );

    list.innerHTML = '';
    songs.forEach(song => {
        const li =
        document.createElement(
        'li'
        );

        li.innerText =
        song;
        list.appendChild(
        li
        );
    });
}

function loadConfidenceBars(
scores
){
    const container =
    document.getElementById(
    'confidenceBars'
    );

    container.innerHTML =
    '';

    Object.entries(scores)
    .forEach(
    ([emotion,value])=>{
        container.innerHTML +=
        `
        <div class="bar-container">
            <div class="bar-label">
                <span>
                ${emotion}
                </span>
            
                <span>
                ${value}%
                </span>

            </div>

            <div class="bar">
                <div class="fill"
                style="width:${value}%">
                </div>
            </div>

        </div>
        `;
    });
}

function createChart(scores){
    const ctx =
    document.getElementById(
    'emotionChart'
    );

    const labels =
    Object.keys(scores);
    const values =
    Object.values(scores);

    if(chartInstance){
        chartInstance.destroy();
    }

    chartInstance =
    new Chart(
    ctx,
    {
        type:'pie',
        data:{
            labels:labels,
            datasets:[{
                data:values
            }]
        },

        options:{
            responsive:true,
            plugins:{
                legend:{
                    position:'bottom'
                }
            }
        }
    });
}