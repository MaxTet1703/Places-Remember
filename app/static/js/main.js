$(function($){
    ymaps.ready(function(){
        var map = new ymaps.Map("map", {
            center: [56.0102763820674, 92.85198816311457],
            zoom: 15,
            controls: []
        });
        map.events.add("click", (e) => {
            console.log(e.get("coords"))
            map.geoObjects.removeAll();
            map.geoObjects.add(new ymaps.Placemark(e.get("coords")));
            $('input[name="latitude"]').val(e.get("coords")[1]);
            $('input[name="longitude"]').val(e.get("coords")[0]);
        })
        render_maps();
    });
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
    $("#create").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: this.method,
            url: this.action,
            dataType: 'json',
            data: $(this).serialize(),
            success: function(response){
                console.log("Готово")
            },
            error: function(xhr, status, error){
                console.log("Вы потерпрели фиаско")
                console.log(error);
            }
        })
    });
});