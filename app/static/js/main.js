$(function($){
    ymaps.ready(function(){
        var map = new ymaps.Map("map", {
            center: [56.0102763820674, 92.85198816311457],
            zoom: 15,
            controls: []
        });
        if($('input[name="latitude"]').val()){
            map.geoObjects.add(new ymaps.Placemark([$('input[name="longitude"]').val(),
                                                    $('input[name="latitude"]').val()]));
        }
        map.events.add("click", (e) => {
            console.log(e.get("coords"))
            map.geoObjects.removeAll();
            map.geoObjects.add(new ymaps.Placemark(e.get("coords")));
            $('input[name="latitude"]').val(e.get("coords")[1]);
            $('input[name="longitude"]').val(e.get("coords")[0]);
        })
        if (Array.from($("div.map")).length !=0){
            render_maps();
        }
    });
    // Отображение карт для каждого отзыва 
    function render_maps(){
        Array.from($("div.map")).forEach(element => {
            var map = new ymaps.Map($(element).attr("id"),{
                center: [$(element).attr("longitude"), $(element).attr("latitude")],
                zoom: 15,
                controls: []
            });
            map.geoObjects.add(new ymaps.Placemark([$(element).attr("longitude"), $(element).attr("latitude")])) 
        });
    }
    // Отправка данных для создания/изменения отзыва
    $("#create").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: this.method,
            url: this.action,
            dataType: 'json',
            data: $(this).serialize(),
            success: function(response){
                alert(response.message);
                window.location.pathname = 'main/'
            },
            error: function(xhr, status, error){
                alert("Заполните данные корректно и не забудьте отметить место на карте")
            }
        })
    });
});