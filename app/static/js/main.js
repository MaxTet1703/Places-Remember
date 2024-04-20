$(function($){
    ymaps.ready(function(){
        var map = new ymaps.Map("map", {
            center: [56.0102763820674, 92.85198816311457],
            zoom: 10,
            controls: []
        });
        map.events.add("click", (e) => {
            console.log(e.get("coords"))
            map.geoObjects.removeAll();
            map.geoObjects.add(new ymaps.Placemark(e.get("coords")));
            $('input[name="latitude"]').val(e.get("coords")[1]);
            $('input[name="longitude"]').val(e.get("coords")[0]);
        })
    });
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